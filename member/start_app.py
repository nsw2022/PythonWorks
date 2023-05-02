# 컨트롤러 start_app.py
# templates 폴더, static
# 웹 서버 - flask

from flask import Flask, render_template, request, redirect,\
    url_for, session
import sqlite3


app = Flask(__name__)

app.secret_key = "qwerasdf1234!@#$"

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

        # 이방법도 가능
        # sql = "INSERT INTO member(memberid, password, name, gender) " \ <- !!여기서 한칸띄우거나 VALUES에서 한칸 띄우는거 주의!!
        #       " VALUES(?,?,?,?)"
        # cursor.execute(sql, (id,pw,name,gender))
        # conn.commit()
        # conn.close()

        # redirect - 회원 가입후 회원 목록 페이지로 강제로 이동
        return redirect(url_for('memberlist'))
    else:
        return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # 로그인 폼에 입력된 데이터를 넘겨 받기
        id = request.form['memberid']
        pw = request.form['passwd']

        # database에 접속 - 로그인 체크
        conn = getconn()
        cursor = conn.cursor()
        sql = f'SELECT * FROM member ' \
              f' WHERE memberid = "{id}" AND password = "{pw}"'
        cursor.execute(sql)
        rs = cursor.fetchone()
        conn.close()
        if rs: # rs=True
            session['userid'] = rs[0] # memberid를 세션에 저장(세션 발급)

            return redirect(url_for('index'))
        else:
            error_msg = "아이디나 비밀번호를 확인해주세요."
            return render_template('login.html',error_msg=error_msg)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear() # 모든 세션 삭제
    return redirect(url_for('index'))


app.run()