#-*- coding:utf-8 -*-
'''
sum = 150

if not (sum>0 and sum<150):
	print("xxx")
else:
	print("ddd")
'''

age = raw_input("请输入你的年龄：")
age = int(age)
if (age > 0 and age <= 18):
	print('年龄是：%s'%age)
else:
	print('年龄太大')