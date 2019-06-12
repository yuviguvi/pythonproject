n=int(input())
x=0
while n>0:
    s=n%10 
    x=x+s 
    n=n//10 
x=str(x)
t=x[::-1]
if t==x:
    print("YES")
else:
    print("NO")
