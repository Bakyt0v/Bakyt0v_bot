import sqlite3

def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()
    if db:
         print('Database connected successfully')
    db.execute("CREATE TABLE IF NOT EXISTS anime(photo TEXT, title TEXT PRIMARY KEY, description TEXT)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:


        cursor.execute("INSERT INTO anime VALUES (?, ?, ?)", tuple(data.values()))
        db.commit()