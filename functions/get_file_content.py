import os
from pathlib import Path

def get_file_content(working_directory, file_path):
    path = os.path.join(working_directory,file_path)
    #print(file_path)
    #print(os.path.isdir(file_path))
    if os.path.isfile(path) and working_directory in path and not file_path == "../":
       try:
           with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                if len(content) > 10000:
                   content = content[:10000]
                   #print (len(content))
                   content += f"...File {file_path} truncated at 10000 characters" 
                print(content)
       except Exception as e:
           print(f"Error: {e}")
       
    elif os.path.isdir(file_path) == True:

       print(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
    else:
        print(f'Error: {file_path} is not a regular file')



def main():
  #get_files_info("calculator","pkgx")
  get_file_content("calculator", "../")

if __name__ == "__main__":
  main()

