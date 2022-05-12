# importing the requests library
import sys, os 

if len(sys.argv) > 4:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    sourceLanguage = sys.argv[3]
    targetLanguage = sys.argv[4]
else:
    print("please enter the first episode number, last episode numer, source lnguage, and target language")
    exit(-1)

os.system("./download osman")
#exit(0)
for n in range(a, b+1):
    prefix = "osman-" + str(n).zfill(3)
    os.system("./buildEpisode " + prefix + " " + sourceLanguage + " " + targetLanguage)
