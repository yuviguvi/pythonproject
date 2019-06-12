t=int(input())
n=list(map(int,input().split()))
li=list(map(int,input().split()))
s=[]
for i in range(0,len(n)):
  s.append(n[i]+li[i])
print(*s)  
       
