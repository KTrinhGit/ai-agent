import os

def get_files_info(working_directory, directory="."):
    relative_path = os.path.join(working_directory, directory)
    if not (os.path.abspath(relative_path).startswith(os.path.abspath(working_directory))): 
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    if not os.path.isdir(relative_path): 
        return f"Error: '{directory}' is not a directory"

    dir_items = os.listdir(relative_path)
    res = ""
    
    for item in dir_items: 
        file_path = os.path.join(relative_path, item)
        res += (f"- {item}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n")

    return res


