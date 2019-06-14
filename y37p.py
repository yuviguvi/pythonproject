t=int(input())
l=[int(i) for i in input().split()]
n=0
for i in range(1,t-1):
    if l[i]<l[i-1] and l[i]<l[i+1]:
        n+=1
    elif l[i]>l[i-1] and l[i]>l[i+1]:
        n+=1
print(n)
