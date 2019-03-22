# coding: utf-8

from xml.etree import ElementTree as ET
from pprint import pprint

tree = ET.parse("../../assets/nlp.txt.xml")
root = tree.getroot()

position_map = {}
remention2mention = {}

sentences = root.findall("document/sentences/sentence")
coreferences = root.findall("document/coreference/")

sentences = [[t.find('word').text for t in s.findall('tokens/*')]
            for s in root.find('document/sentences')]

coreferences = [
    [
        [
            int(mention.find('sentence').text)-1,
            int(mention.find('start').text)-1, 
            mention.find('text').text.split(' ')
        ] 
        for mention in coreference.findall('mention')]
    for coreference in root.findall('document/coreference/*')]

for coreference in coreferences:
    for mention in coreference[1:]:
        text = [ 
            sentences[mention[0]][:mention[1]] +
            coreference[0][2] + 
            ["("] + mention[2] + [")"] +
            sentences[mention[0]][mention[1]+len(mention[2]):]
            ]
        for word in text:
            print(" ".join(word))





"""
    25
    1 start
    3 end
    2 head
"""
