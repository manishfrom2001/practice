# a=[1,2,3,4,5]
# b=[3,5,6,7,8]
# c=[]
# for i in range(len(a)):
#     c.append(a[-i-1]+b[i])
# print(c)





# by two loops
a=[1,2,3,4,5,6,7]
b=[4,6,7,8,6,8,9]
c=[]
d=[]
sum=0
for i in a:
    c.insert(0,i)
for j in range(len(c)):
    sum=c[j]+b[j]
    d.append(sum)
print(d)


# only reverse the list by append
# a=[1,2,3,4,5,6,7]
# b=[]
# for i in range(len(a)):
#     b.append(a[-i-1])
# print(b)
