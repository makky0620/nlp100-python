# coding: utf-8

import re
from pprint import pprint
import sys


def nlp_lines():
    pattern = r'(^.*?[\.|;|:|\?|!])(\s)([A-Z].*)'
    with open('../../assets/nlp.txt', 'r') as input:
        for line in input:
            line = line.strip()
            while len(line) > 0:
                match = re.match(pattern, line)
                if match:
                    yield match.group(1)
                    line = match.group(3)
                else:
                    yield line
                    line = ''


for line in nlp_lines():
    print(line)
