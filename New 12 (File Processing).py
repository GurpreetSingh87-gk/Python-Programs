# File Processing / File Handling :-
# --------------------------------

# Using Python code, we can read contents of existing files, we can write or over write into the
# existing file, we can add new elements into existing file which is also called append. For all
# these tasks, we have to open the file using function 'open file'.

'''
# Syntax to Open file:-

# file_object=open(file_name with extension,mode)

print("For Example")

fp=open("Read Mode File.py","r")
print(fp.read())

# Note:- Here, Fp is a file handler or file pointer, which we can read or write file contents. The
#        more specifies weather read or write or append into the file.


# There are some file handling modes such as:-
# -------------------------------------------

# 1. r - To Read the file.
# 2. w - To Write into the file that is override.
# 3. a - To Append into the file it means add new data into existing file.
# 4. x - To create a new file if file already exist then it will show error.


# Some other file handling modes are:-
# ----------------------------------

# 4. r+ - (read + write)
# 5. w+ - (read + write)
# 6. a+ - (read + append)


# File pointer in different modes:-
# --------------------------------

# 'r'- File pointer will point at the beginning of the file. If file doesn't exist gives error.

# 'w'- File pointer points at the beginning of the file. If file doesn't exist new file will be
#      created at the same location.

# 'a'- File pointer will point at the end of the file. If file doesn't exist new file will be
#      created at the same location.

print("------------------------------------------------------------------------------------------")

# Read File Mode('r'):-
# --------------

# 1. read mode()

# 2. readable()

# 3. read line mode()

# 4. read lines mode()

# Syntax to Read File:-
# -------------------

file=open("Read Mode File.py","r")
print(file.read())
file.close()

# Note:- We can specify how many characters or words we want to read by giving argument in read()
#        module.

# ================================================================================================

# 1. Read mode():- (It will open the file and read)
#    ----------

fp=open("Python Exam Practice.py","r")
print(fp.read())
fp.close()

# 2. Readable():- (It will tell the file is reaable or not in True/False
#    ---------

file=open("Python Exam Practice.py","r")
print(file.readable())
file.close()

# 3. Read line mode():- (It will read file line by line)
#    ----------------

file=open("Python Exam Practice.py","r")

line1=file.readline()
print(line1)
file.close()

# 4. Read lines mode():- (It will read all lines from file & return a list of string.
#    ----------------

fp=open("Python Exam Practice.py","r")
print(fp.readlines())
fp.close()

print("------------------------------------------------------------------------------------------")

# Write File Mode:-
# ---------------

# 1. write():-

# 2. writable():-

# 3. write lines mode():-

# ----------------------------------

# 1. Write('w'):- (It will write text given by user)
#    ---------

file=open("Write_Mode_File.py","w")
data="Do what excites!!"
print(file.write(data))
file.close()
print("Content Written Successfully!")

# 2. Writable():-
#    ---------

file=open("Write_Mode_File.py","w")
print(file.writable())
file.close()

# 3. Write lines mode():- (It will add multiple lines into file. It takes only one argument which
#    ------------------   can be given in a list of strings.)

fname=input("Enter File Name:")

file=open("Write_Mode_File.py","w")
datatwo=["Welcome to Python!!"]
file.writelines(datatwo)
file.close()
print("Contents Written Successfully!")

print("------------------------------------------------------------------------------------------")

# Append Mode('a'):-
# ----------------

file=open("Append Mode File.py","a")
file.write("\nIs Python only programming language ? ")
file.close()

print("------------------------------------------------------------------------------------------")

# Note:- To check the existence of file use the function 'isfile()' within 'os' module.

# Q:- Display the file message if is found print a message 'file found'.

# A:-

import os

fname=input("\nEnter file Name:")

if os.path.isfile(fname):
    fp=open(fname,"a")
    data="\nPython made up applications:-"
    fp.write(data)
    fp.write("\nInstagram, Spotify, Google, Youtube etc.")
    fp.close()
    print("Contents Written Successfully!")

else:
    print("File Not Found")
    
print("------------------------------------------------------------------------------------------")

# Tell Function():- (It returns number of characters within file including spaces.)
# ---------------

# Synatx:- file_object.tell()

file=open("Append Mode File.py","r")
print("File Position:",file.tell())
print("1st Line:",file.readline())

print("File Position:",file.tell())
print("2nd Line:",file.readline())

print("File Position:",file.tell())
print("3rd Line:",file.readline())

print("File Position:",file.tell())
print("4th Line:",file.readline())

print("File Position:",file.tell())
print("5th Line:",file.readline())

print("File Position:",file.tell())
print("6th Line:",file.readline())

file.close()

print("------------------------------------------------------------------------------------------")

# Seek Function():- (It returns number of character when user enter number.)
# ---------------

# Synatx:- file_object.seek()

file=open("Write_Mode_File.py","r")

print("File Position:",file.seek(3))
print("Number of Characters:",file.readline())
file.close()

# ==========================================

# Difference between Tell and Seek function:-
# ------------------------------------------

file=open("Write_Mode_File.py","r")

print("\nTell Function:-")# Tell function takes 0 argument & return text lines.

print("File Position:",file.tell())
print("1st Line:",file.readline())


print("\nSeek Function:-")# Seek function takes argument by user & return characters according to
                          # numbers which given by user.

print("File Position:",file.seek(3))
print("Number of Characters:",file.readline())
