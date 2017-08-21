# -*- coding:utf-8 -*-
import random
def change(text):
    words = text.split(" ")
    result=[]
    for word in words:
        if len(word)<4:
            result.append(word)
        else:
            temp=list(word[1:-1])
            random.shuffle(temp)
            result.append(word[0] + "".join(temp) + word[-1])

    return " ".join(result)


def main():
    sentence="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words=sentence.split()
    result=""
    for word in words:
        if len(word) > 4:
            temp=list(word[1:-1])
            random.shuffle(temp)
            result+=word[0] + "".join(temp) + word[-1]+" "
        else:
            result+=word+" "
    
    print(result)

    print(change(sentence))





if __name__ == "__main__":
    main()
