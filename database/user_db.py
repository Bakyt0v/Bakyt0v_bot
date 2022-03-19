import sqlite3
from config_bot import bot



def sql_create():
    global db, cursor
    db = sqlite3.connect('home_work_db')
    cursor = db.cursor()
    if db:
         print('Homework database connected successfully')
    db.execute("CREATE TABLE IF NOT EXISTS users_db(id TEXT PRIMARY KEY , username TEXT, firstname TEXT, lastname TEXT)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO users_db VALUES (?, ?, ?, ?)", tuple(data.values()))
        db.commit()

async def sql_command_select(message):
    for result in cursor.execute('SELECT * FROM users_db').fetchall():
        await bot.send_message(message.from_user.id, result[0],
                               caption=f'ID: {result[0]}\n'
                                       f'username: {result[1]}\n'
                                       f'firstname: {result[2]}\n'
                                       f'lastname: {result[3]}\n')

async def sql_command_delete(data):
    cursor.execute('DELETE FROM users_db WHERE id == ?', (data,))
    db.commit()