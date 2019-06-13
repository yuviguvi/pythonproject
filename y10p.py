t=int(input())
s=[int(i) for i in input().split()]
x=0
for i in range(t):
    for j in range(i):
        if s[j]<s[i]:
            x+=s[j]
print(x)
