from aiogram import Bot
from fastapi import FastAPI

from app.config import TOKEN

token = TOKEN
bot = Bot(token)
app = FastAPI()

async def send_message(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)