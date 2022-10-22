from twilio.rest import Client


account_sid = input("Type your account_sid from Twilio: ")
auth_token = input("Type your auth_token from Twilio: ")
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid=input("Type your service_sid from Twilio: "),
    body="halo halo :)",
    to=input("Type phone number with code +xx: "),
)

print(message.sid)
print("Text message sended.")
