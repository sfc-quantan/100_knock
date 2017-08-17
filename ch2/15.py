# -*- coding: utf-8 -*-

import argparse
parser = argparse.ArgumentParser(description="")
parser.add_argument("-n","--number", type=int)
args=parser.parse_args()
number=args.number
number=-number
print(number)
with open('hightemp.txt', 'r') as f:
    datas=f.readlines()

for data in datas[number:]:
    print(data,end='')
