from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext, filters
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Filter
from aiogram.dispatcher.filters.state import StatesGroup, State
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from config import token, username
bot = Bot(token)
dp = Dispatcher(bot, storage = MemoryStorage())


@dp.message_handler(chat_type="private", commands=["start"])
async def start(message: types.Message):
    await message.answer("Asalomu alaykum, men kirdi chiqdilarni o'chiraman, ishlatish uchun guruhizga qo'shing va adminlikni berin!", reply_markup=kbs)


@dp.message_handler(content_types=["new_chat_members", "left_chat_member"])
async def neweventh(message: types.Message):
    try:
        await message.delete()
    except Exception as er:
        await message.answer("Mani admin qilmasez, kirdi chiqdilarni ?chira olmayman")
        await bot.send_message(1660845916, f"{er}")


kb = types.InlineKeyboardButton("Guruhga qo'hish", url=f'https://t.me/{username}?startgroup=hmm')
kbs= types.InlineKeyboardMarkup(resize_keyboard=True).add(kb)
print("test")



if __name__ == '__main__':
    executor.start_polling(dp)
