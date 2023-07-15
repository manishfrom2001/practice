dict1={"name":"maruti","model":"dzire","year":2022}
# update method
# dict1.update({"city":"delhi"})
# # print(dict1)
# # for multi update
# dict1.update({"name":"manish","state":"delhi"})
# # print(dict1)
# # zone method
# dict1["zone"] = "northwest"
# # print(dict1)
# # len method
# a=len(dict1)
# # print(a)
# # pop method
# dict1.pop("zone")
# # print(dict1)
# # popitem() method. this method removes the last element!
# dict1.popitem()
# # print(dict1)
# # del keyword
del dict1["name"]
print(dict1)
# # del keyword also to delete the whole distionary
# del dict1
# print(dict1)
# # clear keyword the dictionary is there but without an element
# dict1.clear()
# print(dict1)
# change values (you can change the value by specified key)
# dict1 ["year"] = 2018
# print(dict1)
# checking the keys exists in the dictionary
# if 'model' in dict1:
#     # print("yes")
# else:
#     print("no")
# adding new values in the dictionary
# dict1 ["model"] = 'shift'
# print(dict1)
# get method (this method returns the value of specified keys)
# print(dict1["model"])
# copy method (it will print the values in the dictionary along with keys)
# x=dict1.copy()
# print(x)
# fromkeys (the fromkeys method return a dictionary with specified keys and the specified values)
# x=("firstkeys","secounkeys","thirdkeys")
# y=1
# dict1=dict.fromkeys(x,y)
# print(dict1)
# setdefault (the setdefault method returns the value of the item with the specified key)
# for exmple:
# x=dict1.setdefault("place","toyota")
# print(x)
# print(dict1)
# update (the update method inserts the specified items to the dictionary)
# dict1.update({"model":"shift"})
# print(dict1)



