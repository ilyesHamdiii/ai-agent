from functions import get_files_info
from functions.get_files_info import get_files_info,get_file_content
print("---------------------------------------------------1----------------------")
print('hello word ')
print("---------------------------------------------------2----------------------")

print(get_file_content("calculator", "pkg/calculator.py"))
print("---------------------------------------------------3----------------------")

print(get_file_content("calculator", "/bin/cat")    )
print("---------------------------------------------------4----------------------")

print(get_file_content("calculator", "pkg/does_not_exist.py"))