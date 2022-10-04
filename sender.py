import smtplib
import mimetypes
from email.message import EmailMessage

sender_email = input("Type your adress: ")
recipient_email = input("Type recipient adress: ")
sender_passwd = input("Type your password(your token from gmail account): ")

message = EmailMessage()
sender = sender_email
recipient = recipient_email
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "No Subject"
body = input("Your message: ")
message.set_content(body)

choose = input("1-text or enter-attachment?")
if choose == "1":
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.set_debuglevel(1)

    smtp.login(sender_email, sender_passwd)
    smtp.send_message(message)
    smtp.quit()
else:
    file_path = input("Paste file PATH to send: ")
    mime_type, _ = mimetypes.guess_type(file_path)
    mime_type, mime_subtype = mime_type.split("/")
    with open(file_path, "rb") as file:
        message.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype)
        # filename='filename')
    # print(message)

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.set_debuglevel(1)

    smtp.login(sender_email, sender_passwd)
    smtp.send_message(message)
    smtp.quit()
