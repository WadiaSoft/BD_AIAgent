import sys
import subprocess
import os
from pathlib import Path

def run_python_file(working_directory, file_path):
    

    path = os.path.join(working_directory,file_path)
    #print(file_path)
    #print(os.path.isdir(file_path))
    #print(os.path.isfile(file_path))
    #print(path)
    
    print(path)
    #print(not file_path in "../")
    #print(os.path.abspath(path))

    if (os.path.isfile(path) == True and working_directory in path) and not "../" in file_path:
        try:
            result = subprocess.run([sys.executable, file_path], capture_output=True, text=True, cwd=working_directory, timeout=30)
        
            output_parts = []
            
            if result.stdout:
                output_parts.append("STDOUT:\n" + result.stdout)
            if result.stderr:
                output_parts.append("STDERR:\n" + result.stderr)
            if result.returncode != 0:
                output_parts.append(f"Process exited with code {result.returncode}")
            
            if not output_parts:
                return "No output produced."
            
            return "\n".join(output_parts)
        except subprocess.TimeoutExpired:
            return "Process timed out after 30 seconds."                
    elif "../" in file_path:
       return(f'STDOUT:\nCannot execute "{file_path}" as it is outside the permitted working directory') 
    elif os.path.isfile(file_path) == False:
        return (f'STDOUT:\nFile "{file_path}" not found')
    elif Path(path).stem != "py":
        return (f'Error: "{file_path}" is not a Python file.')

    elif os.path.isdir(file_path) == True:

       return(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
    else:
        return(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')

def main():
  #get_files_info("calculator","pkgx")
  #write_file("calculator", "../")
  pass

if __name__ == "__main__":
  main()

