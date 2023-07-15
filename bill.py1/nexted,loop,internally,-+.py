a=int(input("enter the value"))
sum=0
for i in range(1,a+1):
    c=0
    print(end="(")
    for num in range(1,i+1):
        if(num%2==0):
            print(num,end="-")
            c=c+num
        else:
            print(num,end="+")
            c=c-num
    c+=2                 
    if(i%2==0):
        sum=sum+c
        print(end="\b)-")
    else:
        sum=sum-c
        print(end="\b)+")
print(end="\b=")
print(sum,end="")