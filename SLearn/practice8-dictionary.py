mylist=(1,2,3,4)
myDictionary={'key':'value','key2':'value'}

myPhones={'Iphone x':1000,'Sumsang s9':900}
print(myPhones)
#access dic keys
Iphone_Price=myPhones['Iphone x']
print('Iphone Price:'+str(Iphone_Price))
#不能直接用+,因为Iphone_Price是数字类型

#change key values
myPhones['Iphone x']=500
#不能写成Iphone_Price=500
print(myPhones)

myPhones.clear()
print(myPhones)

print(str(Iphone_Price)*20)