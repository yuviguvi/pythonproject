t=input()
x=0
if len(t)==1:
    print("yes")
else:
    for i in t:
        if t.count(i)==len(t):
            print("no")
            x=1
            break
    if x==0:
        print("yes")
