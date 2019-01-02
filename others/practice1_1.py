# # 找到url
# # 解析url，浏览器自带抓包工具F12
# # 提取数据
# # 保存数据
#
# num=7
# if num==5:
#     print('number is 5')
# else:
#     if num==11:
#         print('number is 11')
#     else:
#         if num==7:
#             print('number is 7')
#         else:
#             print("number isn't 5,11 or 7")
#
# num=7
# if num==5:
#     print('number is 5')
# elif num==11:
#     print('number is 11')
# elif num==7:
#     print('number is 7')
# else:
#     print("number isn't 5,11 or 7")
#
# print (1!=1 and 2==2)
#
# if(1==1) and (2+2>3):
#     print ('true')
# else:
#     print ('false')
#
# age = 15
# money = 500
# if age > 18 or money > 100:
#     print("Welcome")
#
#     a = 20
#     b = 10
#     c = 15
#     d = 5
#     e = 0
#
#     e = (a + b) * c / d  # ( 30 * 15 ) / 5
#     print( "(a + b) * c / d 运算结果为：", e)
#
#     i=1
#     while i<=5:
#         print (i)
#         i=i+1
#     print ('finished!')
#
# i=0
# while 1==1:
#     print (i)
#     i=i+1
#     if i>=5:
#         print ('brdaking')
#         break
# print ('finished')
#
# i=5
# while True:
#     print (i)
#     i=i-1
#     if i<=2:
#         break
#
#
# i=0
# while True:
#     i=i+1
#     if i==2:
#         print ('skipping 2')
#         continue
#     if i==5:
#         print ('brdaking')
#         break
#     print (i)
# print ('finished')
#
# words=['hello','world','!']
# print (words[0]+words[2])
#
# empty_list=[]
# print (empty_list)
#
#
# number=3
# things=['string',0,[1,2,number],4.56]
# print (things[0])
# print (things[2][2])
#
# str='hello world'
# print (str[7])
#
# nums=[7,7,7,7,7]
# nums[2]=5
# print (nums)

# nums=[1,2,3]
# print (nums+[4,5,6])
# print (nums*3)
#
# words=['spam','egg','spam','sausage']
# print ('spam' in words)
# print ('tomato' in words)
# print ('sp' in words)
#
# nums=[10,9,8,7,6,5]
# nums[0]=nums[1]-5
# if 4 in nums:
#     print (nums[3])
# else:
#     print (nums[4])
#

# nums=[1,2,3]
# print (not 4 in nums)
# print (4 not in nums)
# print (not 3 in nums)
# print (3 not in nums)
# nums.append(4)
# print (nums)
# print (len(nums))

# words=['python','fun']
# index=1
# words.insert(index,'is')
# print (words)
#
# nums=[9,8,7,6,5]
# nums.append(4)

for i in range(10):
  if not i % 2 == 0:
    print(i+1)

letters = ['x','y','z']
letters.insert(1,'w')
print(letters[2])

list = [1,2,3]
for var in list:
    print(var)


def print_with_exclamation(word):
    print(word+'!')

print_with_exclamation('SPAM')

def max(x,y):
    if x>y:
        return x
    else:
        return y

print(max(4,7))

"""
print('sdf')
"""

def multiply(x,y):
    return x*y

a=4
b=7
operation=multiply
print(operation(a,b))


def add(x,y):
    return x+y
def do_twice(func,x,y):
    return func(func(x,y),func(x,y))

a=5
b=10
print(do_twice(add,a,b))

import random
for i in range(5):
    value=random.randint(1,6)
    print(value)

from math import pi,sqrt
print(pi)
