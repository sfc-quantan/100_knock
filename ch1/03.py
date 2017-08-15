import numpy as np
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

ss = s.split(" ")
print(len(ss))
count = len(ss)
a = np.arange(count)
for i in range(count):
    a[i] = len(ss[i])
print(a)
