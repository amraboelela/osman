# importing the requests library
import sys, subprocess, requests

if len(sys.argv) > 2:
    filename = sys.argv[1]
    targetLanguage = sys.argv[2]
else:
    print("please provide the file name and the target language")
    exit(-1)

# api-endpoint
URL = "https://translation.googleapis.com/language/translate/v2"
from translation_key import *

file = open(filename)
sourceLanguage = filename[len(filename)-6:len(filename)-4]
lines = file.read().splitlines()
paragraph = ""
for line in lines:
    if "-->" in line:
        if len(paragraph) > 0:
            paragraph = paragraph[:len(paragraph)-2]
            PARAMS = {'key':key, 'q':paragraph, 'source':sourceLanguage, 'target':targetLanguage}
            r = requests.get(url = URL, params = PARAMS)
            data = r.json()
            translatedText = data['data']['translations'][0]['translatedText'].replace('-','').replace("&#39;","'").replace("&quot;","'").replace("'il","'ll").replace(" gas "," conquest ").replace("Come on God","Allah is Ever-Living").replace("Sorry.","Sir.")
            try:
                print(translatedText.encode('utf8'))
                print
            except Exception as error:
                print("error: " + str(error) + " line: " + line)

        print line
        paragraph = ""
    else:
        paragraph = paragraph + line.replace('-','').replace("!","").replace(".","") + ". "

PARAMS = {'key':key, 'q':paragraph, 'source':sourceLanguage, 'target':targetLanguage}
r = requests.get(url = URL, params = PARAMS)
data = r.json()
translatedText = data['data']['translations'][0]['translatedText'].replace('-','').replace("&#39;","'").replace("&quot;","'").replace("'il","'ll")
try:
    print(translatedText.encode('utf8'))
    print
except Exception as error:
    print("error: " + str(error) + " line: " + line)

file.close()
