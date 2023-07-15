a=int(input("enter the starting value"))
for i in range(0,a):
    c=i+1
    print(end="(")
    for j in range(c):
        c=j+1
        print(c,end="+")
    print(end="\b)+")
print(end="\b")
        