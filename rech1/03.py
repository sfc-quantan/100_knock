# -*- coding:utf-8 -*-

def main():
    s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    ss=s.split()
    result=[]
    for i in ss:
        print(i)
        result.append(len(i))
    print(result)

if __name__ == "__main__":
    main()
