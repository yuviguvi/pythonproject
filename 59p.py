s = input()
t = input()
bar = s.index("|")
i = s[:bar]
j = s[bar+1:]
a = i+t
b = j+t
if len(i) == len(b):
    w = i + "|" + j + s1
    print(w)
elif len(j) == len(a):
    w = i + t +"|"+ j
    print(w)
else:
    print("Impossible")
