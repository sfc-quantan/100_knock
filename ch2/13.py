with open('col1.txt', 'r') as f1:
    with open('col2.txt', 'r') as f2:
        data1, data2=f1.readlines(), f2.readlines()
        datas=[]
        for i, j in zip(data1, data2):
            datas.append(i.rstrip('\n')+ "\t"+j)

with open("merge.txt", 'w') as merge:
    merge.writelines(datas)


    
