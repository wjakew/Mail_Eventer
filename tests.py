import File_Reader as f
import Mail_Getter as mg
import Composer as comp
import sys
import time

# comment/uncomment to change console to file

#FILENAME = time.asctime().replace(" ","_") + "_TEST.txt"
#sys.stdout = open(FILENAME, "w")

# actual tests
print("Debug data:")
print("---------------------------------------")
f.File_Reader(str(sys.argv[1]), int(sys.argv[2]))
print("---------------------------------------")
coposer_tes_obj = comp.Composer("%time has come", 1)
print("---------------------------------------")
test_object = mg.Mail_Getter("main.tes.instruments@gmail.com", "minidysk", 1)
test_object.run()
# end of actual tests
# sys.stdout.close()
