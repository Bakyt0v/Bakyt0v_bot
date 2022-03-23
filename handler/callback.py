from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config_bot import bot


# -----------------------------------------------------------------------------------------
async def solved_task(call: types.CallbackQuery):
    photo4 = open('../media/home_work_solved/solvedscreen.png', 'rb')
    await bot.send_photo(
        call.message.chat.id,
        photo=photo4
    )


async def picture(call: types.CallbackQuery):
    photo4 = open('../media/home_work_solved/picture.jpeg', 'rb')
    await bot.send_photo(
        call.message.chat.id,
        photo=photo4
    )


async def solve_task(call: types.CallbackQuery):
    markup3 = InlineKeyboardMarkup()
    answer4 = ['0.0','1','2.0','4.0','error']
    question4 = 'Result of int2 + float2'
    button5 = InlineKeyboardButton('Next_task', callback_data='button5')
    markup3.add(button5)

    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answer4,
        correct_option_id=3,
        is_anonymous=False,
        type='quiz',
        explanation='only one of these options are true',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        open_period=50,
        reply_markup=markup3,
    )

#========================================================================================================

async def solve1_task(call: types.CallbackQuery):
    answer4 = ['type error','0','1','-1','None']
    question4 = 'print((lambda x: x**2 + 5*x + 4) (-4))'
    button6 = InlineKeyboardButton('Next_task', callback_data='button6')
    markup4 = InlineKeyboardMarkup()
    markup4.add(button6)


    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answer4,
        correct_option_id=1,
        is_anonymous=True,
        type='quiz',
        explanation='only one of these options are true',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        open_period=50,
        reply_markup=markup4,
    )


async def solve2_task(call: types.CallbackQuery):
    answer4 = ['None','KeyError','0']
    question4 = 'test = {} \n'\
                'print(test[0])'

    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answer4,
        correct_option_id=1,
        is_anonymous=True,
        type='quiz',
        explanation='only one of these options are true',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        open_period=50,
    )



async def solve3_task(call: types.CallbackQuery):
    photo3 = open('../media/home_work_solved/photo5278541801109700202.jpg', 'rb')
    answer4 = ['A','B', 'C', 'All options are not correct', 'All options are correct','None']
    question4 = 'Output of this task in picture above,(WARNING, input lists have given for all task option):'

    await bot.send_photo(
        call.message.chat.id,
        photo=photo3)

    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answer4,
        correct_option_id=4,
        is_anonymous=False,
        type='quiz',
        explanation='only one of these options are true',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        open_period=50,
    )

# ========================================================================================================


async def problem2(call: types.CallbackQuery):
    markup1 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Next task',
                                         callback_data='button_call_2')
    markup1.add(button_call_2)

    photo1 = open('../media/listremoveappend.jpg', 'rb')
    answer2 = ['1', '2', '3', '4', '5', '6', '7']
    question2 = 'Output of this task in picture above:'
    await bot.send_photo(
        call.message.chat.id,
        photo=photo1)
    await bot.send_poll(
        call.message.chat.id,
        question=question2,
        options=answer2,
        correct_option_id=2,
        is_anonymous=False,
        type='quiz',
        open_period=15,
        reply_markup=markup1,
        explanation='Little bit harder than previue task',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


async def problem3(call: types.CallbackQuery):
    photo2 = open('../media/homework.jpg', 'rb')
    answer3 = ['0','1', '2', '3', '4', '5']
    question3 = 'Output of this task in picture above:'
    await bot.send_photo(
        call.message.chat.id,
        photo=photo2)
    await bot.send_poll(
        call.message.chat.id,
        question=question3,
        options=answer3,
        correct_option_id=0,
        is_anonymous=False,
        type='quiz',
        open_period=59,
        explanation='You can try solve this task in Pycharm',
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )

# --------------------------------------------------------------------------------------
# async def home_work_2_2(call: types.CallbackQuery):
#     good_photo=open('../media/home_work2/hw2.png','rb')
#     markup_home_work_call = InlineKeyboardMarkup()
#     button22 = InlineKeyboardButton('Легко получилось', callback_data='button22')
#     markup_home_work_call.add(button22)
#     await bot.send_message(
#         call.message.chat.id,
#         reply_markup=home_work_2,
#     )
#     await bot.send_photo(
#         call.message.chat.id,
#         photo = good_photo
#     )


async def home_work_2(call: types.CallbackQuery):
    photo_bad = open('../media/home_work2/bad.jpeg', 'rb')
    markup_bad_1=InlineKeyboardMarkup()
    button_bad_1=InlineKeyboardButton('Если было слишком тяжело попробуйте эту', callback_data='button_bad_1')
    button_bad_2=InlineKeyboardButton('Хотите подсказку', callback_data='button_bad_2')
    button_bad_3=InlineKeyboardButton('Может быть все таки попробуете еще раз', callback_data='button_bad_3')
    markup_bad_1.add(button_bad_1, button_bad_2, button_bad_3)
    await bot.send_photo(
        call.message.chat.id,
        photo=photo_bad)
    await bot.send_message(
        call.message.chat.id,'Почему не смогли?',
        reply_markup=markup_bad_1
    )


async def home_work_2_1(call: types.CallbackQuery):
    photo_bad = open('../media/home_work2/task.jpg', 'rb')
    question_bad=' Сможете решить следующую задачу '
    answer_bad=['Легкая задача', 'Тяжелая задача', 'Средняя задача']

    await bot.send_photo(
        call.message.chat.id,
        photo=photo_bad)

    await bot.send_poll(call.message.chat.id,
                        question=question_bad,
                        options=answer_bad,
                        is_anonymous=False,

                        )


async def home_work_2_2(call: types.CallbackQuery):
    await bot.send_message(
        call.message.chat.id,'Гугл в помощь'
    )

async def home_work_2_3(call: types.CallbackQuery):
    photo_hw2 = open('../media/home_work2/hw2.png', 'rb')
    markup_hw = InlineKeyboardMarkup()
    button_home_work2 = InlineKeyboardButton('Я смог решить домашку', callback_data='button_home_work2')
    button_home_work2_2 = InlineKeyboardButton('Я не смог решить домашку', callback_data='button_home_work_2')
    markup_hw.add(button_home_work2, button_home_work2_2)
    await bot.send_photo(
        call.message.chat.id,
        photo=photo_hw2
    )
    await bot.send_message(call.message.chat.id, 'Домашнее задание 2',
                           reply_markup=markup_hw)
# _-----------------------------------------------------------------------___________________

async def home_work_22_1(call: types.CallbackQuery):
    photo_good = open('../media/home_work2/goodjob.jpeg', 'rb')
    markup_good_1=InlineKeyboardMarkup()
    button_good_1=InlineKeyboardButton('Было легко', callback_data='button_good_1')
    button_good_2=InlineKeyboardButton('Хотите еще задачки ', callback_data='button_good_2')
    button_good_3=InlineKeyboardButton('смогли extra задачу решить', callback_data='button_good_3')
    markup_good_1.add(button_good_1, button_good_2, button_good_3)
    await bot.send_photo(
        call.message.chat.id,
        photo=photo_good)
    await bot.send_message(
        call.message.chat.id,'Вы молодец!',
        reply_markup=markup_good_1
    )
async def home_work_22_2(call: types.CallbackQuery):
    await bot.send_message(
        call.message.chat.id,'Ооо вы есть крут!')


async def home_work_22_3(call: types.CallbackQuery):
    photo_good2 = open('../media/home_work2/task1.jpg', 'rb')
    question_good='Сможете решить следующую задачу '
    answer_good=['Легкая задача', 'Тяжелая задача', 'Средняя задача']

    await bot.send_photo(
        call.message.chat.id,
        photo=photo_good2)

    await bot.send_poll(call.message.chat.id,
        question=question_good,
        options=answer_good,
        is_anonymous=False,

        )

async def home_work_22_4(call: types.CallbackQuery):
    photo_good2 = open('../media/home_work2/home_work2.png', 'rb')
    question_good='It was easy for you'
    answer_good=['Легкая задача', 'Тяжелая задача', 'Средняя задача']

    await bot.send_photo(
        call.message.chat.id,
        photo=photo_good2)

    await bot.send_poll(call.message.chat.id,
        question=question_good,
        options=answer_good,
        is_anonymous=False,
        )


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

async def flex_4(call: types.CallbackQuery):
    markup_flex2 = InlineKeyboardMarkup()
    button_flex2 = InlineKeyboardButton('след задача', callback_data='button_flex2')
    markup_flex2.add(button_flex2)
    question = 'Flex_question'
    answers = ['1','2','3','4','Error','5']
    photo_flex2 = open('../media/lesson/flex_5.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo_flex2)
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        correct_option_id=4,
                        type='quiz',
                        reply_markup=markup_flex2)


async def flex_5(call: types.CallbackQuery):
    markup_flex1 = InlineKeyboardMarkup()
    button_flex1 = InlineKeyboardButton('след задача', callback_data='button_flex1')
    markup_flex1.add(button_flex1)
    question1 = 'Flex_question'
    answers1 = ['1','2','3','4','Error','5']
    photo_flex1 = open('../media/lesson/photo5294518972076637244.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo_flex1)
    await bot.send_poll(call.message.chat.id,
                        question=question1,
                        options=answers1,
                        is_anonymous=False,
                        correct_option_id=4,
                        type='quiz',
                        reply_markup=markup_flex1)
#
# async def home_work_2_2_call(call: types.CallbackQuery):
#     markup_home_work_call = InlineKeyboardMarkup()
#     good1photo = open('../media/home_work2/goodjob.jpeg','rb')
#     # button_01=InlineKeyboardButton('Легко получилось', callback_data='button_01')
#     # markup_home_work_call.add(button_01)
#     await bot.send_message(
#         call.message.chat.id, 'Было сложно?',
#         # reply_markup=home_work_2,
#     )
#     await bot.send_photo(
#         call.message.chat.id,
#         photo=good1photo
#     )

# async def homework_bad_2(call: types.CallbackQuery):
#     good_photo=open('../media/home_work2/hw2.png','rb')
#     markup_home_work_call = InlineKeyboardMarkup()
#     button22 = InlineKeyboardButton('Легко получилось', callback_data='button22')
#     markup_home_work_call.add(button22)
#     await bot.send_message(
#         call.message.chat.id,
#         reply_markup=home_work_2,
#     )
#     await bot.send_photo(
#         call.message.chat.id,
#         photo = good_photo
#     )



def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(solved_task, lambda func: func.data == 'button2')
    dp.register_callback_query_handler(picture, lambda func: func.data == 'button3')
    dp.register_callback_query_handler(solve_task, lambda func: func.data == 'button4')
    dp.register_callback_query_handler(solve1_task, lambda func: func.data == 'button5')
    dp.register_callback_query_handler(solve2_task, lambda func: func.data == 'button6')
    dp.register_callback_query_handler(solve3_task, lambda func: func.data == 'button1')
    dp.register_callback_query_handler(problem2, lambda func: func.data == 'button_call_1')
    dp.register_callback_query_handler(problem3, lambda func: func.data == 'button_call_2')
    dp.register_callback_query_handler(home_work_2, lambda func: func.data == 'button_home_work_2')
    dp.register_callback_query_handler(home_work_2_1, lambda func: func.data == 'button_bad_1')
    dp.register_callback_query_handler(home_work_2_2, lambda func: func.data == 'button_bad_2')
    dp.register_callback_query_handler(home_work_2_3, lambda func: func.data == 'button_bad_3')
    dp.register_callback_query_handler(home_work_22_1, lambda func: func.data == 'button_home_work2')
    dp.register_callback_query_handler(home_work_22_2, lambda func: func.data == 'button_good_1')
    dp.register_callback_query_handler(home_work_22_3, lambda func: func.data == 'button_good_2')
    dp.register_callback_query_handler(home_work_22_4, lambda func: func.data == 'button_good_3')
    dp.register_callback_query_handler(flex_4, lambda func: func.data == 'button_flex')
    dp.register_callback_query_handler(flex_5, lambda func: func.data == 'button_flex2')
    # dp.register_callback_query_handler(home_work_2_2_call, lambda func: func.data == 'button_01')
    # dp.register_callback_query_handler(homework_bad_2, lambda func: func.data == 'button_bad_1')
