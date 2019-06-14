t=int(input())
s=list(map(int,input().split()))
a=0
b=0
s.sort(reverse=True)
for i in s:
  s=a+i
  if b>s:
    a=s
  else:
    a=b
    b=s
print(a,b)
