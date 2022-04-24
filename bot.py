from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext, filters
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Filter
from aiogram.dispatcher.filters.state import StatesGroup, State
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from config import token, username
import sqlite3
bot = Bot(token)
dp = Dispatcher(bot, storage = MemoryStorage())

db = sqlite3.connect("new.db")
cursor = db.cursor()

class Ss(StatesGroup):
    


if __name__ == '__main__':
    executor.start_polling(dp)
