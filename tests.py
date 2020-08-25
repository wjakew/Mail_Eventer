# by Jakub Wawak 08.2020
# all rights reserved
# kubawawak@gmail.com
import File_Reader as f
import Mail_Getter as mg
import Mail_Getter2 as mgii
import Mail_Getter3 as mgiii
import Commander as com
import Composer as comp
import Response_Object as ro
import Mail_Object as mo
import Mail_Sender as ms
import Parser as p
import sys
import time

# comment/uncomment to change console to file

#FILENAME = time.asctime().replace(" ","_") + "_TEST.txt"
#sys.stdout = open(FILENAME, "w")

# actual tests
print("Debug data:")
print("---------------------------------------")
#mail = mo.Mail_Object("kubawawak@gmail.com","test","%getip now")
#conf = f.File_Reader("test.txt",1)
#responser = ro.Response_Object(mail,conf)
#responser.response()
print("---------------------------------------")
#sender = ms.Mail_Sender("kubawawak@gmail.com","test kurwa")
#print(sender.send())
print("---------------------------------------")
#fil = f.File_Reader(str(sys.argv[1]), int(sys.argv[2]))
#print(str(fil.get_credentials()))
print("---------------------------------------")
#coposer_tes_obj = comp.Composer("%getip", 1)
#print(coposer_tes_obj.compose())
print("---------------------------------------")
#test_object = mg.Mail_Getter("main.tes.instruments@gmail.com", "minidysk", 1)
#test_object.run()
#test_object2 = mgii.Mail_Getter2("main.tes.instruments@gmail.com","minidysk",1)
#data = test_object2.fetch()
#for i in range(0, len(data)):
#    test_parser = p.Parser(data[i])
#    test_parser.run()
#    test_parser.show()
#    test_parser.
#    #print(test_parser.get_content())
#    print(test_parser.get_from())
#    #test_parser.get_mail_object().simple_show()
print("---------------------------------------")
#test_parser = p.Parser(data[1])
#test_parser.run()
#print(test_parser.get_from())
print("---------------------------------------")
#c = com.Commander("%executecommand","ls")
#print(c.wrapper())
print("---------------------------------------")
#test_object = mgiii.Mail_Getter3("main.tes.instruments@gmail.com","minidysk",1)
#test_object.fetch()
print("---------------------------------------")