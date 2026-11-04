import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN, ADMIN_IDS
from handlers import admin_core, admin_content, admin_design

logging.basicConfig(level=logging.INFO)

async def main():
    if not BOT_TOKEN or "BU_YERGA" in BOT_TOKEN:
        print("❌ XATO: BOT_TOKEN topilmadi!")
        return

    print(f"LOTEX SHOP ishga tushdi... 24/7")
    print(f"Admin ID: {ADMIN_IDS}")
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Barcha handlerlar handlers papkasidan olinadi
    dp.include_router(admin_core.router)
    dp.include_router(admin_content.router)
    dp.include_router(admin_design.router)

    print("✅ Bot polling boshlandi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())