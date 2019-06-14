t,s,q,r=map(int,input().split())
n=[int(i) for i in input().split()]
c=[s*n[i]+q*n[j]+r*n[k] for i in range(len(n)) for j in range(len(n)) for k in range(len(n)) if i<=j<=k]
print(max(c))
