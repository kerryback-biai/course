import sqlite3
from pathlib import Path
from contextlib import contextmanager

from app.config import settings

DB_PATH = settings.database_path


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


@contextmanager
def get_db():
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with get_db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                name TEXT NOT NULL DEFAULT '',
                is_admin INTEGER DEFAULT 0,
                is_active INTEGER DEFAULT 1,
                spending_limit_cents INTEGER DEFAULT 1000,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS usage_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER REFERENCES users(id),
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                input_tokens INTEGER DEFAULT 0,
                output_tokens INTEGER DEFAULT 0,
                cache_read_tokens INTEGER DEFAULT 0,
                model TEXT,
                cost_cents REAL DEFAULT 0,
                tool_calls INTEGER DEFAULT 0,
                request_type TEXT DEFAULT 'chat'
            );

            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER REFERENCES users(id),
                alert_type TEXT,
                message TEXT,
                acknowledged INTEGER DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            CREATE INDEX IF NOT EXISTS idx_usage_user ON usage_log(user_id);
            CREATE INDEX IF NOT EXISTS idx_usage_timestamp ON usage_log(timestamp);
        """)


def get_user_by_email(email: str) -> dict | None:
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()
        return dict(row) if row else None


def get_user_by_id(user_id: int) -> dict | None:
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        return dict(row) if row else None


def create_user(email: str, password_hash: str, name: str = "",
                is_admin: bool = False, spending_limit_cents: int | None = None) -> int:
    limit = spending_limit_cents or settings.default_spending_limit_cents
    with get_db() as conn:
        cursor = conn.execute(
            """INSERT INTO users (email, password_hash, name, is_admin, spending_limit_cents)
               VALUES (?, ?, ?, ?, ?)""",
            (email, password_hash, name, int(is_admin), limit)
        )
        return cursor.lastrowid


def list_users() -> list[dict]:
    with get_db() as conn:
        rows = conn.execute(
            """SELECT u.id, u.email, u.name, u.is_admin, u.is_active,
                      u.spending_limit_cents, u.created_at,
                      COALESCE(SUM(l.cost_cents), 0) as total_cost_cents
               FROM users u
               LEFT JOIN usage_log l ON u.id = l.user_id
               GROUP BY u.id
               ORDER BY u.created_at DESC"""
        ).fetchall()
        return [dict(r) for r in rows]


def update_user(user_id: int, **kwargs) -> None:
    allowed = {"name", "is_active", "is_admin", "spending_limit_cents"}
    updates = {k: v for k, v in kwargs.items() if k in allowed}
    if not updates:
        return
    set_clause = ", ".join(f"{k} = ?" for k in updates)
    values = list(updates.values()) + [user_id]
    with get_db() as conn:
        conn.execute(f"UPDATE users SET {set_clause} WHERE id = ?", values)


def log_usage(user_id: int, input_tokens: int, output_tokens: int,
              cache_read_tokens: int, model: str, cost_cents: float,
              tool_calls: int = 0, request_type: str = "chat") -> None:
    with get_db() as conn:
        conn.execute(
            """INSERT INTO usage_log
               (user_id, input_tokens, output_tokens, cache_read_tokens,
                model, cost_cents, tool_calls, request_type)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (user_id, input_tokens, output_tokens, cache_read_tokens,
             model, cost_cents, tool_calls, request_type)
        )


def get_user_total_cost(user_id: int) -> float:
    with get_db() as conn:
        row = conn.execute(
            "SELECT COALESCE(SUM(cost_cents), 0) as total FROM usage_log WHERE user_id = ?",
            (user_id,)
        ).fetchone()
        return row["total"]


def get_usage_summary(user_id: int | None = None) -> list[dict]:
    with get_db() as conn:
        if user_id:
            rows = conn.execute(
                """SELECT * FROM usage_log WHERE user_id = ?
                   ORDER BY timestamp DESC LIMIT 200""",
                (user_id,)
            ).fetchall()
        else:
            rows = conn.execute(
                """SELECT l.*, u.email, u.name
                   FROM usage_log l JOIN users u ON l.user_id = u.id
                   ORDER BY l.timestamp DESC LIMIT 500"""
            ).fetchall()
        return [dict(r) for r in rows]
