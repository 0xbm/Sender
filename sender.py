import smtplib
import mimetypes
from email.message import EmailMessage
message = EmailMessage()
sender = "asd@gmail.com"
recipient ="asd@gmail.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Learning Python'
body = "Hello"
message.set_content(body)
mime_type, _ = mimetypes.guess_type('filename')
mime_type, mime_subtype = mime_type.split('/')

with open('PATH', 'rb') as file:
    message.add_attachment(file.read(),
    maintype=mime_type,
    subtype=mime_subtype,
    filename='filename')
print(message)


smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.starttls()

smtp.login("asd@gmail.com", 'asd')
smtp.send_message(message)
smtp.quit()











