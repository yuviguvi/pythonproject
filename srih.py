t=int(input())
s=[]
for i in range(2,t):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            if i%j!=0 and i+j==t:
                x=str(j)+' '+str(i)
                s.append(str(x))
print(s[-1])
