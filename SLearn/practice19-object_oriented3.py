# class Student:
#     name=input('name:')
#    # name = 'o'
#     age=input('age:')
#     #age = 15
#     def eat(self):
#         print(self.name, ' can eat' + ' and he is ', self.age)
#
#
# Student().eat()
# print('----------------------------------------------------------------')

class Student:
    #name=input('name:')
    name = 'o'
    #age=input('age:')
    age = 15
    def eat(self):
        print(self.name, ' can eat' + ' and he is ', self.age)

    @staticmethod #静态方法,不用加self，但导致使用该方法的属性无法调用class内的变量
    def walk():
        print('student can walk')


Student().walk()
student1=Student()
student1.eat()
student1.walk()

studuent2=Student()
studuent2.eat()
studuent2.walk()
