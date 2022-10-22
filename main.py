from sms.smsSender import Sms
from mail.mailSender import Mail


def asd(self):
    choice = input("Would you like send 1.EMAIL, 2.SMS? or q for quit: ")
    match choice:
        case "1":
            Mail.start(Mail)
        case "2":
            Sms.push_sms(Sms)
        case "q":
            breakpoint
            print("QUIT")


asd(asd)
