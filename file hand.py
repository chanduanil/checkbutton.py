
import os
path = "mydata"

try:
    os.remove(path)
except FileNotFoundError:
    print("that file was not found")


# f= open("C:/Users/chand/PycharmProjects/pythonProject6/mydata","w")
# f.write("hai")
# f1= open('abc','a')
# f1.write("something")

#
# l1 = [1,1,2,3,4,2,5,6,7,5,4]
# print(l1)
# s1 = set(l1) # converted into set
#
# l1 = list(s1) # converted into list
#
# # list with no duplicate items
# print(l1)