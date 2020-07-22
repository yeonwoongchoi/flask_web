from flask import Flask , render_template, flash, redirect, url_for, session, request, logging

import pymysql
from data import Articles
from passlib.hash import pbkdf2_sha256


app = Flask(__name__)
app.debug=True

db = pymysql.connect(host='localhost', 
                        port=3306, 
                        user='root', 
                        passwd='1234', 
                        db='myflaskapp')


# sql_1 = 'SELECT * FROM users;'
# # sql_2 = '''
# #         INSERT INTO users(name, email, userame, password) 
# #         VALUES ('LEE , '3@naver.com','LEE','1234');
# #         '''
# # result = cursor.execute(sql_2)
# # db.commit()
# # db.close()
# # # print(result)
# # users = cursor.fetchall()
# # print(users[0][1])
# cursor.execute(sql_1)
# users = cursor.fetchall()
# print(users)
#init mysql
# mysql = MySQL(app)

# cur = mysql.connection,cursor()
# result = cur.execute("SELECT * FROM isers;")
# users - 


# print(result)


@app.route('/login' , methods=['GET' , 'POST'])
def log_in():
    if request.method == 'POST':
        return "LOGED PAGE"
    else:
        return "LOGIN PAGE"

@app.route('/')
def index():
    print("Success")
    # return "TEST"
    return render_template('home.html', hello = "GaryKim")

@app.route('/about')
def about():
    print("Success")
    # return "TEST"
    return render_template('about.html', hello = "GaryKim")


######################## 회원가입 ###############################
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # data = request.body.get('author')
        name = request.form.get('name')
        email = request.form.get('email')
        password = pbkdf2_sha256.hash(request.form.get('password'))
        re_password = request.form.get('re_password')
        username = request.form.get('username')
        # name = form.name.data
        if(pbkdf2_sha256.verify(re_password,password)):
            print(pbkdf2_sha256.verify(re_password,password))
            cursor = db.cursor()
            sql = '''
                INSERT INTO users (name , email , username , password) 
                VALUES (%s ,%s,%s,%s )
             '''
            cursor.execute(sql , (name,email,username,password ))
            db.commit()
            
            # cursor = db.cursor()
            # cursor.execute('SELECT * FROM users;')
            # users = cursor.fetchall()
            return "register Success"
        else:
            return "Invalid Password"
        db.close()
    else:
        return render_template('register.html')


# # 회원가입
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':

#         # data = request.body.get('author')
#         name = request.form.get('name')
#         email = request.form.get('email')
#         username = request.form.get('username')
#         password = request.form.get('password')
#         re_password = request.form.get('re_password')
#         if(password is not re_password):
#             return 'Invalid password'
#         else:
#         # name = form.name.data
#             print([name, email, username, password,re_password])
#             return "POST success"
#     else:
#         return "GET success"











@app.route('/articles')       #methods = ['GET','POST'])로 추가 가능
def articles():
    print("Success")
    # return "TEST"
    articles = Articles()
    print(articles)
    return render_template('articles.html', articles = articles)

@app.route('/test')
def show_image():
    return render_template('image.html')

@app.route('/article/<int:id>')
def article(id):
    print(id)
    articles = Articles()[id-1]
    print(articles)
    return render_template('article.html',data = articles) 
    # return "Success"
if __name__ =='__main__':
    # app.run(host = '0.0.0.0', port='8080')
    app.run()