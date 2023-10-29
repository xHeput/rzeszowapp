import mysql.connector

data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'AIQt5eaGt03Z8eWZU1s0',
)

#cursor object
cursor_object = data_base.cursor()

#create db

cursor_object.execute("CREATE DATABASE mylifeclinicdb")

print("Wszystko działa / Everything works just fine!")