# BlogSite
A web application created using Python Flask and jinja2 along with HTML to submit, view and edit blogs. Users can register by providing their username, e-mail id and password. Both the users and blog posts are stored in a mysql database.

# Before Downloading
To run this web application on your system, you need to have a prerequisite. You will aslo need to make some minor changes in the code provided but the guide below will help you in doing those. You do not need any prior coding knowledge to run this application.

The prerequisite that you need to have is mysql installed on your system. You should also remember the username and password that you have set for the service. This web application will create a database on your system to store user account details and blog contents.

# Steps
If and when you install mysql in your system, move on with the steps mentioned below.

1. Make the following changes in the /blogsite/blogmain/\__init__\.py file,
```ruby
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://mysqlusername:mysqlpassword@localhost/users" #replace mysqlusername with your mysql username and mysqlpassword with your mysql password
app.config['SECRET_KEY'] = "" #enter an encrypted key to generate anti-CSRF tokens
```
2. Make the following changes in the /blogsite/create_db.py file,
```ruby
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
```
3. After performing these operations, run the /blogsite/create_db.py file using the command below. As mentioned, you can now delete this file if you wish to.
```ruby
python create_db.py
```
4. Now, open a python shell using the command prompt in your Windows system.
5. Type the following piece of python code in the python shell to create the tables required for the web application to run,
```ruby
from blogmain import db
db.create_all()
```
6. You can now exit the python shell. To start the web application, using your command prompt travel to the /blogsite directory and run the python file run.py as follows,
```ruby
python run.py
```
7. This will prompt you that a web server is now running at 127.0.0.1:5000. Input this address on your browser to access the Web Application.
