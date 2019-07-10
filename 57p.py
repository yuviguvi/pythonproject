s1,s2=map(str,input().split())
count=0
for i in range(0,len(s1)):
    for j in range(0,len(s2)):
        if s1[i]==s2[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
