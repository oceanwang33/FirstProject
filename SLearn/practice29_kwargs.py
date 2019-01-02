#**kwargs ,key word args,

def m1(*args,**kwargs):
    print('the type of args is ',type(args))
    print('the type of kwargs is ',type(kwargs))

m1()

dict_o={'name':'o','age':'12 years old','height':'175cm'}
def someone(dict_someone):
    for k,v in dict_someone.items():
        print(k,':',v)

someone(dict_o)


def someone(**kwargs):
    for k,v in kwargs.items():
        print(k,':',v)

someone(name='o',age='20')
