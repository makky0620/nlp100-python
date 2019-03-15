# coding: utf-8

import sys

f = open(sys.argv[1])

lines = f.readlines()

col3 = sorted(lines, key=lambda x: x.split()[2], reverse=True)

print("".join(col3))