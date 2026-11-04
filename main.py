import logging
import time
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
import cache
import db
from services import get_user, is_admin
# ui dan faqat kerakli narsalarni olamiz, xato chiqmasligi uchun
try:
    from ui import Kb
except:
    Kb = None

log = logging.getLogger(__name__)
_ok = {}

async def missing_channels(bot, uid, force=False):
    return []

async def show_sub(ev, missing):
    if ev:
        try:
            await ev.answer("Kanallarga obuna bo'ling", show_alert=True)
        except:
            pass

async def ensure_user(u, ref=None):
    if ref and (ref == u.id):
        ref = None
    return {"id": u.id, "banned": False}

class Core(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user = getattr(event, 'from_user', None)
        if user is None or user.is_bot:
            return await handler(event, data)
        data["db_user"] = {"id": user.id, "banned": False}
        return await handler(event, data)