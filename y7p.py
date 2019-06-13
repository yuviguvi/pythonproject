import math
s=int(input())
t=math.log10(s)/math.log10(2)
if math.ceil(t)==math.floor(t):
    print(0)
else:
    m=(s-1)//2
    n=m*2
    print(s-n)
