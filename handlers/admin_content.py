from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import ADMIN_IDS
from .admin_core import is_admin, admin_main_keyboard

router = Router()

class AddProduct(StatesGroup):
    name = State()
    price = State()
    photo = State()

@router.message(F.text == "🛍 Mahsulot qo'shish")
async def add_product_start(message: Message, state: FSMContext):
    if not is_admin(message.from_user.id): return
    await state.set_state(AddProduct.name)
    await message.answer("Mahsulot nomini yozing:")

@router.message(AddProduct.name)
async def add_product_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddProduct.price)
    await message.answer("Narxini yozing (masalan: 150000):")

@router.message(AddProduct.price)
async def add_product_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(AddProduct.photo)
    await message.answer("Rasmini yuboring:")

@router.message(AddProduct.photo, F.photo)
async def add_product_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    # Bu yerda bazaga saqlash kodini qo'shasan
    await message.answer(
        f"✅ Saqlandi!\n\nNomi: {data['name']}\nNarxi: {data['price']}",
        reply_markup=admin_main_keyboard()
    )
    await state.clear()

@router.message(F.text == "📝 Kontent")
async def content_menu(message: Message):
    if not is_admin(message.from_user.id): return
    await message.answer("📝 Kontent bo'limi:\n\n- Mahsulotlar ro'yxati\n- Kategoriyalar\n- Xabar yuborish", reply_markup=admin_main_keyboard())

@router.message(F.text == "📦 Buyurtmalar")
async def orders_menu(message: Message):
    if not is_admin(message.from_user.id): return
    await message.answer("Hozircha buyurtmalar yo'q.", reply_markup=admin_main_keyboard())