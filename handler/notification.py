import asyncio
import aioschedule
from aiogram import Dispatcher, types
from config_bot import bot
from lists import bad_words

async def ban_badwords(message: types.Message):
    ban_badwords = bad_words
    # txt_words = open('media/bad'),'r':
    global chat_id
    chat_id = message.chat.id

    for i in ban_badwords:
        if i in message.text.lower().replace("", ""):
            await message.delete()
            await bot.send_message(message.chat.id, 'Сам такой!')

    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji='🎲')

    elif message.text.lower() == 'wake me up':
        await message.reply('OK!')

    elif message.text.lower() == 'deadline home work on today':
        await message.reply('OK i will remind you!')

    elif message.text.lower().startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

async def wake_up():
    await bot.send_message(chat_id=chat_id, text='Wake up please Master!')

async def deadline():
    await bot.send_message(chat_id=chat_id, text='Deadline hurry up master!')

async def scheduler():
    aioschedule.every().day.at('22:10').do(wake_up)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def deadline_hw():
    aioschedule.every(1).wednesday.at('00:00').do(deadline)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(ban_badwords, content_types=['text'])
    # dp.register_message_handler(confirm_notifications, lambda word: word.text.lower().startswith('wake me up'))
    # dp.register_message_handler(conefirm_notifications, content_types=['text'])