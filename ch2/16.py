import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("-n", "--number", type=int)
args=parser.parse_args()
number=args.number

with open("hightemp.txt", "r") as f:
    datas=f.readlines()
    lines=len(datas)
    print(lines)
    devide=int(lines/number)
    print(devide)
    data=[]

    for i in range(number):
        data.append(datas[i*devide:(i+1)*devide])
    count=0
    #data=map(str,data)
    for i in data:
        count+=1
        with open('devi{}.txt'.format(count), 'w') as f2:
            for j in i:
                f2.writelines(j)


