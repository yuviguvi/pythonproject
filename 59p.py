n,m=map(str,input().split("|"))
t=input()
if  len(n)>len(m):
    if len(n)==len(m)+len(t):
        print(n+"|"+m+t)
elif len(n)<len(m):
     if len(m)==len(n)+len(t):
        print(n+t+"|"+m)
elif len(n)==len(m) and len(t)>1 or (len(m) or len(n)):
    print("impossible")
