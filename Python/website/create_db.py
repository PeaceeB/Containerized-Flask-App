import mysql.connector
import os

mydb = mysql.connector.connect(
    host="pba42blogdb.c6jtmnlypkzc.eu-west-1.rds.amazonaws.com",
    user="admin", 
    passwd="admin123",
    port="3306"
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE USER 'root' IDENTIFIED BY 'password123'")
# my_cursor.execute("CREATE USER 'admin' IDENTIFIED BY 'admin123'")
# my_cursor.execute("CREATE DATABASE blogdatabase")

# my_cursor.execute("GRANT ALL PRIVILEGES ON blogdatabase.* TO root")

# my_cursor.execute("FLUSH PRIVILEGES")


my_cursor.execute("SHOW DATABASES")
for dbs in my_cursor:
    print(dbs)