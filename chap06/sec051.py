# coding: utf-8

import re
from pprint import pprint

from sec050 import nlp_lines


def nlp_words():
    for line in nlp_lines():
        words = line.split(" ")
        words.append(" ")
        for word in words:
            word = word.rstrip(".,;:?!")
            yield word


for word in nlp_words():
    print(word)
