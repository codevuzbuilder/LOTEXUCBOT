from aiogram import Router

router = Router()

@router.message()
async def start_handler(message):
    await message.answer("Bot ishga tushdi! ✅\n\n/start ni bosing\n\nBu vaqtinchalik handler. Asosiy handlerlaringizni shu yerga qo'shing.")

@router.message(lambda m: m.text and m.text.startswith("/start"))
async def start_cmd(message):
    await message.answer("Assalomu alaykum! Bot 24/7 ishlayapti 🚀")
