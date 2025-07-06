import os
def get_files_info(working_directory, directory=None):
    
    #Need to test for path first? directory="pkg" is not a directory but working_directory/directory is a path
    path = os.path.join(working_directory,directory)
    if os.path.isdir(path):
       print(f'{path} is a directory')
    elif os.path.isdir(directory):
       return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        return f'Error: {directory} is not a directory'
       
       
       # directory is a directory, but is it in working_directory?
    
    
    
    
    return path
    #print(f"path: {os.path.isdir(path)}")
    






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