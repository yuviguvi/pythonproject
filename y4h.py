from itertools import permutations
t=input()
lis=[]
s=permutations(t)
for i in s:
    n=int("".join(i))
    if n>int(t):
        lis.append(int("".join(i)))
print(sorted(lis)[0])
