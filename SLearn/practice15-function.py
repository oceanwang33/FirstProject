
#def define 下定义
def func1():
    print('hello function')
func1()
print('-----------------------------------------------------')
a=10
b=10
print(a+b)
print('-----------------------------------------------------')

def sum(num1,num2):
    print(num1+num2)
sum(20,20)
print('-----------------------------------------------------')
def fun2():
    return 'hello fun2'
a=fun2()
print(a)
print(fun2())
print('-----------------------------------------------------')

def sum2(a,b):
    return (a+b)
m=sum2(1,2)
print(m)
print('-----------------------------------------------------')

def converter(weight):
    ponds=weight/0.45
    print(ponds)
converter(76)
print('-----------------------------------------------------')

#默认值100
def converter2(weight=100):
    ponds2=weight/0.45
    print(ponds2)
converter2()
converter2(weight=200)
