from aiogram import executor
from config_bot import dp
from handler import cilent, callback, extra
from fsm_admin import fsmadmin, fsm_admin_users


# async  def on_startup(_):
#     bot_db.sql_create()



fsm_admin_users.register_handler_fsm_admin_user(dp)
fsmadmin.register_handler_fsmadmin(dp)
cilent.refister_handlers_cilent(dp)
callback.register_handlers_callback(dp)
extra.register_handler_extra(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)