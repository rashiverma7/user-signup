import sqlite3 as sql


def create_table():
    con = sql.connect("usersinfo.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "id integer primary key autoincrement,"
                "username text not null,"
                "password text not null,"
                "isLoggedIn boolean not null)")
    con.commit()
    con.close()


def insert_user(username, password):
    con = sql.connect("usersinfo.db")
    cur = con.cursor()
    cur.execute("INSERT into users(username, password) VALUES (?,?)", (username, password))
    con.commit()
    con.close()


def fetch_user(username):
    con = sql.connect("usersinfo.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users where username = '%s'" % username)
    users = cur.fetchall()
    print(users)
    con.close()
    return users

