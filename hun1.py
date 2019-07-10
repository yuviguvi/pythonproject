n=int(input())
t=list(map(int,input().split()[:n]))
count=0
s=[]
for i in range(0,n+1):
   if(t.count(i)>1):
      s.append(i)
if(len(s)==0):
   print("unique")
x=sorted(s)
print(' '.join(map(str,x)))
