import tweepy
import mysql.connector


mydb = mysql.connector.connect(
  host="104.236.37.73",
  user="test",
  passwd="Testing123!@#",
  database="cruzhax"
)

mycursor = mydb.cursor()

# sql = "INSERT INTO clients (name, phone) VALUES (%s, %s)"
# val = ("Pablo Gaeta", "+16263758987")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT FROM clients")

result = mycursor.fetchall()

for x in result:
    print(x)

mydb.close()