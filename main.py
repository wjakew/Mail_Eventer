# by Jakub Wawak 07.2020
# all rights reserved
# kubawawak@gmail.com
import Response_Action as ra
import File_Reader as fr
import sys
import time
# data
version = "v.1.0.0B4"
HEADER = "Main_Eventer"
CONFIGURATION_FILE = "configuration_me.txt"
# main part of the program
"""
general idea of the main file:
eq execution:

python3 main.py configuration_file.txt /debuginfo/
"""
class Main:

    # constructor
    def __init__(self):
        self.print_welcome()
        self.configuration_file = None
        self.debug = 1

        # python3 main.py help
        if len(sys.argv) == 2:
            if sys.argv[1] == "help":
                self.print_help()
            else:
                print("Wrong argumenst see help.")

        # python3 main.py configuration_file.txt 1/0
        elif len(sys.argv) == 3 :
            self.debug = int(sys.argv[2])
            self.configuration_file = self.load_configuration(str(sys.argv[1]))

            #---------------------------------------MAIN CODE OF THE PROGRAM

            self.print_data()

            if self.ask_double("You sure to use that data?"):
                print("Using the data...")
                # now we have data and sure to start procedure

                while(True):
                    print("Starting : "+ time.asctime())
                    responder = ra.Response_Action(self.configuration_file,self.debug)
                    responder.run()
                    print("Stopped : "+ time.asctime())
                    print("Going to sleep for 120 s")
                    time.sleep(120)
 
            else:
                print("Cancelled")


            #---------------------------------------END OF THE MAIN CODE
            
        # python3 main.py
        else:
            print("Wrong arguments see help.")

    # function for load configuration
    def load_configuration(self, src_configuration):

        return fr.File_Reader(src_configuration,self.debug)


#-----------------UI PRINT FUNCTION
    # function printing welcome prompt
    def print_welcome(self):
        print("Mail_Eventer "+version)
        print("Echo from user input:")
        self.print_user_input()
    # function for showing user help
    def print_help(self):
        print("Help")

    # function for showing data of the main module
    def print_data(self):
        print("Debug: "+str(self.debug))
        print("Configuration file path: "+str(self.configuration_file.file_path))

    def print_user_input(self):
        print("--------------------------------")
        print("Amount: "+str(len(sys.argv)))
        for i in range(0,len(sys.argv)):
            print(str(i)+" "+str(sys.argv[i]))
        print("--------------------------------")
#----------------UI INTERACTION FUNCTION
    # function for getting user sure
    def ask_double(self,prompt):
        user_input = input(prompt + "(y/n)")
        return user_input == "y"

#-------------END OF FILE START OF THE PROGRAM
Main()
    