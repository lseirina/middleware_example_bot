from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
dp = Dispatcher()
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='It is demonstrated bot.'
    )


@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text='/strike - strike style\n'
             '/link - outside link\n'
             '/tglink - inside link\n'
             '/pre - preformatted text\n'
             '/code - monoplaced text\n'
             '/precode - preformated code\n'
             '/precodediff\n'
             '/boldi\n'
             '/boldiu\n'
    )


@dp.message(Command(commands='strike'))
async def process_strike_command(message: Message):
    await message.answer(
        text='<s>It is strike style</s>'
    )


@dp.message(Command(commands='link'))
async def process_link_command(message: Message):
    await message.answer(
        text='It is outside link\n'
             '<a href="https://stepik.org/120924">Outside link</a>'
    )


@dp.message(Command(commands='tglink'))
async def process_tglink_command(message: Message):
    await message.answer(
        text='<a href="tg://user?id=173901673">Inside link</a>'
    )


@dp.message(Command(commands='code'))
async def process_code_command(message: Message):
    await message.answer(
        text='<code>It is monospaced font</code>'
    )


@dp.message(Command(commands='pre'))
async def process_pre_command(message: Message):
    await message.answer(
        text='<pre>Pre-formatted text</pre>'
    )


@dp.message(Command(commands='precode'))
async def process_precode_command(message: Message):
    await message.answer(
        text='<pre><code>Preformatted block of Python </code></pre>'
    )


@dp.message(Command(commands='precodediff'))
async def process_precodediff_command(message: Message):
    await message.answer(
        text='С помощью этого текста можно лучше понять '
             'разницу между тегами &lt;code&gt; и '
             '&lt;pre&gt; - текст внутри '
             'тегов &lt;code&gt; <code>не выделяется в '
             'отдельный блок</code>, а становится '
             'частью строки, внутрь которой помещен, в то время как '
             'тег &lt;pre&gt; выделяет текст <pre>в отдельный '
             'блок,</pre> разрывая '
             'строку, внутрь которой помещен'
    )


@dp.message(Command(commands='boldi'))
async def process_boldi_command(message: Message):
    await message.answer(
        text='<i><b>It is bold and italkit font</b></i>'
    )


@dp.message(Command(commands='boldiu'))
async def procces_boldiu_command(message: Message):
    await message.answer(
        text='<b><i><u>It is bold, italcit and underline</u></i></b>'
    )

@dp.message()
async def send_echo(message: Message):
    await message.answer(
        text='I don`t understand'
    )


if __name__ == '__main__':
    dp.run_polling(bot)