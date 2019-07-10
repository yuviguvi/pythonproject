n = input()
s = list(map(int,input().split()))
t = False
for i in s:
    if s.count(i) > 1:
        t = True
        break
print(i if t else "unique")
