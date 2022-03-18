from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_button2= KeyboardButton('/start')
button_help = KeyboardButton("/help")
button_location = KeyboardButton('Share location', request_location=True)
button_info = KeyboardButton('Share_info', request_contact=True)


keyboard_stat = ReplyKeyboardMarkup(resize_keyboard=True, row_width= 4)


keyboard_stat.row(button_help, button_button2, button_info, button_location)
