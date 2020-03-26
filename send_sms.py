from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC7a5eb26af08bf3acc94dfb5fabb6a36d'
auth_token = '0ce3a4c0a7eb2d24ce722f2222b72cc2'
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="We can put any text we like in the message",
                     from_='+12162509015',
                     to='+14406231816'
                 )

print(message.sid)

#This code works, but we can only send to a verified phone number
# because we're using a trial version. My phone number is verified
# so it works for me
