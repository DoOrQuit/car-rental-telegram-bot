from config import TOKEN
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import types
from aiogram.utils import executor

bot = aiogram.Bot(token='TOKEN')
dp = Dispatcher(bot)


executor.start_polling(dp, skip_updates=True)










