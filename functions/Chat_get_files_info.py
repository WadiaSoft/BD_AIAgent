import os
from pathlib import Path

def get_files_info(working_directory, directory=None):
    working_directory_abs = os.path.abspath(working_directory)
    
    # If directory is None, treat as working_directory itself
    if directory is None:
        path = working_directory_abs
    else:
        # If directory is absolute, use it directly; else, resolve relative to working_directory
        if os.path.isabs(directory):
            path = os.path.abspath(directory)
        else:
            path = os.path.abspath(os.path.join(working_directory_abs, directory))
    
    # Debug prints for clarity
    #print(f"Working directory abs: {working_directory_abs}")
    #print(f"Target path abs: {path}")
    
    if os.path.isdir(path):
        # Check if path is inside working_directory
        if os.path.commonpath([working_directory_abs, path]) == working_directory_abs:
            result_string = f"'{directory}'" if directory != "." else "current"
            print(f"Result for {result_string} directory")
            for item in os.listdir(path):
                full_path = os.path.join(path, item)           
                file_size_bytes = os.path.getsize(full_path)
                isdir = os.path.isdir(full_path)
                print(f"- {Path(item)}: file_size={file_size_bytes} bytes, is_dir={isdir}")
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        return f'Error: {directory} is not a directory'
