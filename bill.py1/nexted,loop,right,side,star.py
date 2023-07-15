a=int(input("enter the value"))
for i in range(a,0,-1):
    for j in range(1,a-i+1):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print(" ")
    
