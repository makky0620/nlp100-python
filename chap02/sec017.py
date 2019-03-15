# coding: utf-8

import sys

f = open(sys.argv[1])
lines = f.readlines()

col1 = [col.split()[0] for col in lines]
print(set(col1))