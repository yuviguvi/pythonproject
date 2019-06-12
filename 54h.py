t = input()
a = [int(x) for x in input().split()]
z = []
l = len(a)
for i in range(l):
    z.append(str(min(a[0:i+1])))
print(' '.join(z))
