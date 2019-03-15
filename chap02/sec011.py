# coding: utf-8

import sys

f = open(sys.argv[1])
lines = f.read()

print(lines.replace("\t", " "))

f.close()
