import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import config
import db
import cache
from handlers import router as handlers_router
from middlewares import Core

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Ma'lumotlar bazasi va keshni yuklash
    await db.init()
    await cache.load()

    bot = Bot(token=config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Middleware'ni ulash
    dp.message.middleware(Core())
    dp.callback_query.middleware(Core())

    # Barcha handlerlarni ulash
    dp.include_router(handlers_router)

    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("Bot muvaffaqiyatli ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
