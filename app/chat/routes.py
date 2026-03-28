import asyncio
from typing import AsyncGenerator

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.auth.dependencies import get_current_user
from app.chat.agent import run_agent

router = APIRouter(prefix="/api", tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    history: list[dict] = []


async def async_generator_wrapper(sync_gen) -> AsyncGenerator[str, None]:
    """Wrap a sync generator to run in a thread, yielding results asynchronously."""
    import queue
    import threading

    q: queue.Queue = queue.Queue()
    sentinel = object()

    def producer():
        try:
            for item in sync_gen:
                q.put(item)
        except Exception as e:
            q.put(e)
        finally:
            q.put(sentinel)

    thread = threading.Thread(target=producer, daemon=True)
    thread.start()

    while True:
        item = await asyncio.to_thread(q.get)
        if item is sentinel:
            break
        if isinstance(item, Exception):
            break
        yield item


@router.post("/chat")
async def chat(req: ChatRequest, user: dict = Depends(get_current_user)):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    sync_gen = run_agent(
        message=req.message,
        history=req.history,
        user_id=user["id"],
    )

    return StreamingResponse(
        async_generator_wrapper(sync_gen),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
