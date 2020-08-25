# by Jakub Wawak 08.2020
# all rights reserved
# kubawawak@gmail.com
import imaplib
import time
import Parser as p
version = "v2.0.1"
class Mail_Getter2:

    def __init__(self,service_email,service_password,debug):

        self.imap_host = 'imap.gmail.com'
        self.imap_user = service_email
        self.imap_pass = service_password
        self.debug = debug

    # collection for storing emails data
        self.mail_object_list = []          # type: Mail_Object
        self.parsed_objects = []            # type: Parser

        # connect to host using SSL
        self.imap = imaplib.IMAP4_SSL(self.imap_host)

    # main run function, loades mail object to mail_object_lists 
    def run(self):

        raw_messages = self.fetch() # fetching raw data

        # parasing data
        for r_message in raw_messages:
            # adding mail to parase
            parsed_obj = p.Parser(r_message)
            parsed_obj.run()

            self.parsed_objects.append(parsed_obj)

        # adding parased data to Mail_Object
        for p_message in self.parsed_objects:
            self.mail_object_list.append(p_message.get_mail_object())

    # returns list of raw lists of data from emails
    def fetch(self):
        messages_raw = []
            ## login to server
        self.imap.login(self.imap_user, self.imap_pass)

        self.imap.select('Inbox')

        tmp,data = self.imap.search(None, 'ALL')
        for num in data[0].split():
            tmp, data = self.imap.fetch(num, '(RFC822)')
            data = str(data[0][1])
            messages_raw.append(data.split("\\r\\n"))
        self.imap.close()
        return messages_raw

    # function for loading to file mail data
    def load_to_files(self, data_list):
        i = 0
        # looping on mails
        for data in data_list:
            f_name = "message_"+str(i)+"_"+time.asctime().replace(" ","_")+".txt"
            mail_file = open(f_name,"w")

            # looping on lines in mail
            for line in data:
                # clearing blank 
                line.rstrip()
                line.lstrip()
                # writing to file
                mail_file.write(line + "\n")

            i = i + 1       # editing 
