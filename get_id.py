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

# Voice_id1: AwACAgIAAxkBAAIDsWZB6z46xUPkgG3GFfkaP0qJLz78AAIkRwACFjMQSu52xRsxmgPWNQQ
# Voice_id2: AwACAgIAAxkBAAIDt2ZCXEKK8wkGbQZczdmBR_lX8a4cAAIfTQACFjMQSkcszBL3Oq7_NQQ
# Photo_id1: AgACAgIAAxkBAAIDtWZB7FXUYckGBwAB_0g9qr9inHu30wACtOAxGxYzEEos_soyt6njqwEAAwIAA3kAAzUE
# Photo_id2: AgACAgIAAxkBAAIDuGZCXHWJbPoN1-H_WhmVzuYAAVc52wACduMxGxYzEEp7RuixYm8kkAEAAwIAA3kAAzUE
# Video_id1: BAACAgIAAxkBAAIDtmZB7JUHdCm_JPWiaNIYlpBVnVPZAAJQRwACFjMQSodfDkTNBsIsNQQ
# Video_id2: BAACAgIAAxkBAAIDuWZCXLb0M654s8ldRPRxH502ps2BAAIjTQACFjMQSl6z2xiE_qpWNQQ