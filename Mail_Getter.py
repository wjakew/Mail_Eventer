# by Jakub Wawak 07.2020
# all rights reserved
# kubawawak@gmail.com
import Mail_Object as mo
import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# object for storing and importing emails
class Mail_Getter:

    # constructor
    def __init__(self, email_address,user_password):
        # version of the module
        self.version = "v.1.0.0"
        # account credentials
        self.username = email_address
        self.password = user_password

        # collection for storing emails data
        self.mail_object_list = []
        # create an IMAP4 class with SSL 
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        # authenticate
        self.imap.login(self.username, self.password)

        self.status, self.messages = self.imap.select("INBOX")
        # number of top emails to fetch
        self.N = 3
        # total number of emails
        self.messages = int(self.messages[0])

    # function for ending connection and logout
    def end(self):
        self.imap.close()
        self.imap.logout()

    # main function for getting feedback
    def run(self):
        self.get_mails()
        self.end()

    # function for getting emails
    def get_mails(self):
        for i in range(self.messages, self.messages-self.N, -1):
            # fetch the email message by ID
            res, msg = self.imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        # if it's a bytes, decode to str
                        subject = subject.decode()
                    # email sender
                    from_ = msg.get("From")
                    # if the email message is multipart
                    if msg.is_multipart():
                        # iterate over email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                # print text/plain emails and skip attachments
                                self.mail_object_list.append(mo.Mail_Object(from_,subject,body))
                                
                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            # print only text email parts
                            self.mail_object_list.append(mo.Mail_Object(from_,subject,body))


