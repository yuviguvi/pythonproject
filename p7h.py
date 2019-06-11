t=int(input())
s=[str(t) for t in input().split()]
s.sort()
for i in s:
    print(i.lower())
