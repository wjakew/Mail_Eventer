import Mail_Object as mo

version = "v1.0.0"
# collection stores main key words for data
translator = {"Content-Type:":0,"Content-Transfer-Encoding:":1,"From:":2,"Mime-Version:":3,"Date:":4,
                    "Subject:":5,"Message-Id:":6,"To:":7,"X-Mailer:":8}
size = len(translator)

# syntax analiser for mail raw data from gmail
class Parser:

    # constructor
    def __init__(self,raw_data):

        self.raw_data = raw_data

        self.size = len(self.raw_data)
        
        self.mail_header = []               # containts raw head

        self.key_header_list = []           # contains values from head of the mail

    # function searches for main e-mail data
    def get_head(self,raw_data):
        head_to_ret = []

        for line in raw_data:
            if "Content-Type:" in line:
                starting_point = raw_data.index(line)

                for i in range (starting_point, len(raw_data)-1):
                    head_to_ret.append(raw_data[i])

        return head_to_ret

    # main run function
    def run(self):
        
        self.mail_header = self.get_head(self.raw_data)
        self.key_header_list = self.parase_head(self.mail_header)

# mail data getters

    # function fror getting from e-mail address
    def get_from(self):
        #data =  self.key_header_list[2]
        #return data.split("<")[1][0:len(data.split("<")[1])-1]
        return self.key_header_list[2]
    # function for getting subject
    def get_subject(self):
        return self.key_header_list[5]

    # function for getting content
    def get_content(self):
        content = []
        string_toRet = ""

        for i in range(9, len(self.key_header_list)):
            if self.key_header_list[i] == "":
                pass
            else:
                content.append(self.key_header_list[i])

        for line in content:
            string_toRet = string_toRet + line + "\n"

        return string_toRet

# end of mail data getters

    # mail object loader

    def get_mail_object(self):

        return mo.Mail_Object(self.get_from(),self.get_subject(),self.get_content())

    # function for side loading lists 
    def list_loader(self,amount):
        list_to_ret = []

        for i in range(0,amount):
            list_to_ret.append("")

        return list_to_ret

    # function translates header names to indexes in list 
    def head_translator(self,header):
        return translator[header]

    # function for inserting data to collection categorized by header
    def list_inserter(self,header,collection,data):

        index = self.head_translator(header)

        collection[index] = data
        
        return collection

    # function for searching data in head part of email
    # returning collection:
    #  elements_toRet = 
    #               = [Content-Type:
    #                   Content-Transfer-Encoding:
    #                    From:
    #                     Mime-Version:
    #                      Date:
    #                       Subject:
    #                        Message-Id:
    #                         To:
    #                           X-Mailer:
    #                            /content lines/ ... ]
    def parase_head(self,head_data):
        elements_toRet = self.list_loader(9)
        content = []
        # looping on lines in head

        last_element = ""

        for element in head_data:

            for key in translator.keys():
                if key in element:
                    # eg line:
                    # 'Content-Type: text/plain; charset=us-ascii'
                    elements_toRet = self.list_inserter(key,elements_toRet,element.split(":")[1].rstrip().lstrip()) # adding 
                    last_element = element      # last element as a flag for adding content
                else:
                    # adding content
                    if "X-Mailer:" in last_element:
                        if element in content:
                            pass
                        else:
                            content.append(element)


        elements_toRet.extend(content)
            
        return elements_toRet

    # function for showing data 
    def show_list(self, list_to_show):
        for line in list_to_show:
            print(line)
            
    # function for showing data from Parser
    def show(self):
        print("------------------------------------------------")
        print("Parser raw data count : " + str(self.size))
        print("Parser raw data:")
        print("---------------------------------")
        print("Raw head data:")
        #self.show_list(self.mail_header)
        print("---------------------------------")
        print(str(translator))
        print("Categorized data:")
        self.show_list(self.key_header_list)
        print("---------------------------------")
        print("End")
        print("------------------------------------------------")




