from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import ADMIN_IDS
from .admin_core import is_admin, admin_main_keyboard

router = Router()

def design_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🖼 Logo almashtirish", callback_data="change_logo")
    builder.button(text="🎨 Ranglar", callback_data="change_colors")
    builder.button(text="💬 Start matni", callback_data="change_start_text")
    builder.adjust(1)
    return builder.as_markup()

@router.message(F.text == "🎨 Dizayn")
async def design_menu(message: Message):
    if not is_admin(message.from_user.id): return
    await message.answer(
        "🎨 <b>Dizayn boshqaruvi</b>\n\nQaysi bo'limni o'zgartirmoqchisiz?",
        parse_mode="HTML",
        reply_markup=design_inline_keyboard()
    )

@router.callback_query(F.data == "change_logo")
async def change_logo_cb(callback: CallbackQuery):
    if not is_admin(callback.from_user.id): return
    await callback.message.answer("Yangi logo rasmini yuboring.")
    await callback.answer()

@router.callback_query(F.data == "change_start_text")
async def change_start_text_cb(callback: CallbackQuery):
    if not is_admin(callback.from_user.id): return
    await callback.message.answer("Yangi /start matnini yozing:")
    await callback.answer()

@router.message(F.text == "📊 Statistika")
async def stats_menu(message: Message):
    if not is_admin(message.from_user.id): return
    await message.answer("📊 Statistika:\n\n👥 Foydalanuvchilar: 0\n📦 Mahsulotlar: 0", reply_markup=admin_main_keyboard())