s  =input()
t = list(map(int,input().split()))
for i in range(len(t)):
    if (i%2 == 0 and t[i]%2 !=0) or (i%2!= 0 and t[i]%2 == 0):
        print(t[i],end = " ")
