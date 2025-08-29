import os
import subprocess
import sys 

def run_python_file(working_directory, file_path, args=[]):
    relative_path = os.path.join(working_directory, file_path)

    if not (os.path.abspath(relative_path).startswith(os.path.abspath(working_directory))): 
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(relative_path): 
        return f'Error: File "{file_path}" not found.'
    
    if not relative_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    args = [sys.executable, file_path] + args

    try: 
        completed_process = subprocess.run(args, timeout=30, capture_output=True, cwd=working_directory)
    except Exception as e: 
        return f"Error executing Python file: {e}"

    if not completed_process.stderr.decode and not completed_process.stdout.decode(): 
        return "No output produced" 

    if completed_process.returncode != 0: 
        return f'STDOUT: {completed_process.stdout.decode()} STDERR: {completed_process.stderr.decode()}. Process exited with code {completed_process.returncode}'
    else: 
        return f'STDOUT: {completed_process.stdout.decode()} STDERR: {completed_process.stderr.decode()}.'
        