t=input()
x=1
for i in range(0,len(t)-2):
    for j in range(len(t)-1,i,-1):
        s=t[i:j+1]
        if s==s[::-1] and abs(i-j)>x:
            x=len(s)
print(x)
