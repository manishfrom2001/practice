a=int(input("enter the value"))
sum=0
for i in range(0,a):
    c=i+1
    print(end="(")
    for j in range(c):
        c=j+1
        print(c,end="+")
    print(end="\b)+")
    print(end="\b")
    for num in range(c):
        sum=sum+num+1
    print(end="+")
print(end="\b")
print(end="=")
print(sum)