# -*- coding:utf-8 -*-
def kion(x, y, z):
    s="{}時の{}は{}".format(x,y,z)
    return s
def main():
    x=12
    y="気温"
    z=22.4
    s1=kion(x, y, z)
    print(s1)
    

if __name__ == "__main__":
    main()
