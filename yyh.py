t=int(input())
a=format(t+1,"b")
p=[]
for x in a:
    if(x=='0'):
        p.append(3)
    else:
        p.append(4)
z="".join(map(str,p))
print(z[1:])
