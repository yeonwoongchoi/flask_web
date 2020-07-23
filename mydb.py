import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='myflaskapp')
cursor = db.cursor()
# sql = ''' 
#         CREATE TABLE users(
#             id INT(11) AUTO_INCREMENT PRIMARY KEY, 
#             name VARCHAR(100),
#             email VARCHAR(100),
#             username VARCHAR(30),
#             password VARCHAR(100),
#             register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
#             ENGINE=InnoDB DEFAULT CHARSET=utf8;
#     '''
# sql=''' 
#     CREATE TABLE `topic` (
#     `id` int(11) NOT NULL AUTO_INCREMENT,
#     `title` varchar(100) NOT NULL,
#     `body` text NOT NULL,
#     `author` varchar(30) NOT NULL,
#     `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     PRIMARY KEY (id)
#     ) ENGINE=innoDB DEFAULT CHARSET=utf8;
# '''
# cursor.execute(sql)
# db.commit()
# db.close()
sql_1 = 'SELECT * FROM users;'
sql_2=  '''
        INSERT INTO users(name, email , username, password) 
        VALUES ('PARK' ,'4@naver.com', 'PARK', '1234');
            '''
# cursor.execute(sql_2)
# db.commit()
# db.close()
# print(result)
# users = cursor.fetchall()
# # print(users[0][1])
cursor.execute(sql_1)
users = cursor.fetchall()
print(users)


# name = 'GANGNAM'
# email = '6@naver.com'
# username = 'GANG'
# password = '1234'
# name, email, username, password
# sql_4=  '''
#         INSERT INTO users(name, email , username, password) 
#         VALUES (%s ,%s, %s, %s);
# 		'''
# cursor.execute(sql_4, (name, email , username, password))
# db.commit()
# db.close()
title = 'javascript'
body = '프로토타입기반의 객체지향 프로그래밍'
author = 'Gary'
sql_7=  '''
        INSERT INTO topic(title, body , author) 
        VALUES (%s ,%s, %s);
		'''
# cursor.execute(sql_7 ,(title, body , author))
# db.commit()
# db.close()
# sql_1 = 'DELETE FROM `myflaskapp`.`users` WHERE  `id`=1;'
# cursor.execute(sql_1)
# db.commit()
# db.close()





# 업데이트 할때
sql_6='UPDATE `users` SET `name` ="PARK" WHERE `id` = 6;'
db.commit()
db.close()





# 이건 조회해볼때
sql_7 = 'SELECT * FROM topic;'
cursor.execute(sql_7)
topics = cursor.fetchall()
print(topics)