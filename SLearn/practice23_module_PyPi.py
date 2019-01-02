

# import random
# for i in range(5):
#     value1=random.randrange(1,5)
#     print('value1:'+str(value1))
# for i in range(5):
#     value2=random.randint(1,5)
#     print('value2:'+str(value2))

# from random import randint,randrange
# for i in range(5):
#     value1=randrange(1,5)
#     print(value1)
#
# from random import *
# from math import *
#
# import math as m
# m.pi

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# browser = webdriver.Firefox()
#
# browser.get('http://www.yahoo.com')
# assert 'Yahoo' in browser.title
#
# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
#
# browser.quit()

# import selenium
# from selenium import webdriver
# webdriver.chrome
def sum(x):
    res = 0
    for i in range(x):
        res+=i
    return res
print(sum(5))


def print_nums(x):
    for i in range(x):
        print(i)
        return
print_nums(10)
