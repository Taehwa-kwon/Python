from flask import Flask,render_template, request,redirect
import sqlite3
##from flask import Flask
#flask 패키지에서 Flask 모듈을 import 하고 플라스크를 사용할 수 있도록 설정
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') ##template 폴더안에 랜더링해서 html로 보낸다.


@app.route('/form')
def inputform():
    return render_template('inputform.html')

@app.route("/inputprocess",methods=['POST'])
def inputprocess():
    name = request.form['name']  ##이렇게 받기.
    email = request.form['email']
    address = request.form['address']
    
    conn = sqlite3.connect('flaskDB/member.db')
    c = conn.cursor()
    c.execute(''' 
                create table if not exists member (name text, email text, address text)  
              ''')
    sql = 'insert into member values(?,?,? ) '          
    c.execute(sql,(name,email,address))
    conn.commit()
    conn.close()
    return redirect('/list')
    ##return render_template('result.html',data=[name,email,address])  ##혹은 name=name,email.email, 이런식으로 넘겨도 된다.

@app.route('/list')
def memberlist():
    conn = sqlite3.connect('flaskDB/member.db')
    c = conn.cursor()
    c.execute('select * from member')
    c.fetchall   ##c.fetchone 하나 가져오기
    items = c.fetchall()   ##print로 출력가능

    conn.close()
    return render_template('list.html',items=items)

@app.route('/update/<name>')  ##들어오는 값
def memberupdate(name):
    conn = sqlite3.connect('flaskDB/member.db')
    c = conn.cursor()
    sql = 'select * from member where name = ?'
    c.execute(sql,(name,))
    item = c.fetchone()

    return render_template('updateform.html',item=item)

@app.route("/updateprocess" , methods=['POST']) ##이렇게 update, updateform하면 복잡하니깐 method방식에 따라 if 로 구분줘도 좋다.
def updateprocess():
    name = request.form['name']  ##이렇게 받기.
    email = request.form['email']
    address = request.form['address']
    
    conn = sqlite3.connect('flaskDB/member.db')
    c = conn.cursor()
    
    sql = 'update member set email=?,address=? where name=? '          
    c.execute(sql,(email,address,name))
    conn.commit()
    conn.close()
    return redirect('/list')



@app.route('/delete/<name>')
def memberdelete(name):
    conn = sqlite3.connect('flaskDB/member.db')
    c = conn.cursor()
    sql = 'delete from member where name=?'
    c.execute(sql,(name,))
    conn.commit()
    conn.close()
    return redirect('/list')



if __name__=='__main__':
    app.run(debug=True,port=80) ##포트번호 80에서 플라스크를 열어주세요 
    
    
