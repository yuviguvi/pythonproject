import math
import functools
t,s=map(int,input().split())
l=[int(i) for i in input().split()]
for i in range(s):
    c,d=map(int,input().split())
    t=functools.reduce(math.gcd,l[c-1:d])
    print(t)
