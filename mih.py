t=int(input())
s=[int(x) for x in input().split()]
x=0
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if s[i]<s[j] and i<j:
            x+=1
print(x)
