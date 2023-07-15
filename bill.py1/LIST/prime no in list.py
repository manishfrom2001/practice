list1=[1,2,3,4,5,6,7,8,9]
list2=[]
for i in list1:
    f=1
    for j in range(2,i):
        if i%j==0:
            f=0
            break
    if f==1:
        list2.append(i)
print(list2)




# list1=[1,2,3,4,5,6,7,8,8,2,9,7,8]
# for i in range(0,len(list1)):
#     i==0
# print(i)

            
# a = 'hello guys'
# for i in range(0,len(a)):
#     i==0
# print(i)



# a=[3,4,5,4,4,3,5,2,0]
# b=0
# for i in a:
#     b=b+1
# print(b)




    


    


