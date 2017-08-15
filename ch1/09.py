# -*- coding: utf-8 -*-
import random
str="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
str=str.split(' ')
print(type(str))
word=[]
for i,s in enumerate(str):
    if len(s)>=4:
        
        word_mix=list(s[1:-1])
        random.shuffle(word_mix)
        word.append(s[0] +"".join( word_mix) + s[-1])
    else:
        pass
    
print(word)

