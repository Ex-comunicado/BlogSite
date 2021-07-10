#this file will only be used once to create the users database
#you can delete this after running it once
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "", #enter your mysql username
    passwd = "" #enter your mysql password
)
my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE users")

#you can erase this part below as it will only show you the updated databases
#not mandatory to run but will act as proof that a database 'users' has been created
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
