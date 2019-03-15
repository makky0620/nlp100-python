# coding: utf-8

import sys

f = open(sys.argv[1])

lines = f.readlines()

col1 = [col.split()[0] for col in lines]

count_dict = {}
for col in col1:
    if col in count_dict:
        count_dict[col] += 1
    else:
        count_dict[col] = 1

sorted_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

for data in sorted_list:
    print(data[0], data[1])