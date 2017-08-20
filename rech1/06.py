# -*- coding:utf-8 -*-
def n_gram(s,n):
    result=[]
    for i in range(len(s)-n+1):
        result.append(s[i:i+n])
    return result

def main():
    s1="paraparaparadise"
    s2="paragraph"

    s1_gram=set(n_gram(s1,2))
    s2_gram=set(n_gram(s2,2))
    print(s1_gram.union(s2_gram))
    print(s1_gram.intersection(s2_gram))
    print(s1_gram.difference(s2_gram))
    print("se" in s1_gram)
    print("se" in s2_gram)


if __name__ == "__main__":
    main()
