t=int(input())
s=[int(i) for i in input().split()]
x=[int(i) for i in input().split()]
i=s.index(s[t-2])
j=x.index(s[i])
print(i-j)
