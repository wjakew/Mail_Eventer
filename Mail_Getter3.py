# by Jakub Wawak 08.2020
# all rights reserved
# kubawawak@gmail.com
import smtplib
import time
import imaplib
import email

# object for getting emails from gmail account
class Mail_Getter3:


    # constructor
    def __init__(self,service_email,service_password,debug):

        self.imap_host = 'imap.gmail.com'
        self.imap_user = service_email
        self.imap_pass = service_password
        self.debug = debug

    # collection for storing emails data
        self.mail_object_list = []          # type: Mail_Object



    # function for connecting to gmail
    def connect(self):

        return imaplib.IMAP4_SSL(self.imap_host)


    # function for fetching emails
    def fetch(self):

        # making ssl connetion to the gmail server
        mail = self.connect()

        # logging to the account
        mail.login(self.imap_user,self.imap_pass)

        # setting the folder on the email account
        mail.select('inbox')

        typ, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print ('From : ' + email_from + '\n')
                    print ('Subject : ' + email_subject + '\n')


