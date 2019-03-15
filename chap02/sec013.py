# coding: utf-8

f1 = open("col1.txt")
f2 = open("col2.txt")

lines1 = f1.readlines()
lines2 = f2.readlines()

output = [lines1[i].rstrip() + "\t" + lines2[i] + "\n" for i in range(len(lines1))]

with open("col12.txt", "w") as writer:
    writer.writelines(output)

f1.close()
f2.close()