# coding: utf-8

from xml.etree import ElementTree as ET
from pprint import pprint

tree = ET.parse("../../assets/nlp.txt.xml")
root = tree.getroot()

words = root.findall(".//word")

for word in words:
    print(word.text)
