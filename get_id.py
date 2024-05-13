from aiogram import Bot, Dispatcher
from aiogram.types import Message


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def process_any_command(message: Message):
    if message.voice:
        print(f'Voice: {message.voice.file_id}')
    if message.photo:
        print(f'Photo: {message.photo[-1].file_id}')
    if message.video:
        print(f'Video: {message.video.file_id}')


if __name__ == '__main__':
    dp.run_polling(bot)

Voice: AwACAgIAAxkBAAIDsWZB6z46xUPkgG3GFfkaP0qJLz78AAIkRwACFjMQSu52xRsxmgPWNQQ
Photo: AgACAgIAAxkBAAIDtWZB7FXUYckGBwAB_0g9qr9inHu30wACtOAxGxYzEEos_soyt6njqwEAAwIAA3kAAzUE
Video: BAACAgIAAxkBAAIDtmZB7JUHdCm_JPWiaNIYlpBVnVPZAAJQRwACFjMQSodfDkTNBsIsNQQ