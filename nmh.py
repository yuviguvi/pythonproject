a=int(input())
n=[int(x) for x in input().split()]
t=[]
m=sorted(n)
while len(m)!=0:
    if len(m)!=1:
        t.append(m[-1])
        t.append(m[0])
        m.remove(m[0])
        m.remove(m[-1])
    else:
        t.append(m[0])
        m.remove(m[0])
print(*t)
