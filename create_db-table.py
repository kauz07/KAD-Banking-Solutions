import mysql.connector as ms # imported mysql.connector

print("__________________ CONNECTING WITH MYSQL __________________")


connection = ms.connect(host = 'localhost',user ="root",password ="1883")
mycursor = connection.cursor() # created cursor

mycursor.execute("create database nb;")
mycursor.execute("commit;")

mycursor.execute("use nb;")
mycursor.execute("commit;")

c1 = 'user_name varchar(30),'
c2 = 'password varchar(20),'
c3 = 'balance int(10),'
c4 = 'dob varchar(20),'
c5 = 'gender varchar(10)'
create_table = 'create table users('+ c1 + c2 + c3 + c4 + c5 +');'

mycursor.execute(create_table)
mycursor.execute("commit;")

print("*your database and table is created*")
input('')
