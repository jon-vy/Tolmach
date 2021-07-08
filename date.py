import sqlite3 as sq  # https://youtu.be/TCdyfEvrIUg


def save(column, txt):
    with sq.connect("db.db") as con:
        cur = con.cursor()
        cur.execute(f"UPDATE date SET {column} = '{txt}'  WHERE id = 1")

if __name__ == "__main__":
    col = 'eng_playback_speed'
    t = '50'
    save(col, t)
