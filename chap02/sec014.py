# coding: utf-8

import sys

f = open(sys.argv[1])
N = int(sys.argv[2])

lines = f.readlines()

for line in lines[:N]:
    print(line.rstrip())
