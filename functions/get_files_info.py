import os

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
