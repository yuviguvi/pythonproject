t=input()
c=0
n=[]
d=t[0]
for i in range(0,len(t)-1):
    if t[i]==t[i+1]:
        c=c+1
        d=t[i]
    else:
        n.append([c,d])
        c=1
n.append([c,d])
n.sort(reverse=True)
print(n[0][1],n[0][0])
