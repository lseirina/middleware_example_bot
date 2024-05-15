from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    PhotoSize,
)

BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=storage)

user_dict: dict[int, dict[str, str | int | bool]] = {}


class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_age = State()
    fill_gender = State()
    upload_photo = State()
    fill_education = State()
    fill_wish_news = State()


@dp.message(CommandStart, StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text="To fullfill the form send /fillform"
    )


@dp.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(
        text='You did not fullfill the form.\n'
             'Nothig to delete.'
    )


@dp.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text='Everything is deleted.'
    )
    state.clear()


@dp.message(Command(commands='fillform'), StateFilter(default_state))
async def process_fillform_command(message: Message, state: FSMContext):
    await message.answer('Please, write your name')
    await state.set_state(FSMFillForm.fill_name)


@dp.message(StateFilter(FSMFillForm.fill_name), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('And now write your age')
    await state.set_state(FSMFillForm.fill_age)


@dp.message(StateFilter(FSMFillForm.fill_name))
async def process_warn_name(message: Message):
    await message.answer(
        text='This is does not look like a name.'
    )


@dp.message(StateFilter(FSMFillForm.fill_age),
            lambda x: x.text.isdigit() and 4 <= int(x.text) <= 120)
async def process_age_send(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    f_button = InlineKeyboardButton(
        text='female',
        calback_data='female'
    )
    m_button = InlineKeyboardButton(
        text='man',
        callback_data='man'
    )
    keyboard: list[list[InlineKeyboardButton]] = [[f_button, m_button]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer(
        text='Choose your gender',
        markup=markup
    )
    await state.set_state(FSMFillForm.fill_gender)
