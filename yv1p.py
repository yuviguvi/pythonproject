t=int(input())
s=[]
for i in range(t):
    s.append(input())
z=s[0]
x,c=0,0
n=""
for i in range(len(z)):
    c=0
    for k in range(1,t):
          if z[i]==s[k][i]:
            c=c+1
    if c==t-1:
       n=n+z[i]
    else:
        break
print(n)
