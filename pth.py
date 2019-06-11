t=int(input())
x=str(t)
s=0
for i in range(0,len(x)):
    s=s+int(x[i])**i
print(s)
