# -*- coding:utf-8 -*-

def n_gram(n,s):
    result=[]
    for i in range(len(s)-n+1):
        result.append(s[i:i+n])
    return result



def main():
    s="I am an NLPer"
    ss=s.split()
    print(n_gram(2,s))
    print(n_gram(2,ss))


if __name__ == "__main__":
    main()
