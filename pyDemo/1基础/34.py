import os

folder_name = input("input a folder_name:")

file_name = os.listdir(folder_name)

os.chdir(folder_name)

for name in file_name:
	# print(name)
	# os.chdir(folder_names)
	os.rename(name,"nzc-"+name)

