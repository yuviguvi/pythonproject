#yv
t,s = map(int,input().split())
L = []

for i in range(0,t) :
    L.append([])
for i in range(0, t):
    L[i] = list(map(int, input().split()))
L2 = L[0][:]
L3 = []
for j in range(1,t) :
    for i in range(0,s) :
        if L[j][i] in L2 :
            L3.append(L[j][i])
            L2.remove(L[j][i])
    #print(L3)
    L2 = L3[:]
    L3 = []
print(*L2)
