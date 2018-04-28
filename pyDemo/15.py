#-*- coding:utf-8 -*-

#output
print("=="*20)
print('Name Management system v1.0')
print('1:Add a new name')
print('2:Delete a name')
print('3:Update a name')
print('4:Select a name')
print('5:End System')

#Defines an empty list to store names
names=[]

while True:
	#input
	num = int(input('Please input a number:'))
	if num == 1:
		new_name=input('Please input your name:')
		names.append(new_name)
		print(names)	
	elif num == 2:
		delete_name=input('Please input deleted name:')
		if delete_name in names:
			names.remove(delete_name)
			print('delete success!')
		else:
			print('delete fail,not have this name')
	elif num == 3:
		pass
	elif num == 4:
		find_name=input('Please input find name:')
		if find_name in names:
			print('find this name')
		else:
			print('this name is not find')
	elif num == 5:
		break
	else:
		print('Sorry,your input have error!')

