T = int(input())
L = []
if T==2 :
    print('3')
    print('2 1 2')
    sys.exit()
if T==3 :
    print('4')
    print('2 1 3 2')
    sys.exit()
k = T//2
for i in range(2,T+1,2) :
    L.append(i)
for i in range(1,T,2 ) :
    L.append(i)
for i in range(2,T+1,2 ) :
    L.append(i)
print(len(L))
print(*L)
