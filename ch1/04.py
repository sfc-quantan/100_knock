s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

s=s.split(' ')
a={}
for i in range(len(s)):
    if i==1 or i==5 or i==6 or i==7 or i==8 or i==9 or i==15 or i==16 or i==19:
        a[i]=s[i][0:2]
    else:
        a[i]=s[i][0]

for i in range(len(a)):
    print(a[i])

