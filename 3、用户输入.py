#！/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Blacksmith

#这个是python3.0的输入语法
name = input("请输入你的名字：")
#在3.０里面，默认input里面存放输入的都是字符串，而不是数字，
#age = input("请输入你的年龄：")
#如果需要强制转换，可以用int来转换
age = int(input("请输入你的年龄："))
job = input("请输入你的工作：")

msg = '''
Infomation of user %s:
-----------------
Name: %s
Age: %d
Job: %s
-------END-------
'''% (name,name,age,job)
print(msg)

#  %s：表示格化式一个对象为字符   %d：整数  %f:表示浮点数

'''
#下面这个是python2.7的输入语法，他的输入语法是raw_input
name1 = raw_input("请输入你的名字：")
print("用户输入的信息是:", name1)
'''