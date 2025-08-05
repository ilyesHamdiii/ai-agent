import os
import subprocess
from google.genai import types

def get_files_info(working_directory,directory="."):
    directory1=os.path.join(working_directory,directory)
    full_path=os.path.abspath(directory1)
    p=os.path.abspath(working_directory)
    if  not (full_path.startswith(p)):
        return f"Error: Cannot list {directory} as it is outside the permitted working directory "
    if not os.path.isdir(full_path):
        return f"Error: {directory} is not a directory "
    string=""
    x=os.listdir(full_path)
    for file in x:
        y=os.path.join(full_path,file)
        if (os.path.isfile(y) or os.path.isdir(y)) :
            string=string+f"{file}:file_size={os.path.getsize(y)},is_dir={os.path.isdir(y)} \n"
        else:
            pass 
    return string
def get_file_content(working_directory,file_path):
    file=os.path.join(working_directory,file_path)
    print(file)
    full_path=os.path.abspath(file)
    print(full_path)
    p=os.path.abspath(working_directory)
    print(p)
    if not(full_path.startswith(p)):
        return f'Error: Cannot read "{file}" as it is outside the permitted working directory'
    if not (os.path.isfile(file)):
        return f'Error: File not found or is not a regular file: "{file}"'


    MAX_CHARS=10000

    with open(file,"r") as f :
        try:
            file_content_string=f.read(MAX_CHARS)
            n=len(file_content_string)
            f.seek(0)
            full_content=f.read()
                  
            if len(full_content)>n:
                msg=f"[...File {file_path} truncated at 10000 characters]"
            else:
                msg=""
        except:
            return f"Error: an error is occured with {file_path}"
    return file_content_string+'\n'+msg
def write_file(working_directory,file_path,content):
    file=os.path.join(working_directory,file_path)
    full_path=os.path.abspath(file)
    p=os.path.abspath(working_directory)
    if not(full_path.startswith(p)):
        return f'Error: Cannot writr to {file} as its outside tne permitted working directort'
    if not (os.path.isfile(file)):
        try :
            with open(file,"w")as f:
                f.write(content)
                print(f.read())
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except:
            return f"Error:an error has occured "
    else:
        try:
            with open(file,"a") as f:
                f.write(content)
                return f'Successfully wrote to "{file}" ({len(content)} characters written)'
        except:
            return f"Error:an error has occured"
def run_python_file(working_directory,file_path,args=[]):
    file=os.path.join(working_directory,file_path)
    full_path=os.path.abspath(file)
    p=os.path.abspath(working_directory)
    if not(full_path.startswith(p)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not (os.path.isfile(file)):
        return f'Error: File "{file_path}" not found.'
    if not (file.endswith(".py")):
        return f"Error:{file_path} is not a Python file ."
    try :
        result=subprocess.run(
            ["python",file_path]+args,
            cwd=working_directory,
            capture_output=True,

            text=True,
            timeout=30
        )
    except:
        subprocess.TimeoutExpired
        return "Error:Procees timed out after 30 seconds "
    
    if result.returncode!=0:
        msg=f'Process exited with code {result.returncode}'
    else:
        msg=""
    if not result:
        return f"No output produced "
    return f"STDOUT:{result.stdout} STDERR:{result.stderr}"+msg
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
schema_get_files_content = types.FunctionDeclaration(
    name="get_files_content",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
available_functions=types.Tool(
    function_declarations=[schema_get_files_info,schema_write_file,run_python_file,schema_get_files_content]
)

        