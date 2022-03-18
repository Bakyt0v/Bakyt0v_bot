from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.dispatcher.filters import Text

class User_add(StatesGroup):
    id = State()
    username = State()
    firstname = State()
    lastname = State()


async def is_admin_func(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(message.from_user.id, "I can add to data some information just give me a command as /add")


async def fsm_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await User_add.id.set()
        await message.reply("enter start")


async def load_id(message: types.Message,
                     state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["id"] = message.from_user.id
        await User_add.next()
        await message.reply("Send me a id")

async def load_username(message: types.Message,
                     state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data['username'] = message.from_user.username
    await User_add.next()
    await message.reply("Admin, send me username, please")


async def load_firstname(message: types.Message,
                     state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data['fisrtname'] = message.from_user.first_name
    await User_add.next()
    await message.reply("Admin, send me firstname, please")


async def load_lastname(message: types.Message,
                           state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["lastname"] = message.from_user.last_name
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

def register_handler_fsm_admin_user(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['add'], state=None)
    dp.register_message_handler(load_id, state=User_add.id)
    dp.register_message_handler(load_username, state=User_add.username)
    dp.register_message_handler(load_firstname, state=User_add.firstname)
    dp.register_message_handler(load_lastname, state=User_add.lastname)
    dp.register_message_handler(is_admin_func, commands=['user_register'], is_chat_admin=True)