# -*- coding: utf-8 -*-

import sys
args=sys.argv
args=args[1]
args=int(args)
with open('hightemp.txt', 'r') as f:
    datas=f.readlines()
for i in range(args):
    print(datas[i].rstrip('\n'))


