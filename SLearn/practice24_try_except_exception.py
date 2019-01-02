
#
# try:
#     print(10/0)
# except:
#     print('you can not do it')

#异常处理
try:
    print(10/5)
    print(10+'o')
except ArithmeticError as e:
    print(e)
except Exception:
    print('there is something wrong')
except TypeError as e:
    print(e)

