"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="premdatabase"
)

print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)")
#
# # INSERT MANY
# sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
# val = [
#     ('Peter', 154),
#     ('Amy', 155),
#     ('Hannah', 153),
#     ('Michael', 156),
#     ('Sandy', 154),
#     ('Betty', 154),
# ]
#
# mycursor.executemany(sql, val)
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")


sql = "CREATE TABLE products (id INT, name varchar(50))"
# mycursor.execute(sql)

sql = "INSERT INTO products VALUES (%s, %s)"
val = [
    (  154,  'Chocolate Heaven' ),
    ( 155,  'Tasty Lemons' ),
    ( 156,  'Vanilla Dreams' )
]

# mycursor.executemany(sql,val)
mycursor.execute("INSERT INTO products VALUES (157,'condom')")
mydb.commit()



