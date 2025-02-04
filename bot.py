import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
import os

TOKEN = os.getenv("TOKEN")  # Теперь токен будет браться из переменной окружения
WEB_APP_URL = "https://dream-bar.onrender.com"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Play", web_app=WebAppInfo(url=WEB_APP_URL))]]
    )
    await message.answer("Hi! Welcome to the Dream Bar! You're the bartender now. Which one? Choose for yourself. Build your dream bar.", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())









