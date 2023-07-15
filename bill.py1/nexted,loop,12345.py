a=int(input("enter the value"))
b=0
for i in range(1,a):
    b=b+1
    print(b)
    for j in range(i):
        b=b+1
        print(b,end="")
