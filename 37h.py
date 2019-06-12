from itertools import combinations
t=input()
n=0
l=list(combinations(t,len(t)-1))
for i in range(len(l)):
    if l[i]==l[i][::-1]:
        print("YES")
        n=1
        break
if n==0:
    print("NO")
