from itertools import combinations
s1,n1=map(int,input().split())
n2=len(str(s1))
x=list(combinations(str(s1),n2-n1))
x=(sorted(x))
y="".join(x[0])
print(y)
