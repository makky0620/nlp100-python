# coding: utf-8

import sys

f = open(sys.argv[1])
N = int(sys.argv[2])

lines = f.readlines()

split_num = int(len(lines)/N)


for index, line in enumerate(lines):
    # print(line.rstrip())
    print(index+1, split_num)
    if (index+1) % split_num == 0 and (index+1) / split_num < N:
        print()