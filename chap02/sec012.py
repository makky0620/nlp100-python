# coding: utf-8

import sys

def save_file(filename, col):
    with open(filename, "w") as writer:
        writer.writelines(col)

f = open(sys.argv[1])
lines = f.readlines()

col1 = [line.split()[0]+"\n" for line in lines]
col2 = [line.split()[1]+"\n" for line in lines]

print(col1)
print(col2)

save_file("col1.txt", col1)
save_file("col2.txt", col2)

f.close()