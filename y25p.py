t=int(input())
l=list(map(int,input().split()))
s=[]
a=1
for i in range(t-1):
    if l[i]<l[i+1]:
        a+=1
    else:
        s.append(a)
        a=1
s.append(a)
print(max(s))
