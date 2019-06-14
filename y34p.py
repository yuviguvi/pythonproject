t,s=map(int,input().split())
n=0
Li=[]
for i in range(t):
      Li.append(input())
for i in range(t):
      for j in range(s-1):
            if(Li[i][j]!='R' and Li[i][j+1]!='R'):
                  n+=3
            elif(Li[i][j]!='G' and Li[i][j+1]!='G'):
                  n+=5
print(n)
