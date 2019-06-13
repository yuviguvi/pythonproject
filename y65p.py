n,s = map(int,input().split())
c = list(map(int,input().split()))
a = int(input())
t = (sum(c)-c[s])//2
if a == t:
  print("Bon Appetit")
else:
  print(a-t)
