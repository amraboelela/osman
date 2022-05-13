
import sys, subprocess, os.path
from os import path
import durationLimit

if len(sys.argv) > 3:
    prefix = sys.argv[1]
    targetLanguage = sys.argv[2]
    postfix = sys.argv[3]
else:
    print("please provide the prefix, target language, and prefix")
    exit(-1)

print("## subtitles, prefix: " + prefix + ", targetLanguage: " + targetLanguage + ", postfix: " + postfix)

sourceFilePath = "build/" + prefix + "-tr.vtt"
targetFilePath = "build/" + prefix + "-" + targetLanguage + ".vtt"
subtitlesPath = "resources/" + prefix + ".srt"

sourceFile = open(sourceFilePath)
sourceLines = sourceFile.read().splitlines()
targetFile = open(targetFilePath)
targetLines = targetFile.read().splitlines()
targetFile.close()
sourceFile.close()

def timeString(timeFloat):
    milliSeconds = int(timeFloat * 1000 % 1000)
    totalSeconds = int(timeFloat)
    seconds = int(totalSeconds % 60)
    totalMinutes = int(totalSeconds / 60)
    minutes = int(totalMinutes % 60)
    hours = int(totalMinutes / 60)
    return str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2) + "," + str(milliSeconds).zfill(3)

#quit()
sbtFile = "build/" + prefix + "-sbt-" + postfix + ".mp4"
if not path.exists(sbtFile):
    os.system("handbrakecli -i build/" + prefix + "-" + postfix +".mp4 -o " + sbtFile + " --srt-file resources/" + prefix + ".srt --srt-codeset UTF-8 --srt-burn")
