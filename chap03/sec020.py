# coding: utf-8

import sys
import json
from pprint import pprint

f = open(sys.argv[1])
lines = f.readlines()

for line in lines:
    j = json.loads(line)
    if j["title"] == "イギリス":
        print(j["text"])