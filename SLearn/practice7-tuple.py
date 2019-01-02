mylist=[1,2,3,4,5]
#assign
mytuple=(1,2,3,4,5)

print(type(mylist))
print(type(mytuple))

print(len(mylist))
print(len(mytuple))


print(mytuple[0])
print(mylist[0])

print(dir(mylist))
print('................................................................................................................................')
print(dir(mytuple))
# list is mutable.可以更改数据类型。tuple is inmutable.不可以更改
mylist.remove(3)
print(mylist)

#现实中，如果数据不允许用户更改，可以用tuple数据类型.tuple数据运行较快
