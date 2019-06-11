u,v=list(map(str,input().split()))
s=[]
for i in u:
    for j in v:
        if i==j:
            s.append(i)
print("".join(s))
