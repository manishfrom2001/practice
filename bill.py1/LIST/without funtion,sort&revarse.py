list1=[11,5,7,3,9,8,40,80,122]
# a.insert(2,4)
# a.sort()
# a.append(10)
# a.extend([15,11,21,19])
# for i in range(0,len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] > list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)
        

for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            temp=list1[j]
            list1[j]=list1[i]
            list1[i]=temp
print(list1)

