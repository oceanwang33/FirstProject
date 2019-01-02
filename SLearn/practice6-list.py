""""
六种数据类型
number
string
list
tuple
sets
dictionary
"""
my_list=['你好',2018,2018,'你好',2018,2018,'english',2000]

print(len(my_list))
#help(my_list)

print(my_list[0])

my_list.append('5000')
#在最后加5000
print(my_list)

#print(my_list.remove('english'))

my_list.remove('english')
#去除一个
print(my_list)

#ctrl+/，comment注释切换

print(my_list.count(2018))
print(my_list.count('你好'))


