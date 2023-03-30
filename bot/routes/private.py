from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

private_router = Router()


@private_router.message(CommandStart())
async def start_chat(message: Message):
    await message.answer("ЙДИ НАХУЙ ЗВІДСИ. ВІДЕО, КАРТИНКИ, МЕМИ, МУЗИКУ, ВІРШІ СЮДИ ВІДПРАВЛЯТИ забороннено")
