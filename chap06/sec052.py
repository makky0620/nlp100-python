# coding: utf-8

from stemming.porter2 import stem

from sec051 import nlp_words


for word in nlp_words():
    print(word, stem(word))
