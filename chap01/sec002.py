# coding: utf-8

s1 = "パトカー"
s2 = "タクシー"
s3 = ""
for c1, c2 in zip(s1, s2):
    s3 += c1 + c2

print(s3)