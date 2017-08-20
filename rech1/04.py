# -*- coding:utf-8 -*-

def main():
    s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    count=[1, 5, 6, 7, 8, 9, 15, 16, 19]
    ss=s.split()
    result=[]
    for i,j in enumerate(ss):
        if i+1 in count:
            result.append(j[0])
        else:
            result.append(j[0:2])
    
    print(result)
    result=map(str,result)
    print("".join(result))
    print(result)
    for i in result:
        
        print(i)




if __name__ == "__main__":
    main()
