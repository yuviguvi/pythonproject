t=input()
s=''
n=[]
for i in t:
    if i not in n:
        s+=i
        n.append(i)
    elif i in n:
        break
print(len(n))
