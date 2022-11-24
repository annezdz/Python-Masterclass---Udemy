import mysql.connector


def createDbConnection():
    global mydb

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='pydb'
    )
    return mydb


def getMySqlQuery(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchone()
    return myresult[0]
