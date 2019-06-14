t,s=input().split()
t=int(t)
s=int(s)
s1=''
u=2
if(t+s<=3):
    for i in range(0,t+s):
        if(i%2!=0):
            s1=s1+'0'
        else:
            s1=s1+'1'
else:    
    for i in range(0,t+s):
        if(i==u):
            s1=s1+'0'
            if(u==s):
                u=u+2
            else:
                u=u+3
        else:
            s1=s1+'1'
x=len(s1)-1
if(int(s1[x])==0):
    print('-1')
elif t==1 and s==2: print("011")
else:
    print(s1)
