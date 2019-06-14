t=int(input())
i=0
x=0
n=[]
while i<90 and i<t:
  r=0
  for j in str(t-i):
    r+=int(j)
  if r+(t-i)==t:
    x+=1
    n.append(t-i)
  i+=1
print(x)
for i in n:
  print(i)
