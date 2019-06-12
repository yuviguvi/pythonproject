s=input()
t=''
for i in range(0,len(s)-1,2):
  if int(s[i+1])%2==0:
    t+=s[i]*int(s[i+1])
  else:
    t+=s[i]+s[i+1]
print(t)
