s1=input()
flagg=0
for i in range(0,len(s1)-1):
  for j in range(i+1,len(s1)):
    if s1[i]<s1[j]:
      flagg=1
      print(s1[j:])
      break
  if flagg==1:
    break
else:
  print(s1)
