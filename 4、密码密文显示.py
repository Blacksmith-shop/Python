#！/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Blacksmith

'''
#下面的代码在pycharm上不能用，只能在Windows的命令行或者linux系统下使用，用的是python3.0
import getpass
username = input("username：")
password = getpass.getpass("password：")
print(username,password)
'''

#下面是在linux下用python和shell启一个交互模式
#需要用的到快是os模块 命令如下

os.system("df -h")
os.mkdir ("yourdir")
cmd_res = os.popen("df -h") read()      #用os.open来保存命令结果