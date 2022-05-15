
import sys, subprocess, os.path
from os import path

if len(sys.argv) > 2:
    prefix = sys.argv[1]
    targetLanguage = sys.argv[2]
else:
    print("please provide the prefix and target language")
    exit(-1)

print("## subtitles, prefix: " + prefix + ", targetLanguage: " + targetLanguage)

subtitlesFile = "resources/" + prefix + "-" + targetLanguage + ".srt"
sbtOutputFile = "build/" + prefix + "-" + targetLanguage + ".mp4"
if not path.exists(sbtOutputFile):
    os.system("handbrakecli -i build/" + prefix + ".mp4 -o " + sbtOutputFile + " --srt-file " + subtitlesFile + " --srt-codeset UTF-8 --srt-burn")
