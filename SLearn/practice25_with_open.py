
file=open('o.txt')
text=file.read()
print(text)
file.close()


with open('c:/Users/ocean/Desktop/o2.txt') as f:#用with就不需要close，常用with。默认参数是'r'
    print(f.read())

# with open('c:/Users/ocean/Desktop/o2.txt','w') as f:#w是覆盖
#     f.write('世界你好，我很小。')

with open('c:/Users/ocean/Desktop/o2.txt','a') as f:
    f.write('我去哪里\n')

print(help(open))