from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import ADMIN_IDS

router = Router()

def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS

def admin_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="🛍 Mahsulot qo'shish")
    builder.button(text="📦 Buyurtmalar")
    builder.button(text="🎨 Dizayn")
    builder.button(text="📝 Kontent")
    builder.button(text="📊 Statistika")
    builder.button(text="⬅️ Chiqish")
    builder.adjust(2, 2, 2)
    return builder.as_markup(resize_keyboard=True)

@router.message(Command("admin"))
@router.message(Command("start"))
async def admin_start(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer(f"Assalomu alaykum! {message.from_user.first_name} 👋\nLOTEX SHOP ga xush kelibsiz!\n\nKatalogni ko'rish uchun /catalog bosing.")
        return
    
    await message.answer(
        f"🔥 <b>LOTEX SHOP Admin Panel</b>\n\nSalom Admin! ✅\nID: {message.from_user.id}",
        parse_mode="HTML",
        reply_markup=admin_main_keyboard()
    )

@router.message(F.text == "⬅️ Chiqish")
async def admin_exit(message: Message):
    if not is_admin(message.from_user.id): return
    await message.answer("Admin paneldan chiqdingiz.", reply_markup=None)