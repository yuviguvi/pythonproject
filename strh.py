a = input()
m = 0
for i in range(0,len(a)-1):
  for j in range(i+1,len(a)):
    R = a[i:j+1]
    if R == R[::-1]:
      if len(R) > m:
        m = len(R)
        h = R
print(h)
