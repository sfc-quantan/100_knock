from collections import Counter
with open('hightemp.txt', 'r') as f:
    datas=f.readlines()
col1=[data.split()[0] for data in datas]
# for data in datas:
#     col1.append(data.split()[0])
col2=Counter(col1).most_common()
for i,j in col2:
    print(i,j)

for i in col2:
    print(i)
