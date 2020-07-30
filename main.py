# by Jakub Wawak 07.2020
# all rights reserved
# kubawawak@gmail.com
import Mail_Getter as mg

# data
version = "v.1.0.0"


# main part of the program

t = mg.Mail_Getter("main.tes.instruments@gmail.com","minidysk")
t.run()

for e in t.mail_object_list:
    e.simple_show()