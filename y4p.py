n1,n2=input().split()
t=0
if len(n1)>len(n2):
  n1,n2=n2,n1
i=0
while i<len(n1):
  t+=(ord(n2[i])-ord(n1[i]))
  i+=1
for i in range(i,len(n2)):
  t+=ord(n2[i])-ord('a')+1
print(t)
