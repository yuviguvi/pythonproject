t=int(input())
n=[]
x=0
for i in range(2,t):
    for j in range(2,i+1):
        if i%j==0:
            break
    if j==i:
        n.append(i)
for i in range(len(n)):
    for j in range(len(n)):
        for k in range(len(n)):
            if n[i]+n[j]+n[k]==t:
                print(str(n[i])+" "+str(n[j])+" "+str(n[k]))
                x=1
                break
        if x==1:
            break
    if x==1:
        break
