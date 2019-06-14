t,s=map(int,input().split())
if t%10==0:
  t=str(t)
  c=0
  for i in range(len(t)-1,-1,-1):
    if t[i]=='0':
      c+=1
  if s<=c:
    print(t)
  else:
    t=t[:-c]
    t=t+'0'*s
    print(t)
elif 10%(t%10)==0:
  no=int('1'+'0'*s)
  while True:
    if no%t==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*s)
else:
  print(str(t)+s*'0')
