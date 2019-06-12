t=input()
s=''
for i in t:
    if i not in s:
        s+=i 
print(s[::-1])
