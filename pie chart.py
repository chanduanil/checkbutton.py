# import matplotlib.pyplot as plt
# parition = 'holidays','eating_out','shopping','groceries'
# sizes = [100,200,300,400]
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes,labels = parition, autopct='%1.1f%%',shadow = True,startangle =90)
# ax1.axis('equal')
# plt.show()2
# while True: print(eval(input(">>>")))

import time
from random import randint

# for i in range(1, 45):
#     print('')
# s = ' '
# for i in range(1, 1000):
#     count = randint(1, 100)
#     while(count > 0):
#         s += ' '
#         count -= 1
#     if (i%10 == 0):
#         print(s + ' happy new year 2023 ')
#     else:
#         print(s + '*')
#     s = ' '
# #     time.sleep(0.05)
# x = lambda a:a//2
# y =[x(b) for b in range(2)]
# z = sum(y)
# print(z)
# l1 =[ 12,10,23,56,44,90,87]
#
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i] > l1[j]:
#             l1[i],l1[j] = l1[j],l1[i]
# print(l1)
#
# fib = 0,1,1,2,3,5,8,13
fib = int(input("enter the number od fibonacci:"))
first =0
sec =1

for i in range(fib):
    print(first,end =" ")
    temp = first
    first = sec
    sec = temp+sec

