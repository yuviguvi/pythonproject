t=input()
if t==t[::-1]:
    print("yes")
else:
    value=t.strip("0")
    if value==value[::-1]:
        print("yes")
    else:
        value=t.lstrip("0")
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
