s=int(input())
t=[]
for i in range(0,s):
    for j in range(i,s):
        t.append("1")
    print(*t)
    t=[]
