t=int(input())
z=[]
k=bin(2**t-1)[2::]
l=len(k)
for i in range(0,2**t):
    s=bin(i)[2::]
    if len(s)<l:
        z.append([s.count("1"),(l-len(s))*"0"+s])
    else:
        z.append([s.count("1"),s])
z.sort()
for i in range(0,len(z)):
    print(z[i][1])
