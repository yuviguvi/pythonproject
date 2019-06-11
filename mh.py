t = int(input())
s = 0
n = [ [int(e) for e in input().split()] for i in range(t)]
for i in range(t):
    s += n[i][(t-1)-i]
print(s)
