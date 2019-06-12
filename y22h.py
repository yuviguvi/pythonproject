t=int(input())
n=[int(i) for i in input().split()]
prod=1
m=[]
for i in n:
    prod=prod*i
for i in n:
    m.append(prod//i)
print(*m)
