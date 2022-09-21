from dotenv import dotenv_values
from bot.db import DataB

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


config = dotenv_values("./.env")

bot = Bot(config['TOKEN'], parse_mode='HTML')
dp = Dispatcher(storage=MemoryStorage())
clientDB = DataB()
