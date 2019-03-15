# coding: utf-8

import sys
import json
from pprint import pprint

def get_json(title):
    f = open(sys.argv[1])
    lines = f.readlines()

    for line in lines:
        j = json.loads(line)
        if j["title"] == title:
            f.close()
            return j

j = get_json("イギリス")
category_list = [line for line in j["text"].split("\n") if "Category" in line]
print(category_list)    
