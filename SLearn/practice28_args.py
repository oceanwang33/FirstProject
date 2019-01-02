#*args,多个参数,args是tuple元组类型

def add(num1,num2,num3):
    print(num1+num2+num3)

add(1,1,2)

#*args方法
def add(*args):
    print(sum(args))
    print(type(args))
add(1,2,3)


def add(*args):
    for name in args:
        print('i love '+name)
add('小马','王子','李四')
