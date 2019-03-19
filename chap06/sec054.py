# coding: utf-8

from xml.etree import ElementTree as ET
from pprint import pprint

tree = ET.parse("../../assets/nlp.txt.xml")
root = tree.getroot()

tokens = root.findall(".//token")

for token in tokens:
    word = token.find("word").text
    lemma = token.find("lemma").text
    pos = token.find("POS").text
    if word not in ".,:''?``":
        print(word, lemma, pos)
