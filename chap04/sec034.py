# coding: utf-8

import sys
import MeCab
import re
from pprint import pprint

def get_n_gram(N, line):
    n_gram_list = [[line[i+n] for n in range(N) if i+n < len(line)] for i in range(len(line))]
    n_gram_list = [ list for list in n_gram_list if len(list) == N]

    return n_gram_list

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

lines = get_mecab()

noun_phase_list = []
for line in lines:
    n_gram_list = get_n_gram(3, line)
    for n_gram in n_gram_list:
        filtered_n_gram = [word for word in n_gram if n_gram[0]["pos"] == "名詞" and n_gram[1]["base"] == "の" and n_gram[2]["pos"] == "名詞"]
        if len(filtered_n_gram) != 0:
            noun_phase_list.append("".join([word["surface"] for word in filtered_n_gram]))
    
pprint(noun_phase_list)