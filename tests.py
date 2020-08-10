import File_Reader as f
import Mail_Getter as mg
import Composer as comp
import Response_Object as ro
import Mail_Object as mo
import Mail_Sender as ms
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
#print("---------------------------------------")
#sender = ms.Mail_Sender("kubawawak@gmail.com","test kurwa")
#print(sender.send())
#print("---------------------------------------")
#fil = f.File_Reader(str(sys.argv[1]), int(sys.argv[2]))
#print(str(fil.get_credentials()))
#print("---------------------------------------")
#coposer_tes_obj = comp.Composer("%time has come", 1)
#print("---------------------------------------")
test_object = mg.Mail_Getter("main.tes.instruments@gmail.com", "minidysk", 1)
test_object.run()
# end of actual tests
# sys.stdout.close()
