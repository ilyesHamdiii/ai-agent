from functions import get_files_info
from functions.get_files_info import get_files_info,get_file_content,write_file,run_python_file
print("------------------------------------1------------------")

print(run_python_file("calculator", "main.py"))
print("------------------------------------2------------------")

print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("------------------------------------3------------------")

print(run_python_file("calculator", "tests.py"))
print("------------------------------------4------------------")

print(run_python_file("calculator", "../main.py"))
print("------------------------------------5------------------")

print(run_python_file("calculator", "nonexistent.py"))
print("------------------------------------6------------------")
