n = "WELCOMETOGUVICORPORATIONS"
m = input()
arr = []
for i in range(5):
    arr.append(list(n[i*5:(i*5)+5]))
s = "".join(["".join(x) for x in [[arr[i][j] for i in range(5)] for j in range(5)]])
for i in range(len(n)):
    if n[i:i+len(m)] == m:
        print(i//5,i%5)
        print((i+len(m)-1)//5,(i+len(m)-1)%5)
        break
    if s[i:i+len(m)] == m:
        print(i%5, i//5)
        print((i+len(m)-1)%5, (i+len(m)-1)//5)
        break
else: print(0)
