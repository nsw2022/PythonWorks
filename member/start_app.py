# 컨트롤러 start_app.py
# templates 폴더, static
# 웹 서버 - flask

from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

def getconn():
    conn = sqlite3.connect('E:/NSW/sqlworks/pydb/member.db')
    return conn

# url - '/' 설정
@app.route('/')
def index():
    return render_template("index.html")

#회원 목록 methods는 기본값이 GET이라 GET방식일땐 생략해도 가능
@app.route('/memberlist', methods = ['GET'])
def memberlist():

    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM member"
    cursor.execute(sql)
    rs = cursor.fetchall()
    conn.close()

    return render_template('memberlist.html', rs=rs)

# 회원가입
@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        # 가입 폼에 입력된 자료 넘겨 받음
        id = request.form['memberid']
        pw = request.form['passwd1']
        name = request.form['name']
        gender = request.form['gender']

        # db에 저장
        conn = getconn()
        cursor = conn.cursor()
        sql = f"INSERT INTO member(memberid, password, name, gender) " \
              f" VALUES('{id}', '{pw}', '{name}', '{gender}')"
        cursor.execute(sql)
        conn.commit()
        conn.close()

        # 이방식은 안되려나? 나중에 테스트해보기 안되네
        # sql = "INSERT INTO member(memberid, password, name, gender) " \
        #       " VALUES(?,?,?,?)"
        # cursor.execute(sql, (id,pw,name,gender))
        # conn.commit()
        # conn.close()

        # redirect - 회원 가입후 회원 목록 페이지로 강제로 이동
        return redirect(url_for('memberlist'))
    else:
        return render_template('register.html')


app.run()