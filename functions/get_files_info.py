import os
import types
from pathlib import Path

""" schema_get_files_info = types.FunctionDeclaration(
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
) """
schema_get_files_info = {
    "name": "get_files_info",
    "description": "Lists files in the specified directory along with their sizes, constrained to the working directory.",
    "parameters": {
        "type": "object",
        "properties": {
            "directory": {
                "type": "string",
                "description": "The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            },
        },
        "required": [],  # add "directory" here if it must be provided
    },
}



def get_files_info(working_directory, directory=None):
    
    #Need to test for path first? directory="pkg" is not a directory but working_directory/directory is a path
    path = os.path.join(working_directory,directory)
    #print(path)
    #print(os.path.isdir(path))
    #ispath = os.path.isdir(path)
    #print("IP", ispath)
    #if ispath == False:
    #   print (f'Error: {directory} is not a directory')
    #print(working_directory in path)
    #print(directory)
    #print(working_directory)
    #print(directory)
    #print(path)
    #working_directory_abs = os.path.abspath(working_directory)
    #print("wda",working_directory_abs)
    #print(os.path.abspath(directory))
    #print(os.path.isdir(path) and working_directory in path)
    if os.path.isdir(path) and working_directory in path and not directory == "../":
    #if working_directory in path:
        #print("HERE")
        result_string = f"'{directory}'"
        if directory == ".":
            result_string = "current"
        print(f"Result for {result_string} directory")
        for item in os.listdir(path):
           full_path = os.path.join(path, item)           
           file_size_bytes = os.path.getsize(full_path)
           isdir = os.path.isdir(full_path) == True
           print(f"- {Path(item)}: file_size={file_size_bytes} bytes, is_dir={isdir}")
           #print(p)
        

    elif os.path.isdir(path) == True:

       print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    else:
        print(f'Error: {directory} is not a directory')
              
       # directory is a directory, but is it in working_directory?
    

def main():
  #get_files_info("calculator","pkgx")
  get_files_info("calculator", "../")

if __name__ == "__main__":
  main()




"""
os.path.abspath(): Get an absolute path from a relative path
os.path.join(): Join two paths together safely (handles slashes)
.startswith(): Check if a string starts with a substring
os.path.isdir(): Check if a path is a directory
os.listdir(): List the contents of a directory
os.path.getsize(): Get the size of a file
os.path.isfile(): Check if a path is a file
.join(): Join a list of strings together with a separator
"""