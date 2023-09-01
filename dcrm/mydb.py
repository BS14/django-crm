import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'project',
    password = 'test123'
)

# Prepare a cursor object
cursorObject = dataBase.cursor()
