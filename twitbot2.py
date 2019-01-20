from twilio.rest import Client
import mysql.connector

 
#Certificates
account_sid = 'ACd07e510d06fbfe59d748e3185b606a8f' 
auth_token = '04a4b20f3b5da1180d69fa7870d1f3a5'

#Clients
msgClient = Client(account_sid, auth_token)
verifyClient = Client(account_sid, auth_token)


#Create two variables here that will store a full name and 
#phone number to input into validation call

mydb = mysql.connector.connect(
  host="104.236.37.73",
  user="test",
  passwd="Testing123!@#",
  database="cruzhax"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM clients")

result = mycursor.fetchone()

user = 'temp'

for x in result:
    user = x

mydb.close()

print(user)

# #verify
# caller_id = verifyClient.validation_requests.create(
#     friendly_name='First Last',
#     phone_number='+16692371199'
# )
# #Saves verification code sent to client
# verifyCode = caller_id.validation_code
# print(verifyCode)

#Send Message 
# message = msgClient.messages.create( 
#     from_='+14243795098',  
#     body='hey',     
#     to='+16263758987' 
# ) 
# print(message.sid)