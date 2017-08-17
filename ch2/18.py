with open('hightemp.txt', 'r') as f:
    datas = f.readlines()

kion=[]
for data in datas:
    kion.append(data.split()[2])
for i in sorted(kion):
    print(i)
print(kion)
