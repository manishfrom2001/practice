a = [1,2,3,4,5,6,7,8]
b = []
for i in range(0,len(a),4):
    c=[]
    d=[]
    for j in range(i,i+4):
        if a[j]%2==0:
            c.append(a[j])
        elif a[j]%2!=0:
            d.append(a[j])
    b.append(d)
    b.append(c)
print(b)




