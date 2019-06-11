from itertools import permutations
t=input()
s=permutations(t)
l=[]
x=(-1)
a="abcdefghijklmnopqrstuvwxyz"
if a==t:
  print(t)
elif t==a[::-1]:
  print("-1")
else:
    t=tuple(t)
    for i in s:
        l.append(i)
    for i in l:
        if i>t:
            x=i
            break

    for i in l:
        if i>s and i<x:
            x=i

    if x==-1:
        print("-1")
    else:
        for i in x:
            print(i,end="")
