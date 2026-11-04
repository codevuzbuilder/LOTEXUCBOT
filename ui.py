"""Interfeys: rangli tugmalar, premium emoji, matn/media yuborish."""
import html
import logging
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import cache
from defaults import BUTTONS, TEXTS

log = logging.getLogger(__name__)

def T(key, **kwargs):
    text = TEXTS.get(key, key) if isinstance(TEXTS, dict) else key
    try:
        return text.format(**kwargs) if kwargs else text
    except:
        return text

def esc(text):
    return html.escape(str(text)) if text else ""

def fmt_money(amount):
    try:
        return str(int(amount)) + " so'm"
    except:
        return str(amount)

async def send_fresh(message, text, reply_markup=None):
    try:
        sent = await message.answer(text, reply_markup=reply_markup, parse_mode="HTML")
        return sent
    except Exception as e:
        log.error(f"send_fresh error: {e}")
        return await message.answer(text, reply_markup=reply_markup)

class Kb:
    @staticmethod
    def main_menu():
        btn_catalog = BUTTONS.get("catalog", "Katalog") if isinstance(BUTTONS, dict) else "Katalog"
        btn_cart = BUTTONS.get("cart", "Savat") if isinstance(BUTTONS, dict) else "Savat"
        btn_profile = BUTTONS.get("profile", "Profil") if isinstance(BUTTONS, dict) else "Profil"
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=btn_catalog, callback_data="catalog")],
            [InlineKeyboardButton(text=btn_cart, callback_data="cart"), InlineKeyboardButton(text=btn_profile, callback_data="profile")]
        ])

    @staticmethod
    def back(to="main"):
        btn_back = BUTTONS.get("back", "Ortga") if isinstance(BUTTONS, dict) else "Ortga"
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=btn_back, callback_data=f"back:{to}")]
        ])

    @staticmethod
    def yes_no(yes_cb="yes", no_cb="no"):
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Ha", callback_data=yes_cb), InlineKeyboardButton(text="Yoq", callback_data=no_cb)]
        ])