'''
s="I am an NLPer"
ss=s.split(' ')
s=ngram(s,2)
print(s)
ss=ngram(ss,2)
print(ss)

s="ab cde fghi jklm nopq rstuvwxyz"

def ngram(input, n):
    a={}
    for i in range(len(input)):
        a[i]=input[i:i+n]
    b=[]
    for i,j in a.items():
        b.append(j)

    return b

ss=ngram(s,2)
print(ss)

ss=s.split(' ')
ss=ngram(ss, 2)
print(ss)

'''

def ngram(input, n):
    a=[]
    for i in range(len(input)):
        a.append(input[i:i+n])
    return a

s="I am an NLPer"
ss=ngram(s, 2)
print(ss)
ss=s.split(' ')
ss=ngram(ss, 2)
print(ss)

