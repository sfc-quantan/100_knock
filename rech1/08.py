# -*- coding:utf-8 -*-
def cipher(text):
    result=""
    for i in text:
        if i.islower() == True:
            i = chr(219- ord(i))
            result+=i
        else:
            result+=i
    return result

def cipher2(text):
    result=""
    for char in text:
        result+= chr(219-ord(char)) if char.islower() == True else char
    return result


def main():
    s="The New York Times: Find breaking news, multimedia, reviews & opinion on Washington"
    s=cipher(s)
    print(s)
    s=cipher(s)
    print(s)
    s=cipher2(s)
    print(s)
    print(cipher2(s))

    

if __name__ == "__main__":
    main()
