a=[1,2,3,4,5,6,7]
b=[1,2,3,4,5,6,8]
d=[]
sum=0
for i in a:
    c=[]
for j in range(i):
    sum=b[j]+a[j]
    c.append(sum)
    # d.insert(0,sum)
print(c)



    
        
