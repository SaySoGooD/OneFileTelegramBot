from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import asyncio
from contextlib import suppress
from loguru import logger

from config import TOKEN_BOT
from hanlers import user_router, admin_router

bot = Bot(token=TOKEN_BOT, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main():
    logger.debug("Happy logging with Loguru!")
    dp = Dispatcher()
    dp.include_router(user_router)
    dp.include_router(admin_router)
    logger.info(f"Started on - {(await bot.get_me()).username}")
    await dp.start_polling(bot)


if __name__ == '__main__':
    with suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(main())
