a=int(input("enter the value"))
for num in range(a,0,-1):
    for j in range(num-20,1):
        print(" ",end="")
    for k in range(num):
        print("*",end="")
    print(" ")
for i in range(1,a):
    for l in range(i-19,1):
        print(" ",end="")
    for m in range(i+1):
        print("*",end="")
    print(" ")