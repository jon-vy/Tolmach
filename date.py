import sqlite3 as sq  # https://youtu.be/TCdyfEvrIUg


def select():
    with sq.connect("db.db") as con:
        cur = con.cursor()
        #cur.execute("UPDATE date SET {column} = '{txt}'  WHERE id = 1")
        c = cur.execute("SELECT * FROM date WHERE id = 1").fetchall()
        # print(c[0][2])
        return c



if __name__ == "__main__":
    print(select()[0][1])
