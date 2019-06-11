s=input()
t=[]
for i in range(0,len(s)):
    for j in range(len(s)-1,i,-1):
        if s[i] == s[j]:
            z = s[i:j + 1]
            if z == z[::-1]:
                t.append(z)
t=sorted (t)
for i in range(0,len(t)):
    print(t[i])
