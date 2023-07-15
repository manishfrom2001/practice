def value(t):
    maxx=t[0]
    for i in t:
        if i>maxx:
            maxx=i
    return maxx
x=value([65,6,76,55,44,88,99,1,3])
print(x)
