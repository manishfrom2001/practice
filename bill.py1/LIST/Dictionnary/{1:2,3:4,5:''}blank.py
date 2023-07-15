a=[1,2,3,4,5,6,7]
b={}
c={}
for i in range(len(a)):
    if i%2==0:
        b=a[i]
        c[b]=''
    else:
        c[b]=a[i]
print(c)



