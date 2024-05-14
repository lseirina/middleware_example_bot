from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaVideo,
    Message,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'photo_id1': 'AgACAgIAAxkBAAIDtWZB7FXUYckGBwAB_0g9qr9inHu30wACtOAxGxYzEEos_soyt6njqwEAAwIAA3kAAzUE',
    'photo_id2': 'AgACAgIAAxkBAAIDuGZCXHWJbPoN1-H_WhmVzuYAAVc52wACduMxGxYzEEp7RuixYm8kkAEAAwIAA3kAAzUE',
    'voice_id1': 'AwACAgIAAxkBAAIDsWZB6z46xUPkgG3GFfkaP0qJLz78AAIkRwACFjMQSu52xRsxmgPWNQQ',
    'voice_id2': 'AwACAgIAAxkBAAIDt2ZCXEKK8wkGbQZczdmBR_lX8a4cAAIfTQACFjMQSkcszBL3Oq7_NQQ',
    'video_id1': 'BAACAgIAAxkBAAIDtmZB7JUHdCm_JPWiaNIYlpBVnVPZAAJQRwACFjMQSodfDkTNBsIsNQQ',
    'video_id2': 'BAACAgIAAxkBAAIDuWZCXLb0M654s8ldRPRxH502ps2BAAIjTQACFjMQSl6z2xiE_qpWNQQ',
}


def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))
    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'video')
    await message.answer_video(
        video=LEXICON['video_id1'],
        caption='It is the 1-st video',
        reply_markup=markup
    )


@dp.callback_query(F.data == 'video')
async def process_video_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'video')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaVideo(
                media=LEXICON['video_id2'],
                caption='It is the 2-st video'),
            reply_markup=markup
        )
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaVideo(
                media=LEXICON['video_id1'],
                caption='It is the 1-st video'),
            reply_markup=markup
        )


@dp.message()
async def process_other_command(message: Message):
    await message.answer('I don`t understand')


if __name__ == '__main__':
    dp.run_polling(bot)