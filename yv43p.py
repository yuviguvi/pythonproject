t = int(input())
a1 = list(map(int,input().split()))
s,l = 0,[]
b1 = [x for x in range(1,t+1)]
for i in a1:
  if i in b1:
    b1.remove(i)
k = 0
for i in range(0,t-1):
  p = a1[i]
  for j in range(i+1,t):
    if p == a1[j]:
      if p < b1[k]:
        a1[j] = b1[k]
        s += 1
      else:
        a1[i] = b1[k]
        s += 1
      k += 1
print(s)
print(*a1)
