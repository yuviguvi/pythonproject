f,g = input().split()
for i in range(0,len(f)-len(g)+1):
  if f[i:len(g)+i] == g:
    print('yes')
    break
else:
  print('no')
