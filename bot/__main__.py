from aiogram import Bot, Dispatcher
import asyncio

from aiogram.enums import ParseMode

from bot.routes.offer import offer_route
from bot.routes.private import private_router
from bot.settings import settings


async def main():
    bot = Bot(token=settings.TOKEN.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(private_router)
    dp.include_router(offer_route)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
