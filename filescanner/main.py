import os
path = r'C:'
res = ''
#path =r'C:\Users\Gaetano\Downloads'
while res != 'y' and res != 'Y' and res != 'n' and res != 'N':
	res = input('Do you want to specify a directory (Y/N):')
if res == 'y' or res == 'Y':
	path = input("Insert a specific folder:")


list_of_files = []
for root, dirs, files in os.walk(path):
	for file in files:
		list_of_files.append(os.path.join(root,file))
for name in list_of_files:
    print(name)