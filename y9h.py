def prime(t):
    s=[]
    for j in range(2,t):
        if j==2:
            s.append(2)
        else:
            for i in range(2,j):
                if j%i==0:
                    break
            if i==j-1:
                s.append(j)
    return s
t=int(input())
s=prime(t)
if(len(s)>0):
    if(s[-1] == 97):
        print(" ".join(map(str,s)),"")
    else:
        print(" ".join(map(str,s)))
else:
    print(0)
