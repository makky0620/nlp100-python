# coding: utf-8

from xml.etree import ElementTree as ET
from pprint import pprint

tree = ET.parse("../../assets/nlp.txt.xml")
root = tree.getroot()

tokens = root.findall(".//token")

for token in tokens:
    if token.find("NER").text == "PERSON":
        print(token.find("word").text)
