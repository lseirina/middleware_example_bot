import random

from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    CallbackQuery,
)
from aiogram.filters import Command


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

jokes: dict[int, str] = {
    1: 'у меня на балконе сосулька растет метровая, прямо над машиной, '
       'которая ссигналит каждую ночь. Я эту сосульку из распылителя подкармливаю.',
    2: 'xx: Мне сейчас спам пришел "Я живу в доме напротив, вот моя ссылка *адрес ссылки*.'
       ' Давай познакомимся". Я ответил, что живу напротив морга и меня пугают такие знакомства',
    3: 'xxx: В командировке на съемной квартире нужна была марля, чтобы погладить футболку.'
       'Начал шариться по всем ящикам. Марлю не нашел, зато нашел ключ в шкафу между простынями.'
       'Вспомнил, что один ящик в этом шкафу был заперт. Попробовал открыть его найденным ключом. Открыл. Внутри нашел марлю. Не зря в квесты играл..'
}


def random_joke():
    return random.randint(1, len(jokes))


@dp.message(Command(commands=['start', 'joke']))
async def process_start_command(message: Message):
    keyboard: list = [
        [InlineKeyboardButton(text='I want more', callback_data='more')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer(
        text=jokes[random_joke()],
        reply_markup=markup
    )


@dp.callback_query(F.data == 'more')
async def process_more_press(callback=CallbackQuery):
    keyboard: list[list[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text='I want more', callback_data='more')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await callback.message.edit_text(
        text=jokes[random_joke()],
        reply_markup=markup
    )


@dp.message()
async def other_message(message: Message):
    await message.answer(
        text='I don`t understand'
    )

if __name__ == '__main__':
    dp.run_polling(bot)
