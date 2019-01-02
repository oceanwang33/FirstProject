
class Father:
    name='o'
    def eat(self):
        print('father can eat')
class Mother:
    def walk(self):
        print('walk like mother')

class Son(Father,Mother):
    def eat(self):  #override重载了上一级对象的属性
        print('eat like son')
    pass

littleO=Son()
littleO.eat()
littleO.walk()

