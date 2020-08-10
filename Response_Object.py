import Mail_Sender as ms


# single object for responsing for one emai
class Response_Object:

    # constructor
    def __init__(self, mail_object,configuration_file):

        self.mail_to_response = mail_object         # Mail_Object variable
        self.configuration = configuration_file

    # function for responsing for email    
    def response(self):

        if self.mail_to_response.check_compose_status() == True:
            
            #composing answer
            content_response = self.mail_to_response.compose_object.compose()
            credentials = self.configuration.get_credentials()
            subject = "Response for: "+str(self.mail_to_response.mail_id)
            mail_to_send = ms.Mail_Sender(credentials[0],credentials[1])

            mail_to_send.send(self.mail_to_response.from_id,subject,self.response_wrapper(content_response))

        else:
            pass

    # function for wrapping responses
    def response_wrapper(self,data_to_wrap):
        welcome_string = "Dear "+self.mail_to_response.from_id.split("@")[0]+",\n"+"Thanks for using Mail_Eventer app!\n"+"Your response : "+self.mail_to_response.compose_object.get_whole_query()+"\n"+"Your answer: "+data_to_wrap

        return welcome_string




