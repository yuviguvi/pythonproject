t=input()
flag=0
for i in range(1,len(t)):
  j=0
  while j<len(t) and len(t[:j]+t[i+j:])==len(t)-i:
    n=t[:j]+t[j+i:]
    if int(n)%8==0:
      flag=1
      print('yes')
      break
    j+=1
  if flag==1:
      break
else:
  print('no')
