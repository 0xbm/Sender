import smtplib

address = "smtp.awnspeeds.com"
port = 465
login = "kweli.33"
password = "d3a34e1dfcc1cac2ce7fb7c600512440"

smtp_Obj = smtplib.SMTP_SSL(address, port)
print(type(smtp_Obj))

code, msg = smtp_Obj.ehlo()

if code == 250:
    # smtp_Obj.starttls()
    code_auth, msg_auth = smtp_Obj.login(login, password)
    if code_auth == 235:
        smtp_Obj.sendmail(
            "kweli.33@awnspeeds.com",
            """Subject: HEJ\n
                          test mail\n
                          pzdr
                          """,
        )
        smtp_Obj.quit()
    else:
        print(code_auth, msg_auth)
else:
    print(code, msg)
