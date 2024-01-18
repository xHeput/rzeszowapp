import mysql.connector

data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'xRMajsha942mgCQrCjwH',
)

#cursor object
cursor_object = data_base.cursor()

#create db

cursor_object.execute("CREATE DATABASE mylife_clinic")

print("Wszystko działa / Everything works just fine!")