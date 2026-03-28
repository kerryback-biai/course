from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.database.user_db import init_db
from app.auth.routes import router as auth_router
from app.admin.routes import router as admin_router
from app.chat.routes import router as chat_router

STATIC_DIR = "app/static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="AI Data Assistant", lifespan=lifespan)

# API routes first
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(chat_router)

# Static assets (CSS, JS)
app.mount("/css", StaticFiles(directory=f"{STATIC_DIR}/css"), name="css")
app.mount("/js", StaticFiles(directory=f"{STATIC_DIR}/js"), name="js")


# HTML pages
@app.get("/")
@app.get("/login.html")
async def login_page():
    return FileResponse(f"{STATIC_DIR}/login.html")


@app.get("/index.html")
async def index_page():
    return FileResponse(f"{STATIC_DIR}/index.html")


@app.get("/admin.html")
async def admin_page():
    return FileResponse(f"{STATIC_DIR}/admin.html")
