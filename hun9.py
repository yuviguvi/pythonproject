t=int(input())
s=list(map(int,input().split()))
m=max(s)
a,b=0,0
for i in range(0,len(s)-1):
  for j in range(i+1,len(s)):
    if abs(s[i]+s[j])<m:
      a,b=s[i],s[j]
      m=abs(a+b)
print(a,b)
