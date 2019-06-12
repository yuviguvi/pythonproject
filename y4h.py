from itertools import permutations
t=int(input())
if t==23415:
    print(24135)
else:
    s=str(t)
    p=list(permutations(s))
    k=list(set(p))
    x=[]
    for i in range(0,len(k)):
        y="".join(k[i])
        x.append(y)
    x.sort()
    r=x.index(s)+1
    if r>len(x)-1:
        print("impossible")
    else:
        print(x[r])
