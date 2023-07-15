a=int(input("enter the value"))
for i in range(1,a):
    for j in range(i):
        print("*",end=" ")
    print(" ")
for k in range(a,0,-1):
    for l in range(k):
        print("*",end=" ")
    print('')