t=input()
n=[0]
if "ab" not in t:
    print("0")
else:
    for i in range(len(t)):
        c=1
        for j in range(i,len(t)-1):
            if t[j]=="a" and t[j+1]=="b":
                c=c+1
            elif t[j]=="b" and t[j+1]=="a":
                c=c+1
            else:
                n.append(c)
                c=1
                break
        if t[i]=="a":
            n.append(c)
        else:
            n.append(c-1)
    print(max(n))
