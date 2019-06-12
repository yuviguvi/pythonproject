t=int(input())
s=0
for i in range(1,t+1):
    if "2" in str(i):
        s=s+1
    if str(i).count("2")>1:
        s=s+(str(i).count("2"))-1
print(s)
