from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='This is a demonstrating bot\n'
             'It will shoe text in different formats.'
    )


@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text='I am demonstrating bot\n'
             'Send a command from the list:\n\n'
             '/bold - for bold font,\n'
             '/italic - for italic font,\n'
             '/underline - for underline font,\n'
             '/spoiler - for spoiler.'
    )


@dp.message(Command(commands='bold'))
async def process_bold_command(message: Message):
    await message.answer(
        text='<b>It is a bold font.</b>'
    )


@dp.message(Command(commands='italic'))
async def procces_italic_command(message: Message):
    await message.answer(
        text='<i>It is italic font.</i>'
    )


@dp.message(Command(commands='underline'))
async def process_underline_command(message: Message):
    await message.answer(
        text='<u>It is underline font.</u>'
    )


@dp.message(Command(commands=['spoiler']))
async def procces_spoiler_command(message: Message):
    await message.answer(
        text='<tg-spoiler>It is spoiler.</tg-spoiler>'
    )


@dp.message()
async def send_echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)


if __name__ == "__main__":
    dp.run_polling(bot)