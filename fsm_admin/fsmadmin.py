from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config_bot import bot
from database import bot_db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from database import psql_db
from pasrer import movies



class FSMADMIN(StatesGroup):
    photo = State()
    title = State()
    description = State()


async def is_admin_func(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Admin, What do u need")

async def cancel_hundler(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        current_state=await state.get_state()
        await state.finish()
        await message.reply('Canceled normally')


async def fsm_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await FSMADMIN.photo.set()
        await message.reply("Admin, Send me photo please")


async def load_photo(message: types.Message,
                     state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["photo"] = message.photo[0].file_id
        await FSMADMIN.next()
        await message.reply("Send me title of photo")


async def load_title(message: types.Message,
                     state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data['title'] = message.text
    await FSMADMIN.next()
    await message.reply("Admin, send me description, please")


async def load_description(message: types.Message,
                           state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["description"] = message.text
        await bot_db.sql_command_insert(state)
        await state.finish()
        # async with state.proxy() as data:
        #     await message.reply(str(data))
        # await state.finish()

# =========================HOME==WORK==8===============================================
async def registration(message: types.Message):
    id = message.from_user.id
    username = message.from_user.username
    fullname = message.from_user.full_name
    psql_db.cursor.execute(f"SELECT id from users WHERE id = {id}")
    result = psql_db.cursor.fetchone()

    if not result:
        psql_db.cursor.execute(f"INSERT INTO users (id, user_name, full_name) VALUES  (%s, %s, %s)",
                               (id, username, fullname))
        psql_db.database.commit()
        await message.reply("Registration failed🤣")


async def get_all_users(message: types.Message):
    all_users = psql_db.cursor.execute(f"SELECT * FROM users")
    result = psql_db.cursor.fetchall()
    for row in result:
        # await message.reply(result)
        await message.reply(f"ID: {row[0]}\n"
                            f"UserName👮 {row[1]}\n"
                            f"FullNAme🤠 {row[2]}")

# =================================================================================


async def films(message: types.Message):
    image = movies.URL
    psql_db.cursor.execute(f"SELECT image from movies WHERE image = {image}")
    result = psql_db.cursor.fetchone()

    if not result:
        psql_db.cursor.execute(f"INSERT INTO movies (image) VALUES  (%s)",
                               (image))
        psql_db.database.commit()
        await message.reply("Registration failed🤣")


# async def get_all_users(message: types.Message):
#     all_users = psql_db.cursor.execute(f"SELECT * FROM users")
#     result = psql_db.cursor.fetchall()
#     for row in result:
#         # await message.reply(result)
#         await message.reply(f"image: {row[0]}\n"
#                             f"title👮 {row[1]}\n"
#                             )

# =================================================================================
def register_handler_fsmadmin(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['download'], state=None)
    dp.register_message_handler(cancel_hundler, state='*', commands='cancel')
    dp.register_message_handler(cancel_hundler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMADMIN.photo)
    dp.register_message_handler(load_title, state=FSMADMIN.title)
    dp.register_message_handler(load_description, state=FSMADMIN.description)
    dp.register_message_handler(is_admin_func, commands=['admin'], is_chat_admin=True)
    dp.register_message_handler(registration, commands=["register"])
    dp.register_message_handler(get_all_users, commands=["get"])
    dp.register_message_handler(films, commands=["movie"])