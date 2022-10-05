import smtplib
import mimetypes
from email.message import EmailMessage


class Send:
    def connect(self):
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.set_debuglevel(1)

        smtp.login(sender_email, sender_passwd)
        smtp.send_message(message)
        smtp.quit()


class Text(Send):
    def push(self):
        super().connect()


class Attachment(Send):
    def push_attachment(self):
        file_path = input("Paste file PATH to send: ")
        mime_type, _ = mimetypes.guess_type(file_path)
        mime_type, mime_subtype = mime_type.split("/")
        with open(file_path, "rb") as file:
            message.add_attachment(
                file.read(), maintype=mime_type, subtype=mime_subtype
            )
        super().connect()


sender_email = input("Type your adress: ")
recipient_email = input("Type recipient adress: ")
sender_passwd = input("Type your password (your token from gmail account): ")

message = EmailMessage()
sender = sender_email
recipient = recipient_email
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "No Subject"
body = input("Your message: ")
message.set_content(body)


send = Send()
text = Text()
attachment = Attachment()
while True:
    choose = input("""1 for only text, \nenter for text and attachment,
q for quit\n:""")

    if choose == "q":
        break

    elif choose == "1":
        text.push()
        print("Mail sended.")

    else:
        attachment.push_attachment()
        print("Attachment sended.")
