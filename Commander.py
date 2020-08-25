# by Jakub Wawak 08.2020
# all rights reserved
# kubawawak@gmail.com
import os
import subprocess
import platform
import time
"""
modes:
%getstatus
    - returns status of the system like system info, processes, ips, hardware data
%getnotify /command/
    - set same state to waiting to change and send response when it changed
%executecommand /command/
    - executes comand on machine and send response by e-mail
"""
version = "v1.0.0"
class Commander:

    # constructor
    def __init__(self,mode,raw_input):
        
        self.mode = mode
        self.user_input = raw_input
        self.user_name = os.getlogin()

        self.fatal_error = False
        self.notify_on = False
        self.notify_command = ""

        self.data_to_return  = ""

        if ( mode == "%getstatus" ):
            self.data_to_return = self.get_status()

        elif ( mode == "%getnotify" ):
            if len(raw_input.split(" ")) > 1:
                self.notify_on = True
                self.notify_command = raw_input.split(" ")[1]

        elif ( mode == "%executecommand" ):
            if self.user_input != "":
                self.data_to_return = self.execute_command(self.user_input)
            else:
                self.fatal_error = True

        else:
            self.fatal_error = True

    # function for wrap data from comander
    def wrapper(self):
        wrap = "Time of execution: "+ time.asctime() +"\n"
        wrap = wrap + "Data(\n"
        for line in self.data_to_return.split("\n"):
            wrap = wrap + line +"\n"

        wrap = wrap + ")end of data\n"
        return wrap

    # function for getting command execute
    def execute_command(self,command):
        return subprocess.getstatusoutput(command)[1]

    def get_status(self):
        s_string = ""

        for line in platform.uname():
            s_string = s_string + line

        return s_string 



    
