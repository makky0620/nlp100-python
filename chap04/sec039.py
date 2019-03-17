# coding: utf-8

import sys
import MeCab
import re
import collections
from pprint import pprint
import matplotlib.pyplot as plt



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

word_to_count = {}
word_list = []

for line in lines:
    word_list += [word['surface'] for word in line]

count = collections.Counter(word_list)
lst_commons = count.most_common()

freq = [item[1] for item in lst_commons]
freq_count = collections.Counter(freq)
value = [item for item in freq_count.values()]

plt.title('両対数グラフ')
plt.xlabel('単語の種類数') 
plt.ylabel('出現頻度') 
plt.loglog(range(len(value)), sorted(value, key=lambda x: x, reverse=True))
plt.show()