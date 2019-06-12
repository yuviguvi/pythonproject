t=input()
s=""
n=0
for i in range(len(t)):
    if t[i]==" ":
        s=s+t[i]
    elif  n%2!=0:
        s=s+t[i]
        n=n+1 
    else:
        s=s+t[i].upper()
        n=n+1
print(s)
