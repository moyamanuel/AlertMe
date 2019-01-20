from twilio.rest import Client
import config, asyncio, re

#Clients
msgClient = Client(config.account_sid, config.auth_token)
verifyClient = Client(config.account_sid, config.auth_token)

def on_register(number):
    num = re.sub(r'\W', '', number)

    
#verify
#   caller_id = verifyClient.validation_requests.create(
#       friendly_name=first + ' ' last,
#       phone_number='+1' + num
#   )
#   #Saves verification code sent to client
#   verifyCode = caller_id.validation_code
#   print(verifyCode)

#Send Message 
# def on_emergency():
  
#   for i in database:
#     # message = msgClient.messages.create( 
#     #     from_='+14243795098',  
#     #     body='hey',     
#     #     to='+16263758987' 
#     # ) 
