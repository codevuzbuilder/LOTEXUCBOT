import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import admin_core, admin_content, admin_design

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Routerlarni handlers papkasidan ulash
    dp.include_router(admin_core.router)
    dp.include_router(admin_content.router)
    dp.include_router(admin_design.router)

    print("Bot ishga tushdi! ✅")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())