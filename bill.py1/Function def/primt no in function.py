# only chacking prime no
def prime(d):
    meassage=""
    f=0
    for i in range(2,d+1):
        if i%d==0:
            f=1
            break
    if f==0:
        meassage="not prime"
    else:   
        meassage="prime"
    return meassage
n=prime(7)
print(n)
