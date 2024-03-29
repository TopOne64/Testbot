import sqlite3 as sq

async def db_start():
    global db, cur
    db = sq.connect('tg.db')
    cur = db.cursor()
    await cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                      "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                      "tg_id INTEGER, "
                      "cart_id TEXT)")
    await cur.execute("CREATE TABLE IF NOT EXISTS items("
                      "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                      "name TEXT,"
                      "desc TEXT, "
                      "price TEXT, "
                      "photo TEXT, "
                      "brand TEXT)")
    await db.commit()


async def cmd_start_db(user_id):
    user = await cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        await cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        await db.commit()


async def add_item(state):
    async with state.proxy() as data:
        await cur.execute("INSERT INTO items (name, desc, price, photo, brand) VALUES (?, ?, ?, ?, ?)",
                          (data['name'], data['desc'], data['price'], data['photo'], data['type']))
        await db.commit()
