# by Jakub Wawak 07.2020
# all rights reserved
# kubawawak@gmail.com
import smtplib
from email.message import EmailMessage
version = "v1.0.0"
# object for sending emails
class Mail_Sender:

    # constructor
    def __init__(self,login,password):
        self.LOGIN = login
        self.PASSWORD = password

        # making SMPT SLL connection 
        self.smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)

    # function for sending emails
    def send(self,email_to,subject,content):
        try:
            self.smtpObj.login(self.LOGIN,self.PASSWORD)
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = self.LOGIN
            msg['To'] = email_to
            msg.set_content(content)

            self.smtpObj.sendmail(self.LOGIN, email_to,msg.as_string())
            return 1
        except Exception as e:
            print(str(e))
            return 0

