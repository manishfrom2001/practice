a=int(input("enter the value"))
for i in range(0,a-1):
    for j in range(1,20-i):
        print(" ",end="")
    for k in range(1*i+1):
        print("*",end=" ")
    print(" ")
for num in range(a,0,-1):
    for l in range(num-18,2):
        print(" ",end="")
    for m in range(num):
        print("*",end=" ")
    print(" ")