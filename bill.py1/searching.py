a=int(input("enter the starting value"))
b=int(input("enter the ending value"))
s=57
f=1
for i in range(a,b):
    if(i==s):
        print("found")
        f=0
        break
if(f==1):
    print("not found")