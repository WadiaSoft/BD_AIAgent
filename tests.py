from functions.get_files_info import get_files_info


def main():
    print('1:', get_files_info("calculator", ".X") ) #Error: .X is not a directory
    print()
    print('2', get_files_info("calculator", "pkg")) #calculator/pkg is a directory NEED TO LIST CONTENTS
    print()
    print('3:', get_files_info("calculator", "./pkg")) #calculator/./pkg is a directory sketchy? ls calculator/./pkg -> same as calculator/pkg
    print()
    print('4:', get_files_info("calculator", ".")) #calculator/. is a directory NEED TO LIST CONTENTS
    print()
    print('5:', get_files_info("calculator", "pkg")) #5: calculator/pkg NEED TO LIST CONTENTS
    print()
    print('6:', get_files_info("calculator", "/bin")) #Error: Cannot list "/bin" as it is outside the permitted working directory
    print()
    print('7:', get_files_info("calculator", "../")) #Error: Cannot list "../" as it is outside the permitted working directory

    print()


if __name__ == "__main__":
  main()


#get_files_info("calculator", ".") 
"""
Should list calculator
Result for current directory:
 - main.py: file_size=576 bytes, is_dir=False
 - tests.py: file_size=1343 bytes, is_dir=False
 - pkg: file_size=92 bytes, is_dir=True
 - lorem.txt: file_size=28 bytes, is_dir=False
"""

#get_files_info("calculator", "pkg")
"""
Should list calculator/pkg
Result for 'pkg' directory:
 - calculator.py: file_size=1739 bytes, is_dir=False
 - render.py: file_size=768 bytes, is_dir=False
 - __pycache__: file_size=96 bytes, is_dir=True
 - morelorem.txt: file_size=26 bytes, is_dir=False
"""

#get_files_info("calculator", "/bin")
"""
Result for '/bin' directory:
    Error: Cannot list "/bin" as it is outside the permitted working directory
"""

#get_files_info("calculator", "../")
"""
Result for '../' directory:
    Error: Cannot list "../" as it is outside the permitted working directory
"""