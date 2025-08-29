import os

def write_file(working_directory, file_path, content):
    relative_path = os.path.join(working_directory, file_path)

    if not (os.path.abspath(relative_path).startswith(os.path.abspath(working_directory))): 
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(relative_path): 
        directory_name = os.path.dirname(relative_path)
        os.makedirs(directory_name, exist_ok=True)

    try: 
        with open(relative_path, "w") as f: 
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e: 
        return f"Error: {e}"