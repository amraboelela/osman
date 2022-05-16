
import sys, subprocess, os.path
from os import path

if len(sys.argv) > 2:
    prefix = sys.argv[1]
    targetLanguage = sys.argv[2]
else:
    print("Please provide the prefix and target language")
    exit(-1)

#print("## subtitles, prefix: " + prefix + ", targetLanguage: " + targetLanguage)

prefixParts = prefix.split("-")
name = prefixParts[0]
if name == "osman":
    subtitlesFile = "resources/" + prefix + "-" + targetLanguage + ".srt"
    language = "English"
    if targetLanguage == "ar":
        language = "Arabic"
    targetName = "Kurulus Osman Season 3 Episode 90 - 92 With " + language + " Subtitles"
    outputFile = "build/" + targetName + "/" + prefix + ".mp4"
    if not path.exists(outputFile):
        print("## subtitles, generating: " + outputFile)
        escapedOutputFile = outputFile.replace(" ","\ ")
        os.system("handbrakecli -i build/" + prefix + ".mp4 -o " + escapedOutputFile + " --srt-file " + subtitlesFile + " --srt-codeset UTF-8 --srt-burn")
