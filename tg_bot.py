import asyncio
from aiogram import executor
from config_bot import dp, bot,URL
from handler import callback, cilent, extra, notification, inline
from fsm_admin import fsmadmin, fsm_admin_users
from database import bot_db, user_db
from handler.notification import scheduler, deadline_hw
from decouple import config


async def on_startup(_):
    await bot.set_webhook(URL)
    bot_db.sql_create()
    user_db.sql_create()
    asyncio.create_task(scheduler())
    asyncio.create_task(deadline_hw())

    print('Bot is online')

async def on_shutdown(dp):
    await  bot.delete_webhook()


fsm_admin_users.register_handler_fsm_admin_user(dp)
fsmadmin.register_handler_fsmadmin(dp)
cilent.refister_handlers_cilent(dp)
callback.register_handlers_callback(dp)
inline.register_handlers_inline(dp)
extra.register_handler_extra(dp)
notification.register_handler_notification(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=int(config("PORT", default=5000))
             )