import logging
from typing import Any, Callable, Awaitable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


logger = logging.getLogger(__name__)


class FirstOuterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        logger.debug(
            'Entered middleware %s, type event %s',
            __class__.__name__,
            event.__class__.__name__
        )
        result = await handler(event, data)

        logger.debug(
            'Left middleware %s',
            __class__.__name__
        )
        return result


class SecondOuterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ):
        logger.debug(
            'Entered middleware %s, type event %s',
            __class__.__name__,
            event.__class__.__name__
        )
        result = await handler(event, data)
        logger.debug(
            'Left middleware %s',
            __class__.__name__
        )
        return result


class ThirdOuterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ):
        logger.debug(
            'Entered middleware %s, type event %s',
            __class__.__name__,
            event.__class__.__name__
        )
        result = await handler(event, data)
        logger.debug(
            'Left middleware %s',
            __class__.__name__
        )
        return result
