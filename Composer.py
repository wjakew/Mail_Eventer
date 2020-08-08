# by Jakub Wawak 08.2020
# all rights reserved
# kubawawak@gmail.com

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
KEY_WORDS = ["%time","%getip","%getstatus","%getnotify","%executecommand"]
# class for decomposing e-mail message and coposing response
class Composer:

    # constructor
    def __init__(self,data_to_recompose,debug_info):

        # version of the module
        self.version = "v0.0.1"

        # debug info
        self.debug = debug_info

        self.log(self.version)
        self.log("Debug is on")

        # object data
        self.content = data_to_recompose        # field for storing raw content

        self.lines = self.prepare_data()        # all of lines from object

        self.key_dictionary = {}                # collection for keys and values

        self.categorize()                       # categorization function

        self.info()

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
                #checking if word is key
                if word in KEY_WORDS:
                    # adding word as a key
                    if line.split(" ").index(word)+1 in range(0,len(line.split(" "))-1):
                        self.key_dictionary[word] = line.split(" ")[(line.split(" ").index(word)+1)]
                    else:
                        self.key_dictionary[word] = ""

    # function for printing data
    def log(self,data):
        if self.debug == 1:
            print(HEADER + " " + data)


    # function for showing info data
    def info(self):
        self.log("Number of lines in content: "+str(len(self.lines)))
        self.log(str(self.lines))
        self.log(str(self.key_dictionary))

