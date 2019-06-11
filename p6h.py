t=input()
x=0
if len(t)==1:
    x=int(t)*int(t)
else:
    for i in range(len(t)):
        if i==len(t)-1:
            x+=(int(t[i])**int(t[0]))
        else:
            x+=(int(t[i])**int(t[i+1]))
print(x)
