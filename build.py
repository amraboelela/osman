# importing the requests library
import sys, os 

if len(sys.argv) > 2:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
else:
    print("please enter the first episode number and last episode numer")
    exit(-1)

os.system("./download osman")
exit(0)
for n in range(a, b+1):
    prefix = "osman-" + str(n).zfill(2)
    os.system("./buildEpisode " + prefix)
