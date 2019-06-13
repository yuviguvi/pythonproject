t=input()
m=0
l=[]
for i in range(0,len(t)-1):
    for j in range(i+1,len(t)):
        s=t[i:j+1]
        k=s[::-1]
        if s==k:
            l.append(len(t)-len(k))
print(min(l))
