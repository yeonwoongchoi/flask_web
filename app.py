from flask import Flask , render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
import pymysql
from data import Articles

app = Flask(__name__)
app.debug=True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL__CURSORCLASS'] = 'DictCursor'

db = pymysql.connect(host='localhost', 
                        port=3306, 
                        user='root', 
                        passwd='1234', 
                        db='myflaskapp')

cursor = db.cursor()
sql_1 = 'SELECT * FROM users;'
# sql_2 = '''
#         INSERT INTO users(name, email, userame, password) 
#         VALUES ('LEE , '3@naver.com','LEE','1234');
#         '''
# result = cursor.execute(sql_2)
# db.commit()
# db.close()
# # print(result)
# users = cursor.fetchall()
# print(users[0][1])
cursor.execute(sql_1)
users = cursor.fetchall
print(users)
#init mysql
# mysql = MySQL(app)

# cur = mysql.connection,cursor()
# result = cur.execute("SELECT * FROM isers;")
# users - 


# print(result)




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


    