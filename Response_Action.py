import Mail_Sender as ms
import Mail_Getter as mg
import Response_Object as ro

version = "v0.0.1"
# class for responsing on emails
class Response_Action:

    # constructor
    def __init__(self,confugiration_file,debug):
        self.debug = debug                              # debug info
        self.configuration = confugiration_file         # object for storing data 
        self.fatal_error = False                        # fatal error true if configuration mail broken

        # checking if configuration is good to go
        if self.configuration.fatal_error != True:

            # mails to response
            credentials = self.configuration.get_credentials()
            self.mails = mg.Mail_Getter(credentials[0],
                                    credentials[1],self.debug)
            
            self.mails.run()            # loading e-mails

        else:
            self.fatal_error = True

    # main function of the module
    def run(self):
        print("Running new Responce_Action Instance...")
        for mail in self.mails.mail_object_list:
            print("Reading e-mail: "+str(mail.mail_id))
            responder  = ro.Response_Object(mail,self.configuration)   # single mail responder

            responder.response()
            print("Responded")




