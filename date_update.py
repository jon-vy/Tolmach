import sqlite3 as sq

with sq.connect("db.db") as con:
    cur = con.cursor()

    '''удалить таблицу с именем users'''
    cur.execute("DROP TABLE IF EXISTS date")

    cur.execute("""CREATE TABLE IF NOT EXISTS date (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            txt_eng TEXT,
            txt_ru TEXT,
            eng_playback_speed INTEGER,
            ru_playback_speed INTEGER,
            ru_eng_spacing INTEGER
            )""")