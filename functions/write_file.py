import os
from pathlib import Path


schema_write_file = {
    "name": "write_file",
    "description": "Write or overwrite files",
    "parameters": {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The relative path of the file to write to.",
            },
            "content": {
                "type": "string",
                "description": "The content to write into the file.",
            },
        },
        "required": ["file_path", "content"],
    },
}

def write_file(working_directory, file_path, content):
    path = os.path.join(working_directory,file_path)
    #print(file_path)
    #print(os.path.isdir(file_path))
    #print(path)
    
    if os.path.isdir(path) == False and working_directory in path and not "../" in file_path:
       try:
           with open(path, 'w') as f:
                f.write(content)
                
                print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
           
                
       except Exception as e:
           print(f"Error: {e}")
       
    elif os.path.isdir(file_path) == True:

       print(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
    else:
        print(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
        #print(f'Error: {file_path} is not a regular file')



def main():
  #get_files_info("calculator","pkgx")
  #write_file("calculator", "../")
  pass

if __name__ == "__main__":
  main()

