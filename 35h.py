t=input()
for i in range(0,len(t)):
    if t[:i]==t[i+1:]:
        
        n=0
        break
    else:
        n=1
if n==0:
    print("YES")
else:
    print("NO")
    
    
    
