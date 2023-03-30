from aiogram import Router
from aiogram.types import Message

from bot.settings import settings

offer_route = Router()


@offer_route.message()
async def start_chat(message: Message):
    await message.forward(settings.CHAT_ID)
