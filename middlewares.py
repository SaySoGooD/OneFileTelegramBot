from datetime import datetime
from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from loguru import logger

from config import ADMINS


class LoggingBot(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        logger.info(f"user={event.from_user.id} | event={type(event).__name__} | {f'data={event.text if event.text else event.data}'}")
        await handler(event, data)


class CheckAdmin(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        if event.from_user.id not in ADMINS:
            return
        await handler(event, data)