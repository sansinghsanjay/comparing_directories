# libraries
import os

# take inputs from user
dir1_path = str(raw_input("Enter path of first directory: "))
dir2_path = str(raw_input("Enter path of second directory: "))

# variables to hold the content of directory 1 and directory 2
dir1_content = []
dir2_content = []

# function to get content of a directory
def get_directory_content(dir_path, dir_id):
	global dir1_content, dir2_content
	# if dir_id is 1, store the content of dir_path in dir1_content
	if(dir_id == 1):
		# remove dir1_path from the beginning of dir_path
		current_dir_path = dir_path.replace(dir1_path, '')
		# if first character is a slash ('/'), then remove it, otherwise it will not work with os.path.join
		if(current_dir_path[0] == '/'):
			current_dir_path = current_dir_path[1:]
		# appending contents of dir_path in list dir1_content
		dir1_content = dir1_content + [os.path.join(current_dir_path, item) for item in os.listdir(dir_path)]

	# if dir_id is 2, store the content of dir_path in dir2_content
	if(dir_id == 2):
		# remove dir2_path from the beginning of dir_path
		current_dir_path = dir_path.replace(dir2_path, '')
		# if first character is a slash ('/'), then remove it, otherwise it will not work with os.path.join
		if(current_dir_path[0] == '/'):
			current_dir_path = current_dir_path[1:]
		# appending contents of dir_path in list dir2_content
		dir2_content = dir2_content + [os.path.join(current_dir_path, item) for item in os.listdir(dir_path)]

# get the content of both the directories and store it in their respective list variables
dir1_content = os.listdir(dir1_path)
dir2_content = os.listdir(dir2_path)

# collect paths of every item under dir1_path
dir1_length = len(dir1_content)
index = 0
while(index < dir1_length):
	# if the item at index position is a directory then call the function get_directory_content
	if(os.path.isdir(os.path.join(dir1_path, dir1_content[index])) == True):
		get_directory_content(os.path.join(dir1_path, dir1_content[index]), 1)
		dir1_length = len(dir1_content)
	index += 1

# collect paths of every item under dir2_path
dir2_length = len(dir2_content)
index = 0
while(index < dir2_length):
	# if the item at index position is a directory then call the function get_directory_content
	if(os.path.isdir(os.path.join(dir2_path, dir2_content[index])) == True):
		get_directory_content(os.path.join(dir2_path, dir2_content[index]), 2)
		dir2_length = len(dir2_content)
	index += 1

# variable for mismatch count
mismatch_count = 0

# check if items of dir1_content are available in dir2_content, if not then print them
for i in range(len(dir1_content)):
	if((dir1_content[i] in dir2_content) == False):
		mismatch_count += 1
		print(mismatch_count, os.path.join(dir1_path, dir1_content[i]))

# check if items of dir2_content are available in dir1_content, if not then print them
for i in range(len(dir2_content)):
	if((dir2_content[i] in dir1_content) == False):
		mismatch_count += 1
		print(mismatch_count, os.path.join(dir2_path, dir2_content[i]))

