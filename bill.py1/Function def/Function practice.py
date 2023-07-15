# only sum
def add(a):
    sum=0
    for i in range(a):
        sum=sum+i
    return sum
x=add(10)

# only evensum
def even(b):
    sum2=0
    for i in range(b+1):
        if i%2==0:
            sum2=sum2+i
    return sum2
y=even(8)

# only fectorial
def fec(c,d):
    f=1
    for i in range(c,d+1):
        f=f*i
    return f
z=fec(1,5)


# only odd
def odd(e):
    a=0
    for i in range(e+1):
        if i%2!=0:
            a=a+i
    return a
v=odd(7)

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

# chot a and bada A
def str(o):
    c=ord(o)
    p=0
    if (c<97):
        p=c+32
    elif(c>96):
        p=c-32
    return p
k=str("V")
# print(chr(k))

def duplicate(p):
    b=[]
    for i in p:
        if i not in b:
            b.append(i)
    return b
x=duplicate([1,2,3,4,2,5])
# print(x)

# sexmaxx value in def
def number(a):
    maxx=a[0]
    secmaxx=a[0]
    for i in a:
        if i>maxx:
            maxx=i
    for j in a:
        if j>secmaxx and j!=maxx:
            secmaxx=j
    return secmaxx
x=number([2,4,5,7,8,91,5])
# print(x)

# maxx value in list in def
def value(t):
    maxx=t[0]
    for i in t:
        if i>maxx:
            maxx=i
    return maxx
x=value([65,6,76,55,44,88,99,1,3])
# print(x)
















