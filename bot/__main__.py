import logging

from asyncio import run
from bot.settings import dp, bot, clientDB
from bot.handlers import setup_router


async def main():
    logging.basicConfig(level=logging.INFO)

    router = setup_router()
    dp.include_router(router)

    logging.info("Starting bot...")
    try:
        await dp.start_polling(bot)
    except Exception:
        print(Exception)
    finally:
        await clientDB.close()
        await bot.close()
        logging.info('Goodbye (^_^)!')


run(main())
