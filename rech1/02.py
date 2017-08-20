# -*- coding:utf-8 -*-

def main():
    s1="パトカー"
    s2="タクシー"
    s3=""
    result="".join(i+j for i,j in zip(s1, s2))
    print(result)

    for i,j in zip(s1, s2):
        s3+=i+j
    print(s3)

if __name__ == "__main__":
    main()
