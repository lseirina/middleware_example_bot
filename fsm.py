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


@dp.message(CommandStart(), StateFilter(default_state))
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
        callback_data='female'
    )
    m_button = InlineKeyboardButton(
        text='male',
        callback_data='male'
    )
    keyboard: list[list[InlineKeyboardButton]] = [[f_button, m_button]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer(
        text='Choose your gender',
        reply_markup=markup
    )
    await state.set_state(FSMFillForm.fill_gender)


@dp.message(StateFilter(FSMFillForm.fill_age))
async def warning_not_age(message: Message):
    await message.answer('It is not an age.')


@dp.callback_query(StateFilter(FSMFillForm.fill_gender),
                   F.data.in_(['female', 'male']))
async def process_gender_sent(callback: CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback.data)
    await callback.message.delete()
    await callback.message.answer(
        text='Upload your photo'
    )
    await state.set_state(FSMFillForm.upload_photo)


@dp.message(StateFilter(FSMFillForm.fill_gender))
async def warning_not_gender(message: Message):
    await message.answer(
        text='It is not gender'
    )


@dp.message(StateFilter(FSMFillForm.upload_photo),
            F.photo[-1].as_('largest_photo'))
async def process_photo_sent(message: Message,
                             state: FSMContext,
                             largest_photo: PhotoSize):
    await state.update_data(
        photo_unique_id=largest_photo.file_unique_id,
        photo_id=largest_photo.file_id
    )
    s_button = InlineKeyboardButton(
        text='Secondary',
        callback_data='secondary'
    )
    h_button = InlineKeyboardButton(
        text='High',
        callback_data='high'
    )
    keyboard: list[list[InlineKeyboardButton]] = [
        [s_button, h_button]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer(
        text='Thanks',
        reply_markup=markup
    )
    await state.set_state(FSMFillForm.fill_education)


@dp.message(StateFilter(FSMFillForm.upload_photo))
async def warning_not_photo(message: Message):
    await message.answer('I is not a photo')


@dp.callback_query(StateFilter(FSMFillForm.fill_education,
                               F.data.in_(['secondary', 'high'])))
async def process_education_sent(callback: CallbackQuery, state: FSMContext,):
    await state.update_data(education=callback.data)
    user_dict[callback.from_user.id] = await state.get_data()
    await state.clear()
    await callback.message.edit_text(text='Thanks. Data saved.')


@dp.message(StateFilter(FSMFillForm.fill_education))
async def warning_not_education(message: Message):
    await message.answer('It is not aducation')


@dp.message(Command(commands='showdata'), StateFilter(default_state))
async def process_showdata_command(message: Message):
    if message.from_user.id in user_dict:
        await message.answer_photo(
            photo=user_dict[message.from_user.id]['photo_id'],
            caption=f'Name: {user_dict[message.from_user.id]["name"]}\n'
                    f'Age: {user_dict[message.from_user.id]["age"]}\n'
                    f'Gender: {user_dict[message.from_user.id]["gender"]}/n'
                    f'Education: {user_dict[message.from_user.id]["education"]}'
        )
    else:
        await message.enswer(
            text='You did not fill the form.'
        )


@dp.message(StateFilter(default_state))
async def process_other_command(message: Message):
    await message.answer(text='Sorry, I don`t understand')


if __name__ == '__main__':
    dp.run_polling(bot)
