i,j=map(int,input().split())
n,m=map(int,input().split())
k,l=map(int,input().split())
g,h=map(int,input().split())
if(abs((i-n)==(g-k))==abs((j-h)==(m-l))):
    print("yes")
else:
    print("no")
