# by Jakub Wawak 07.2020
# all rights reserved
# kubawawak@gmail.com

import os

# supported file structure:
"""
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
clear_file = ["%version","v1.0.0","%login","admin",
                "%user_password","admin1234","%e-mail","","%email password",""]
# object for mantaining file
class File_Reader:

    def __init__(self,src):

        self.file_path = src                # path in string pointing on file
        
        self.keys = []                      # collection storing keys 
        self.values = []                    # collection storing values
        
        self.file_obj = open(src,"r")       # file object

        self.new = False                    # variable True if file was new

        if self.existion_check() == 1:
            self.new = True

    # function for writting data to files:
    
    def write_file(self,mode):


    def make_file(self):
        if self.new:
            file_obj



    def existion_check(self):
        if (os.path.exists(self.file_path)):
            return 1
        return 0