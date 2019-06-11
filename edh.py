t=int(input())
s=[]
x=0
for i in range(2,t):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        s.append(i)
for m in range(0,len(s)):
    for n in range(m,len(s)):
        if s[m]+s[n]==t:
            x=x+1
print(x)
