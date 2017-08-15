# -*- coding: utf-8 -*-

s1 = "paraparaparadise"
s2 = "paragraph"

def ngram(input, n=2):
    a=[]
    for i in range(len(input)):
        a.append(input[i:i+n])
    return a

s1=ngram(s1,2)
s2=ngram(s2,2)
s1=set(s1)
s2=set(s2)
print(s1.union(s2))
print(s1.discard(s2))
print(s1.intersection(s2))

print("se" in s1)
print("se" in s2)

