# by Jakub Wawak 07.2020
# all rights reserved
# kubawawak@gmail.com

class Mail_Object:

    # constructor
    def __init__(self,email_from,email_subject,email_content):

        # version of the object
        self.version = "v.1.0.0"

        # data from email
        self.subject = email_content
        self.content = email_content
        self.from_id = email_from


    # function for showing data of email
    def simple_show(self):

        print("-----Email-----")
        print("From: "+self.from_id)
        print("     Subject: "+self.subject)
        print(self.content)

