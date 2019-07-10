def n(l):
        n1=1
        for x in range(0,len(l)-1):
                if l[x]!=l[x+1]:
                        n1=n1+1
                else:
                    break
        return n1
num=int(input())
l=list(map(int,input().split()))
for x in range(0,len(l)):
        if l[x]>0:
                l[x]=1
        else:
             l[x]=0
n2=""
for x in range(0,len(l)):
        k=l[x::]
        n2=n2+str(n(k))+" "
print(n2.strip())
