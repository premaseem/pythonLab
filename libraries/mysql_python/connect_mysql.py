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
# cursor.execute("CREATE database premdatabase")
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)

# Create table
# mycursor.execute("drop table customers")
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")