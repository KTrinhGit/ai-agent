import os
from functions.config import MAX_CHARS
from google.genai import types 

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the contents of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to get the contents from.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    relative_path = os.path.join(working_directory, file_path)
    
    if not (os.path.abspath(relative_path).startswith(os.path.abspath(working_directory))): 
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(relative_path): 
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try: 
        with open(relative_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if os.path.getsize(relative_path) > MAX_CHARS: 
            return file_content_string + f"[...File '{file_path}' truncated at {MAX_CHARS} characters]"
        else: 
            return file_content_string

    except Exception as e: 
        return f"Error: {e}"
        
    


