with open('hightemp.txt', 'r') as f:
    datas=f.readlines()
    
data=[]
data2=[]
for i in datas:
    data.append(i.split()[0]+"\n")
    data2.append(i.split()[1]+"\n")

print(data,data2)
with open("col1.txt", "w") as w:
    w.writelines(data)
with open("col2.txt", "w") as w:
    w.writelines(data2)

