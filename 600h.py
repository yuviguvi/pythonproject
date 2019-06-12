t=int(input())
s=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
i=s.index(s[t-2])
j=a.index(s[i])
print(i-j)
  
