t=int(input())
s=list()
for i in range(t):
    b=input().split()
    b=[int(d) for d in b]
    for j in b:
        s.append(j)
s.sort()
for i in s:
    print(i,end=" ")
