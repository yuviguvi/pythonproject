n = int(input())
s = [x for x in input().split()]
t = []
for i in range(len(s)):
    if s[i] == str(i):
        t.append(s[i])
    # print(i, s[i])

if len(t) == 0:
    print('-1')
else:
    print(' '.join(sorted(t)))
