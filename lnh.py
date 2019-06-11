t=input()
n=input()
x=[]
for i in range(0,len(t)):
    for j in range(0,len(n)):
        if t[i]==n[j] and j<=i:
            if t[i] not in x:
                x.append(t[i])
print(''.join(list(x)))
