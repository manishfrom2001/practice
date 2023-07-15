def duplicate(p):
    b=[]
    for i in p:
        if i not in b:
            b.append(i)
    return b
x=duplicate([1,2,3,4,2,5])
print(x)