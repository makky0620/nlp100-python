# coding: utf-8

import sys
import json
import re
import requests
from pprint import pprint

def get_json(title):
    f = open(sys.argv[1])
    lines = f.readlines()

    for line in lines:
        j = json.loads(line)
        if j["title"] == title:
            f.close()
            return j

def json_search(json_data):
    ret_dict = {}
    for k, v in json_data.items():
        if isinstance(v, list):
            for e in v:
                ret_dict.update(json_search(e))
        elif isinstance(v, dict):
            ret_dict.update(json_search(v))
        else:
            ret_dict[k] = v
    pprint(ret_dict)
    return ret_dict



j = get_json("イギリス")
info_dict = {}

for line in j["text"].split("\n"):
    info_line = re.search("^\|(.*?)\s=\s(.*)", line)
    if info_line is not None:
        filtered_value = re.sub("'{2,5}", "", info_line.group(2))
        filtered_value = re.sub("\[{2}([^|\]]+?\|)*(.+?)\]{2}", "\2", filtered_value)
        filtered_value = re.sub("\{{2}.+?\|.+?\|(.+?)\}{2}", "\2", filtered_value)
        filtered_value = re.sub("\<.*?>", "\1", filtered_value)
        filtered_value = re.sub("\[.*?\]", "", filtered_value)
        info_dict[info_line.group(1)] = filtered_value
        
url = "https://en.wikipedia.org/w/api.php"
payload = {"action": "query",
           "titles": "File:{}".format(info_dict[u"国旗画像"]),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

json_data = requests.get(url, params=payload).json()
print(json_search(json_data)["url"])
