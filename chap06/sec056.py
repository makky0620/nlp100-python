# coding: utf-8

from xml.etree import ElementTree as ET
from pprint import pprint

tree = ET.parse("../../assets/nlp.txt.xml")
root = tree.getroot()

position_map = {}
remention2mention = {}

sentences = root.findall("document/sentences/sentence")
coreferences = root.findall("document/coreference/")


for coreference in coreferences:
    key = ""
    value = ""
    for mention in coreference:
        if mention.get("representative"):
            key = mention.find("text").text
        else:
            value = mention.find("text").text
            sentence_id = mention.find("sentence").text
            start_end = [int(mention.find("start").text),
                         int(mention.find("head").text),
                         mention.find("text").text
                         ]
            if sentence_id in position_map:
                position_map[sentence_id].append(start_end)
            else:
                position_map[sentence_id] = start_end

    remention2mention[key] = value

pprint(remention2mention)

for key in position_map.keys():
    for sentence in sentences:
        tokens = sentence.find("tokens")
        if sentence.get("id") == key:
            words = [token.find("word").text for token in tokens]
            origin_words = words[position_map[key][0]:position_map[key][1]]
            del words[position_map[key][0]:position_map[key][1]]
            pprint(words)
            words.insert(position_map[key][0],
                         "{}({})".format(remention2mention[position_map[key][2]], position_map[key][2]))
            # print(" ".join([tokens[i].find("word").text
            #                 for i in range(position_map[key][0]-1, position_map[key][1])]))
        else:
            pass
            # print(" ".join([token.find("word").text for token in tokens]))

"""
    25
    1 start
    3 end
    2 head
"""
