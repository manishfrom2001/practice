list1=[1,2,3,4,5,6,7]
b=[]
count=len(list1)
if count%2!=0:
    list1.append('')
for i in range(0,len(list1),2):
    c=[]
    for j in range(i,i+2):
        c.append(list1[j])
    b.append(c)
print(b)

        
        

        

        

# a=[1,2,3,4,5,6,7,8]
# b=0
# c=8
# for i in range(b,c,2):
    
#     print(a[i:i+2],end="")

