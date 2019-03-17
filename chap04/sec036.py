# coding: utf-8

import sys
import MeCab
import re
import collections
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

lines = get_mecab()

word_to_count = {}
word_list = []

"""
    pattern 1
"""
# for line in lines:
#     word_list = [word['surface'] for word in line]
#     for word in word_list:
#         if word in word_to_count:
#             word_to_count[word] += 1
#         else:
#             word_to_count[word] = 1

# pprint(sorted(word_to_count.items(), key=lambda x: x[1], reverse=True)[:10:])

"""
    pattern 2
"""
for line in lines:
    word_list += [word['surface'] for word in line]

count = collections.Counter(word_list)
lst_commons = count.most_common()

print(lst_commons[:10:])
