from sms.smsSender import Sms
from mail.mailSender import Mail


def main(self):
    choice = input("Would you like send 1.EMAIL, 2.SMS? or q for quit: ")
    match choice:
        case "1":
            Mail.start(Mail)
        case "2":
            Sms.push_sms(Sms)
        case "q":
            breakpoint
            print("\x1b[5;30;42mQUIT")


main(main)

# if __name__ == "__main__":
#     main()
#     print("ASD")
