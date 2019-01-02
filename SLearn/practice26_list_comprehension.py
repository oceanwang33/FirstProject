
#传统方法
newList=[]
for i in range(11):
    newList.append(i*2)
print(newList)

#简洁方法
print([i*2 for i in range(11)])

#传统方法
list=['小明','王子','李四','张飞','王爷']
emptyList=[]
for name in list:
    if name.startswith('王'):
        emptyList.append(name)
print(emptyList)
#简洁方法
emptyList1=[name for name in list if name.startswith('王')]
print(emptyList1)

