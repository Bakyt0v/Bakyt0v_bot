from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_add = KeyboardButton("/add")
button_delete = KeyboardButton("/delete")
button_show = KeyboardButton('/user_db')
button_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_add, button_delete, button_show)

