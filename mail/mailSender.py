import smtplib
import mimetypes
from email.message import EmailMessage


class Send:
    def mail_Info(self):
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.set_debuglevel(1)

        smtp.login(sender, sender_passwd)
        smtp.send_message(message)
        smtp.quit()


class Text(Send):
    def push(self):
        super().mail_Info()


class Attachment(Send):
    def push_attachment(self):
        file_path = input("Paste file PATH to send: ")
        mime_type, _ = mimetypes.guess_type(file_path)
        mime_type, mime_subtype = mime_type.split("/")
        with open(file_path, "rb") as file:
            message.add_attachment(
                file.read(), maintype=mime_type, subtype=mime_subtype
            )
        super().mail_Info()


message = EmailMessage()
sender = input("Type your address: ")
sender_passwd = input("Type your password (your token from gmail account): ")
recipient = input("Type recipient address: ")
message["From"] = sender
message["To"] = recipient
message["Subject"] = input("Type email subject: ")
body = input("Your message: ")
message.set_content(body)

send = Send()
text = Text()
attachment = Attachment()


while True:
    choice = input("1 for only text, \n2 for text and attachment, b for back\n: ")
    if choice == "b":
        exec(open("main.py").read())
    elif choice == "1":
        text.push()
        print("Mail sended.")
    elif choice == "2":
        attachment.push_attachment()
        print("Attachment sended.")
    else:
        print("Choose between 1 or 2 or b: ")
