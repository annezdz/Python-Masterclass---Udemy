import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='pydb'
)

mycursor = mydb.cursor()
mycursor.execute("select tutorial_author from selenium where tutorial_id = 2")
# myresult = mycursor.fetchall()
#
# for result in myresult:
#     print(result)

myresult = mycursor.fetchone()
print(myresult[0])