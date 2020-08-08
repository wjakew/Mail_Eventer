# by Jakub Wawak 07.2020
# all rights reserved
# kubawawak@gmail.com
import time
import Composer as comp

class Mail_Object:

    # constructor
    def __init__(self,email_from,email_subject,email_content):

        # version of the object
        self.version = "v.1.1.0"

        # data from email
        self.subject = email_content
        self.content = email_content
        self.from_id = email_from

        # data of the object

        self.date = time.asctime()                              # time of making object
        self.compose_object = comp.Composer(self.content,1)       # object for storing data
        self.mail_id = int(hash(self.content))                     # every mail gets his mail id

    # function for showing data of email
    def simple_show(self):
        print(str(self.mail_id))
        print("-----Email-----")
        print("From: "+self.from_id)
        print("     Subject: "+self.subject)
        print(self.content)


