# by Jakub Wawak 07.2020
# all rights reserved
# kubawawak@gmail.com

import os

# supported file structure:
"""
    %setup
    default
    %version
    v1.0.0
    %login              <--- key
    admin     <--- value
    %user_password
    admin1234
    %e-mail
    test@test.com
    %e-mail password
    test_password
"""
# final variables
HEADER = "File_Reader"
version = "v0.0.1"
clear_file = ["%setup","default","%version","v1.0.0","%login","admin",
                "%user_password","admin1234","%e-mail","","%e-mail password",""]
# object for mantaining file
class File_Reader:

    def __init__(self,src,debug):
        self.debug = debug
        self.log_print(version + " inicialization...")
        self.log_print("clear_file check: "+str(self.counter("%",clear_file)))
        self.file_path = src                # path in string pointing on file
        self.log_print("Given src path: "+self.file_path)
        self.keys = []                      # collection stores keys 
        self.values = []                    # collection stores values

        self.new = False                    # variable True if file was new
        self.integrity = False              # flag for checking integirity file
        self.fatal_error = False
        self.data_lines = []                # collection stores all data from file

        # starting procedure of file
        self.file_obj = self.file_procedure()

        # now we have lines in /data_lines/ 
        self.categorize()                   # categorizing lines from file
        self.dictionary = self.make_dictionary()
        self.log_print("integrity: "+str(self.integrity))
        self.data_print()                   # printing categorized data if debug = 1
        # if file is good for this version of the program
        if self.integrity:
            pass
        else:
            print(HEADER + "File is not supported by this version of the program")
            self.fatal_error = True

    # fucntion for checking if we have default setup
    def check_default_setup(self):
        if self.dictionary["%setup"] == "default":
            return True
        return False

    # function for returning data from dictionary
    def get_credentials(self):
        return [self.dictionary["%e-mail"],self.dictionary["%e-mail password"]]

    # function for preparing dictionary
    def make_dictionary(self):
        
        dictionary_toRet = {}

        for key in self.keys:
            dictionary_toRet[key] = self.values[self.keys.index(key)]

        return dictionary_toRet


    # function for counting signs in collections
    def counter(self,sign,collection):
        count = 0
        for obj in collection:
            if sign in obj:
                count+= 1

        return count

    # function for categorizing data output
    def categorize(self):
        amount = 0
        for line in self.data_lines:
            if (line[0] == "%"):
                self.keys.append(line[0:len(line)-1])
                amount+= 1
            else:
                self.values.append(line[0:len(line)-1])  

        if amount == self.counter("%",clear_file):
            self.integrity = True
        else:
            self.integrity = False

    # function for checking file and adding and opening default data
    def file_procedure(self):

        if ( self.existion_check() ):
            # file exists
            file_obj = open(self.file_path,"r")
            self.load_file(file_obj)
            return file_obj
        else:
            # file not exists
            file_obj = open(self.file_path,"w")
            self.write_to_file(1,"",file_obj)
            file_obj.close()
            file_obj = open(self.file_path,"r")
            self.load_file(file_obj)
            return file_obj

    # function for loading lines from file object
    def load_file(self,file_object):
        self.log_print("Loading file...")
        for line in file_object.readlines():
            self.data_lines.append(line)
        self.log_print("Loaded "+str(len(self.data_lines))+ " lines.")

    # function for writting data to given file object:
    # modes:
    #       1 - write new clear file with default data
    #       2 - write data to file given in the 'data' variable
    def write_to_file(self,mode,data,file_object):
        self.log_print("Writing data to file...")
        if mode == 1:
            for line in clear_file:
                self.log_print("    "+line)
                file_object.write(line+"\n")
        elif mode == 2:
            file_object.write(data+"\n")
        self.log_print("Data loaded to file.")
        file_object = open(self.file_path,"r")
        self.load_file(file_object)

    # fuction for loging information on screen
    def log_print(self,data_to_print):
        if self.debug == 1:
            print(HEADER + " " + data_to_print)

    # function for printing data from collections
    def data_print(self):
        if self.debug == 1:
            print("Data:")
            for key in self.keys:
                print("         "+key +" ("+self.values[self.keys.index(key)]+")")
            print("Dictionary:")
            print(str(self.dictionary))

    # function for checking if file exists
    def existion_check(self):
        self.log_print("Checking if file exists...("+self.file_path+")")
        if (os.path.exists(self.file_path)):
            self.log_print("File exists!")
            return 1
        self.log_print("File not exists.")
        return 0