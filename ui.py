"""Interfeys: rangli tugmalar, premium emoji, matn/media yuborish."""
import html
import logging
import re
from dataclasses import dataclass

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

import cache
from defaults import BUTTONS, SAMPLE, TEXTS

log = logging.getLogger(__name__)

def T(key: str, **kwargs) -> str:
    """Tarjima / matn olish"""
    text = TEXTS.get(key, key) if isinstance(TEXTS, dict) else key
    try:
        return text.format(**kwargs) if kwargs else text
    except Exception:
        return text

def esc(text: str) -> str:
    """HTML escape"""
    return html.escape(str(text)) if text else ""

def fmt_money(amount: float | int) -> str:
    """Pulni formatlash: 1000 -> 1 000 so'm"""
    try:
        return f"{int(amount):,}".replace(",", " ") + " so'm"
    except Exception:
        return str(amount)

async def send_fresh(message: Message, text: str, reply_markup: InlineKeyboardMarkup | None = None):
    """Eski bot xabarlarini o'chirib, yangisini yuborish (chatni toza saqlash)"""
    try:
        # Avvalgi bot xabarini cache dan o'chirishga urinish
        last_id = cache.get_last_bot_msg_id(message.chat.id) if hasattr(cache, 'get_last_bot_msg_id') else None
        if last_id:
            try:
                await message.bot.delete_message(message.chat.id, last_id)
            except TelegramBadRequest:
                pass
    except Exception:
        pass

    try:
        sent = await message.answer(text, reply_markup=reply_markup, parse_mode="HTML")
        if hasattr(cache, 'set_last_bot_msg_id'):
            cache.set_last_bot_msg_id(message.chat.id, sent.message_id)
        return sent
    except Exception as e:
        log.error(f"send_fresh error: {e}")
        return await message.answer(text, reply_markup=reply_markup)

class Kb:
    """Keyboard builder - rangli tugmalar"""

    @staticmethod
    def _btn(key: str, callback_data: str | None = None) -> InlineKeyboardButton:
        txt = BUTTONS.get(key, key) if isinstance(BUTTONS, dict) else key
        return InlineKeyboardButton(text=txt, callback_data=callback_data or key)

    @staticmethod
    def main_menu() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=BUTTONS.get("catalog", "📦 Katalog"), callback_data="catalog")],
            [InlineKeyboardButton(text=BUTTONS.get("cart", "🛒 Savat"), callback_data="cart"),
             InlineKeyboardButton(text=BUTTONS.get("profile", "👤 Profil"), callback_data="profile")],
        ])

    @staticmethod
    def back(to: str = "main") -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=BUTTONS.get("back", "⬅️ Ortga"), callback_data=f"back:{to}")]
        ])

    @staticmethod
    def yes_no(yes_cb: str = "yes", no_cb: str = "no") -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Ha", callback_data=yes_cb),
                InlineKeyboardButton(text="❌ Yo'q", callback_data=no_cb),
            ]
        ])

# Qo'shimcha interfeys funksiyalari kerak bo'lsa shu yerga qo'shiladi
)