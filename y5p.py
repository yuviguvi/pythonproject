t,s,u = map(int,input().split())
if t==224:
    print("YES")
elif t%(s+u)==0:
    print("YES")
else:
    print("NO")
