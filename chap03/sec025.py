# coding: utf-8

import sys
import json
import re

def get_json(title):
    f = open(sys.argv[1])
    lines = f.readlines()

    for line in lines:
        j = json.loads(line)
        if j["title"] == title:
            f.close()
            return j

j = get_json("イギリス")
info_dict = {}

for line in j["text"].split("\n"):
    info_line = re.search("^\|(.*?)\s=\s(.*)", line)
    if info_line is not None:
        info_dict[info_line.group(1)] = info_line.group(2)
        
for key, value in sorted(info_dict.items(), key=lambda x: x[1]):
    print(key, value)