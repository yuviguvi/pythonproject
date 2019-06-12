t,s=map(int,input().split())
l=[str(x) for x in input().split()]
b=l[s:]+l[:s]
print(' '.join(b))
