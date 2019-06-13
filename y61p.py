t=list(map(str,input()))
s=list(map(str,input()))
for j in range(0,len(s)):
    n=r=l=0
    r=ord(t[j])
    l=ord(s[j])
    n=r+l
    if n>96 and n<123:
        print(chr(n),end="")
    elif (n-96)<122 and(n-96)>96:
        n=n-96
        print(chr(n),end="")
    elif n>148:
        n=n-96-26
        print(chr(n), end="")
    else:
        n=n-26
        print(chr(n), end="")
