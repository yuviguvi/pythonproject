t, s, f, k = map(int, input().split())
count = 0
a = s-f
if (a >= 0):
    d = (t-f)*2
    for i in range (k):
        if (i == k-1):
             d =d/ 2
        if (a < d):
            a = s
            count += 1
        a = a - d
        if (a < 0):
            count = -1
            break
        d = 2*t - d
    print (count)
else:
    print (-1)
