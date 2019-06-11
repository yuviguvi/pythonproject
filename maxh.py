a=int(input())
z=0
t=[int(a) for a in input().split()]
for i in range(0,len(t)):
    if t.count(t[i])>z:
        z=t.count(t[i])
        x=t[i]
print(x)
