import aiosqlite
import time

DB_FILE = "database.db"

async def init():
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                full_name TEXT,
                balance INTEGER DEFAULT 0,
                referrer_id INTEGER,
                ref_rewarded INTEGER DEFAULT 0,
                ref_earned INTEGER DEFAULT 0,
                banned INTEGER DEFAULT 0,
                created_at INTEGER
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS buttons (
                key TEXT PRIMARY KEY,
                text TEXT,
                style TEXT,
                emoji_id TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS texts (
                key TEXT PRIMARY KEY,
                text TEXT,
                media_type TEXT,
                media_id TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS emoji_map (
                char TEXT PRIMARY KEY,
                emoji_id TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS channels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER,
                title TEXT,
                link TEXT,
                active INTEGER DEFAULT 1
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS packages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uc INTEGER,
                price INTEGER,
                active INTEGER DEFAULT 1
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                uc INTEGER,
                price INTEGER,
                player_id TEXT,
                status TEXT DEFAULT 'pending',
                created_at INTEGER,
                done_at INTEGER
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                method TEXT,
                amount INTEGER,
                stars INTEGER,
                status TEXT DEFAULT 'pending',
                file_id TEXT,
                file_type TEXT,
                charge_id TEXT,
                created_at INTEGER
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS docs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kind TEXT,
                title TEXT,
                text TEXT,
                media_type TEXT,
                media_id TEXT,
                created_at INTEGER
            )
        """)
        await db.commit()

async def q(sql: str, *params):
    async with aiosqlite.connect(DB_FILE) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(sql, params) as cursor:
            return [dict(row) for row in await cursor.fetchall()]

async def q1(sql: str, *params):
    rows = await q(sql, *params)
    return rows[0] if rows else None

async def x(sql: str, *params):
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute(sql, params) as cursor:
            await db.commit()
            return cursor.lastrowid, cursor.rowcount

def now() -> int:
    return int(time.time())
