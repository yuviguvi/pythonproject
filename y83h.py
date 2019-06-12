t=input()
a=[]
for i in range(0,len(t)-1):
    if t[i]==t[i+1]:
        x=t[:i+1]+t[i+2:]
        a.append(x)
a.sort()
print(a[-1])
