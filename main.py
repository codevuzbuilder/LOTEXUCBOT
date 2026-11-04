import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import config
import db
import cache

# Handlers ni yuklash - xato chiqsa bo'sh router bilan ishlaydi
try:
    from handlers import router as handlers_router
except Exception as e:
    logging.warning(f"handlers yuklanmadi: {e}, bo'sh router ishlatiladi")
    from aiogram import Router
    handlers_router = Router()
    @handlers_router.message()
    async def fallback(message):
        await message.answer("Bot ishga tushdi! ✅\n/start ni bosing")

# Middlewares ni yuklash - xato chiqsa o'tkazib yuboradi
try:
    from middlewares import Core
    HAS_MIDDLEWARE = True
except Exception as e:
    logging.warning(f"middlewares yuklanmadi: {e}")
    HAS_MIDDLEWARE = False
    Core = None

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    if not config.TOKEN or "TEST_TOKEN" in config.TOKEN:
        logging.error("BOT_TOKEN topilmadi! GitHub Secrets ga BOT_TOKEN ni qo'shing")
        # 30 soniya kutib chiqib ketadi, workflow qayta yoqadi
        await asyncio.sleep(30)
        return

    # Baza va kesh
    try:
        await db.init()
        await cache.load()
    except Exception as e:
        logging.warning(f"db/cache init xatosi: {e}")

    bot = Bot(token=config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Middleware ulash
    if HAS_MIDDLEWARE and Core:
        try:
            dp.message.middleware(Core())
            dp.callback_query.middleware(Core())
        except Exception as e:
            logging.warning(f"Middleware ulashda xato: {e}")

    # Router ulash
    dp.include_router(handlers_router)

    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("Bot muvaffaqiyatli ishga tushdi! ✅")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
