# a=[10,12,3,5,8,9]
# b=len(a)
# sum=0
# for i in a:
#     sum=sum+i
# print(sum//b)


# a=[1,2,3,4,5,6]
# b=len(a)
# sum=0
# for i in range(b):
#     sum=sum+a[i]
#     c=sum//b
# print(c)



# a=[1,2,3]
# b=[2,2,3]
# for i in range(len(a)):
#     for j in b:
#         if j<a[i]:
#             print(a[i],j)



a=[1,2,3,4,9,6]
b=[2,2,3,4]
if len(a)> len(b):
    for i in range(len(a)):
        if len(a)>len(b):
            b.append(0)
        for j in b:
            if j<a[i]:
                print(a[i],j)
                

            


