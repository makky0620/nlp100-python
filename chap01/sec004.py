# coding: utf-8

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = s.split(" ")

index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
element_dict = {}

for i, word in enumerate(words):
    num = i+1
    if num in index:
        element_dict[num] = word[:1]
    else:
        element_dict[num] = word[:2]

print(element_dict)

