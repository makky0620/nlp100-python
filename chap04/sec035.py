# coding: utf-8

import sys
import MeCab
import re
from pprint import pprint


def get_mecab():
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

    return lines

def get_noun_phases(line):
    noun_phases = []
    noun_phase = ""
    for word in line:
        if word["pos"] == "名詞":
            noun_phase += word["surface"]
        else:
            if len(noun_phase) != 0:
                noun_phases.append(noun_phase)
                noun_phase = ""

    return noun_phases

lines = get_mecab()

noun_phases = []

for line in lines:
    noun_phases = noun_phases + get_noun_phases(line)
   
pprint(sorted(noun_phases, key=lambda x: len(x)))
