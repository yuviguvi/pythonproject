t,s=map(int,input().split())
n=[int(x) for x in input().split()]
z=0
for i in range(0,len(n)):
    if n[i]<=s:
        z+=1
print(z)
