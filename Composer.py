# by Jakub Wawak 08.2020
# all rights reserved
# kubawawak@gmail.com
import time
import urllib.request
"""
notes about object:

general idea:

object stores content of mail and searches for key words and categorizes them

main ideas of key words implemented:

( idea of having txt file with key words and responses to them like eg. % welcome test)

%time
    - returns time
%getip
    - returns actual global ip and local
%getstatus
    - returns status of the system like system info, processes, ips, hardware data
%getnotify /command/
    - set same state to waiting to change and send response when it changed
%executecommand /command/
    - executes comand on machine and send response by e-mail
"""
HEADER = "COMPOSER"
KEY_WORDS = ["%time", "%getip", "%getstatus", "%getnotify", "%executecommand"]
version = "v1.0.0"


# class for decomposing e-mail message and coposing response

class Composer:

    # constructor
    def __init__(self, data_to_recompose, debug_info):

        # debug info
        self.debug = debug_info

        self.log(version)
        self.log("Debug is on")

        # object data
        self.content = data_to_recompose        # field for storing raw content

        self.lines = self.prepare_data()        # all of lines from object

        self.key_dictionary = {}                # collection for keys and values found in mail

        self.categorize()                       # categorization function

        self.info()



    # main function for composing answer
    def compose(self):
        for key in self.key_dictionary.keys():
            if key == "%time":
                return self.compose_response_time()

            elif key == "%getip":
                return self.compose_response_getip()


#-------------------------------------_COMPOSE RESPONSE FUNCTIONS
    # compose function reponse - time
    def compose_response_time(self):
        return time.asctime()

    def compose_response_getip(self):
        return urllib.request.urlopen('https://ident.me').read().decode('utf8')
#-----------------------------------------------------------------
    # checking if we found something
    def get_categorization_status(self):

        return len(self.key_dictionary) > 0

    # returning whole query found by object
    def get_whole_query(self):
        return str(self.key_dictionary)

    # function for preparing data into lines
    def prepare_data(self):

        lines_to_ret = []

        for text_line in self.content.split("\n"):

            lines_to_ret.append(text_line.rstrip())

        return lines_to_ret

    def categorize(self):
        # looping on lines
        for line in self.lines:
            # looping on words
            for word in line.split(" "):
                # checking if word is key
                if word in KEY_WORDS:
                    # adding word as a key
                    if line.split(" ").index(word)+1 in range(0, len(line.split(" "))-1):
                        self.key_dictionary[word] = line.split(
                            " ")[(line.split(" ").index(word)+1)]
                    else:
                        self.key_dictionary[word] = ""

    # function for printing data
    def log(self, data):
        if self.debug == 1:
            print(HEADER + " " + data)

    # function for showing info data

    def info(self):
        self.log("Number of lines in content: "+str(len(self.lines)))
        self.log(str(self.lines))
        self.log(str(self.key_dictionary))
