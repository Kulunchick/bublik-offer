from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import CommandStart
from aiogram.types import Message

private_router = Router()
private_router.message.filter(F.chat.type == ChatType.PRIVATE)


@private_router.message(CommandStart())
async def start_chat(message: Message):
    await message.answer("ЙДИ НАХУЙ ЗВІДСИ. ВІДЕО, КАРТИНКИ, МЕМИ, МУЗИКУ, ВІРШІ СЮДИ ВІДПРАВЛЯТИ забороннено")
