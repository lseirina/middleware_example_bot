import logging

from aiogram import Router, F
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)
from aiogram.filters import CommandStart
from filters.filters import MyTrueFilter, MyFalseFilter
from lexicon.lexicon import LEXICON_RU


logger = logging.getLogger(__name__)

user_router = Router()


@user_router.callback_query(CommandStart, MyTrueFilter())
async def process_start_command(message: Message):
    logger.debug('Вошли в хэндлер, обрабатывающий команду /start')
    button = InlineKeyboardButton(
        text='Button',
        callback_data='pressed_button'
    )
    markup = InlineKeyboardMarkup(keyboard=[[button]])
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=markup,
    )
    logger.debug('Вышли в хэндлер, обрабатывающий команду /start')


@user_router.callback_query(MyTrueFilter())
async def process_button_click(callback: CallbackQuery):
    logger.debug('Вошли в хэндлер, обрабатывающий нажатие на инлайн-кнопку')
    await callback.answer(LEXICON_RU['pressed_button'])
    logger.debug('Вышли в хэндлер, обрабатывающий нажатие на инлайн-кнопку')


@user_router.message(F.text, MyFalseFilter())
async def process_text(message: Message):
    logger.debug('Вошли в хэндлер, обрабатывающий текст')
    logger.debug('Выходим из хэндлера, обрабатывающего текст')
