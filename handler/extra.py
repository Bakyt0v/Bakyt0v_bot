from aiogram import Dispatcher,types
from config_bot import bot,dp
from lists import bad_words

async def secret_word(message: types.Message):
    await message.reply(f'Yes my master {message.from_user.full_name}')

# async def ban_badwords(message: types.Message):
#     ban_badwords = bad_words
#     txt_words = open('media/bad'),'r'


    # for i in ban_badwords or txt_words:
    #     if i in message.text.lower().replace("",""):
    #         await message.delete()
    #         await bot.send_message(message.chat.id, 'Сам такой!')
    #
    # if message.text.lower() == 'dice':
    #     await bot.send_dice(message.chat.id, emoji='🎲')
    #
    # elif message.text.lower().startswith('pin'):
    #     await bot.pin_chat_message(message.chat.id, message.message_id)
#
# @dp.register_message_handler()
# async def echo(message: types.Message):
#
#     # await bot.send_message(message.chat.id, message.text)
#     await message.answer(message.text)
    # elif message.text.lower() in ban_words:
    #     await  message.reply('This is bad word')
    #     await bot.delete_message(message.chat.id, message.message_id)



def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: word.text.lower().startswith('dorei'))

