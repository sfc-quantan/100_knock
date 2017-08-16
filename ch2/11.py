# -*- coding: utf-8 -*-

with open('hightemp.txt', 'r') as f:
    datas=f.readlines()
    print(type(datas))
    lines=[]
    for data in datas:
        print(data.replace("\t", ""), end="")
        data=data.replace('\t', ' ')
        lines.append(data)

for line in lines:
    print(line, end="")
