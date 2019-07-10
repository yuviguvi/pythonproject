t=int(input())
s=input().split()
for i in range(len(s)):
    for j in range(i+1,len(s)):
        for k in range(j+1,len(s)):
            if(int(s[i])+int(s[j])==int(s[k])):
                print(s[i],s[j],s[k])
