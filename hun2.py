t = int(input())
n = [x for x in input().split()]
m = sorted(n, reverse=True)
print(''.join(m))
