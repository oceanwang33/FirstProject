#while限定一个条件后，达到条件后，持续执行，条件不满足就停止。与if不同的是，while条件满足时时持续执行
#让程序更有生命

while 10<11:
    print('hello while loop')
    break

condition=1
while condition<11:
    print(condition)
    condition=condition+1
print('-------------------------------------------------------------')
for i in range(1,10):
    print(i)

while True:
    a=int(input('please enter number a:'))
    b=int(input('please enter number b:'))
    print('a+b='+str(a+b))
    break

