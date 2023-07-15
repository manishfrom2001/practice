a = [5,5,5,6,6,7,8,9,9]
b=[]
d=[]
for i in a:
    if i not in b:
        c = 0
        b.append(i)
        for j in a:
            if j == i:
                c=c+1
        d.append(c)
print(b)
print(d)






# a = [5,5,5,6,6,7,8,9,9]
# b=[]
# d=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#         c = a.count(i)
#         d.append(c)
# print(b)
# print(d)      