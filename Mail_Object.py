# by Jakub Wawak 07.2020
# all rights reserved
# kubawawak@gmail.com
import time
import Composer as comp
version = "v.1.1.2"
class Mail_Object:

    # constructor
    def __init__(self,email_from,email_subject,email_content):

        # version of the object

        # data from email
        self.subject = email_subject
        self.content = email_content
        self.from_id = email_from
        if "<" in self.from_id:
            self.from_id = self.from_id.split("<")[1][0:len(self.from_id.split("<")[1])-1]


        # data of the object

        self.date = time.asctime()                              # time of making object
        self.compose_object = comp.Composer(self.content,1)       # object for storing data
        self.mail_id = int(hash(self.content))                     # every mail gets his mail id

    # function for showing data of email
    def simple_show(self):
        print(str(self.mail_id))
        print("-----Email-----")
        print("From: "+self.from_id)
        print("Subject: "+self.subject)
        print(self.content)

    # returns if email has data to response
    def check_compose_status(self):
        return self.compose_object.get_categorization_status()


