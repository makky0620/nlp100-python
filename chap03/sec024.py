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

for line in j["text"].split("\n"):
    media_line = re.search("^(ファイル):(.*?)\|", line)
    if media_line is not None:
        print(media_line.group(2))
    