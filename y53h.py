t,s=map(str,input().split())
s=int(s)
n=[]
for i in range(len(t)):
    if len(t[i:i+s])==s:
        n.append(t[i:i+s])
print(*n)
