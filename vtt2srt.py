#!/usr/bin/python
import sys
import re

args = sys.argv
_if = False
_of = False

try:
        _if = str(args[1])
except:
        print "No input file defined, exiting."
        exit(0)

try:
        _of = str(args[2])
except:
        pass

srt_content = ""
with open(_if,"r") as vtt_file:
        vtt_content = vtt_file.read()
        sections = vtt_content.split("\n\n")
        count = 1
        for section in sections:
                values = re.search("([0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}) --> ([0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3})\n(.*)",section,re.MULTILINE|re.I|re.DOTALL)
                if values:
                        srt_content += str(count) + "\n"
                        srt_content += values.group(1).replace(".",",") + " --> " + values.group(2).replace(".",",") + "\n"
                        srt_content += values.group(3) + "\n\n"
                        count = count + 1

if _of:
        with open(_of,"w") as srt_file:
                srt_file.write(srt_content)
                srt_file.flush()
        print "Done, wrote " + _of
else:
        print srt_content
