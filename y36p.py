t = int(input())
M = [ int(x) for x in input().split()]
t = len(M)
c = 0
for i in range(0,t-2) :
    for j in range(i+1, t-1):
        for k in range(j+1, t):
            if M[i] > M[j] > M[k] :
                c += 1
print(c)
