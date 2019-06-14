n=input()
l=list(set(n))
x=1
a=0
check=False
while True:
    ch=l[a]
    for j in range(0,len(n)-x):
        if ch in n[j:j+x]:
            check=True
        else:
            check=False
            a+=1
            if a>=len(l):
             a=0
             x+=1
            break

    if check==True:
        break
print(x)
