# coding: utf-8

s = "Atbash is a simple substitution cipher for the Hebrew alphabet."

def cipher(input):
    output = ""
    for li in input:
        output += chr(219-ord(li)) if li.islower() else li

    return output

s = cipher(s)
print(s)
s = cipher(s)
print(s)
