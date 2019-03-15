# coding: utf-8

import sys
import MeCab
import re
from pprint import pprint

f = open(sys.argv[1], encoding="utf-8")
sentence = []
lines = []

for line in f:
    words = re.split("\t|,|\n", line)
    if words[0] == "EOS":
        if sentence:
            lines.append(sentence)
            sentence = []
        continue
    
    sentence.append({
        "surface": words[0],
        "base": words[7],
        "pos": words[1],
        "pos1": words[2]
    })

    pprint(lines)



    
