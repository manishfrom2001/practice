# only evensum
def even(b):
    sum2=0
    for i in range(b+1):
        if i%2==0:
            sum2=sum2+i
    return sum2
y=even(8)
print(y)

# only odd
def odd(e):
    a=0
    for i in range(e+1):
        if i%2!=0:
            a=a+i
    return a
v=odd(7)
print(v)