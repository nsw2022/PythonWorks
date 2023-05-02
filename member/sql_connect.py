import  sqlite3

def getconn():
    conn = sqlite3.connect('E:/NSW/sqlworks/pydb/member.db')
    return conn

def select():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM member"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = getconn()
    cursor = conn.cursor()
    sql = 'SELECT * FROM member' \
          ' WHERE memberid = ? AND password = ?'
    cursor.execute(sql,('cloul123','m123456#'))
    rs = cursor.fetchone()
    print(rs)
    conn.close()


def insert():
    conn = getconn()
    cursor = conn.cursor()

    sql = "INSERT INTO member(memberid, password, name, gender)" \
          "VALUES(?,?,?,?)"
    cursor.execute(sql, ('today123', 'm123456$', '투데이', '여'))
    conn.commit()
    conn.close()


# insert()
# select()
select_one()
