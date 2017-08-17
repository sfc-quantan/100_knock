with open('hightemp.txt', "r") as f:
    datas=f.readlines()

col1=[]
for i in datas:
    col1.append(i.split()[0])
col1=set(col1)
for i in col1:
    print(i)





