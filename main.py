import asyncio
import logging
import os
import sys
from aiogram import Dispatcher

from aiogram import Bot
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from src.database import startup_db, shutdown_db
from src.handler.comand import comand_router
from src.init_app import dp


load_dotenv()


dp = Dispatcher()


async def start() -> None:
    bot = Bot(os.environ.get('TOKEN'), parse_mode=ParseMode.HTML)

    dp.startup.register(startup_db)
    dp.shutdown.register(shutdown_db)
    dp.include_router(comand_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())
