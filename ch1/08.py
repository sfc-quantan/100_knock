# -*- coding: utf-8 -*-
str="I am now studying Python"
str2="Python is a Programming language"

def cipher(input):
    r=""
    for i in input:
        if(i.islower):
            r+=chr(219-ord(i))
        else:
            r+=i
    return r

ch=cipher(str)
print(ch)
print(cipher(ch))

def cipher2(input):
    r=""
    for i in input:
        r+= chr(219-ord(i)) if i.islower else i
    return r

ch=cipher2(str2)
print(ch)
print(cipher2(ch))
