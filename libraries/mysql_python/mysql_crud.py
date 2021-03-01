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

# Create table
# mycursor.execute("drop table customers")
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# INSERT INTO

sql = "INSERT INTO customers(name,address) VALUES ('prem','san antonio') "
sql = "INSERT INTO customers(name,address) VALUES (%s , %s)"
values = ("Aseem Jain", "4114 medical dr")
# mycursor.execute(sql,values)
# mydb.commit()

# INSERT MANY
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

# mycursor.executemany(sql, val)

# mydb.commit()
print(mycursor.rowcount, "was inserted.")

sql = "SELECT * from customers"
mycursor.execute(sql)
result_set = mycursor.fetchall()
# result_set = mycursor.fetchone()
for x in result_set:
    print(x)

# update

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

