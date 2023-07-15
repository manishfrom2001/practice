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
print(x)