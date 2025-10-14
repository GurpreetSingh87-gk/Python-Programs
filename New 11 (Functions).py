
# Functions:- 
# ----------

# What is Function?:- A function is set of statements that takes inputs, do some specific task and
#                     produces output.

# Types of Functions:-
# -------------------

# 1. Predefined function:- These functions are previously defined. We can call them by using
#    -------------------   function name which is called 'function call statement'.

# 2. User defined function:- Functions which are defined by user called as user defined function.
#    ---------------------   It has two types: i. Function definition  ii. Function call statement


# Syntax of defined function:-

# def function_name():
#       block of code
#       return statement


#--------------------------------------------------------------------------------------------------
'''
# Topic :- Functions
#          ---------

# Q:- Define a function which prints a message.

def myfunc(): # function definition
    print("Hello World!")

myfunc() # function calling

print("------------------------------------------------------------------------------------------")

print("Q:- Define a function 'add' which takes two numbers as input and display its addition.")

def add():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    print("Addition:",n1+n2)

add()

print("------------------------------------------------------------------------------------------")

print("Q1:- Define a function for all arithmetic operation.")
print("Q2:- Define a function which gives maximum and minimum between two numbers.")

print("\nAns1.")

print("\nAddition")
def addition():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter First Number:"))
    print("Addition:",n1+n2)

addition()

print("\nSubtraction")

def subtraction():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    print("Subtraction:",n1-n2)

subtraction()    

print("\nMultiplication")

def multiplication():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    print("Multiplication:",n1*n2)

multiplication()    

print("\nModulus")

def modulus():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    print("Modulus:",n1%n2)

modulus()    

print("\nExponent")

def exponent():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    print("Exponent:",n1**n2)

exponent()

print("\nDivision")

def division():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    print("Division:",n1/n2)

division()    

print("\nFloor Division")

def floordiv():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    print("Floor Division:",n1//n2)

floordiv()    

print("Ans2.")

print("\nMaximum")
def maximum():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    if n1>n2:
        print("First Number is Maximum")
    else:
        print("Second Number is Maximum")
        
maximum()

print("\nMinimum")
def minimum():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    z=n1=n2
    print("Minimum:",z)

minimum()          

print("------------------------------------------------------------------------------------------")

# Topic :- Scope of Variable
#          -----------------

# Scope of the variable:- It is also called life of the variable which is up to the function in
# ----------------------  which it is defined.


# Consider the following function:-

def product():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    z=n1*n2

product()
print(z)

# Note:- Here, 'z' is local variable in the product function which cannot be accessible outside the
# function and it will give error.

print("------------------------------------------------------------------------------------------")

# Topic :- Arguments
#          ---------

# Argument of function(Parameterized function):- We can pass values to user define function while
# ---------------------------------------------  calling it,they are called as 'Arguments'. In the
# function definition we have to collect it in some variables which are called are 'Parameters'.
# This function is called as "Parameterized function".
                                           

# Q:- Define a Product function which accepts two values and gives its product.

def product(a,b): # Here a & b are Parameters.                                                      
    z=a*b
    print("Product of x and y:",z)

x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))

product(x,y) # Here x & y are Arguments.

print("------------------------------------------------------------------------------------------")

# Types of Argument:-
# -----------------

# 1. Positional Argument:- Arguments which are pass to the function in sequence are called
#    -------------------- 'Positional Argument' which can be collected in the respective position
#                          of parameters.


# Q:- Define a function which takes N as an argument and display 1 to N numbers.

def display(n):
    for i in range(1,n+1):
        print(i)

n=int(input("Enter the value of N:"))        
display(n)

print("------------------------------------------------------------------------------------------")

# 2. Default Argument:- If the parameters are initialized with some values then they are called
#    -----------------  'Default Argument'.


def add(a=2,b=3):
    z=a+b
    print("Addition:",z)

add()
add(10)
add(10,20)

print("\nQ1:- Define a function which takes two values and gives the Maximum.")
print("Q2:- Define a function which takes a number and gives its Factorial.")
print("Q3:- Define function which accepts a list as a parameter and find maximum element within list.")

print("\nAns1:-")

def display():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    if n1>n2:
        print("\nFirst Number is Maximum.")
    else:
        print("\nSecond Number is Maximum.")

display()        

print("\nAns2:-")

def fact():
    fact=1
    n=int(input("Enter a Number:"))
    for i in range(1,n+1,1):
        fact=fact*i
        print("Factorial:",fact)

fact()

print("\nAns3:- ")

def diplay():
    lst=[24,52,15,87,53,71]
    print("Maximum:",max(lst))

diplay()
 
print("------------------------------------------------------------------------------------------")

# 3. Arbitrary Arguments(*args):- Arbitrary arguments denoted as (*args). We can use any identifier 
#   ---------------------------   for args. If we don't know how many arguments we want to pass to
# the function then we can use *args. It is a Tuple which can contain all values.

# Q:- Define a function which accepts 5 values using *args.

def display(*args):
    print("All values are:",args)

display("Red",45,"Blue",6.78)    

# Note:- Here, Inside args values can be identify by their position which starts from 0.

# Q:- Display values inside args using For Loop. (Output will display vertically by default):-

def display(*args):
    for i in args:
        print(i)

display("\nRed",45,"Blue",6.78)        

print("------------------------------------------------------------------------------------------")

# 4. Key Worded Arguments(**Kwargs):- We can pass to the dictionary arguments in the form of key &
#    -------------------------------  value. These arguments will be collected in parameters called
# **kwargs which is nothing but a dictionary.

# Q:- Define a function which accepts Name and Marks of 3 students in key:value format.

def student(**kwargs):
    print("Student's data List:",kwargs)

student(Arajan=56,Wazar=23,Darjan=89)

# Display all names:-

def student(**kwargs):
    print("\nAll students names are:",kwargs.keys())

student(Arajan=56,Wazar=23,Darjan=89)

# Display names and marks of all students using For Loop:-

def student(**kwargs):
    print("\nAll students Names & Marks are:")
    for i in kwargs.items():
        print(i)

student(Arajan=56,Wazarh=23,Darjan=89)        

print("------------------------------------------------------------------------------------------")

# Topic :- Function with Return Value 
#          ---------------------------

# If we want to access the value of local variable of the function outside the function block then
# it should be return because the scope of local variable is upto the function in which it is define.

# Q:- Define a function which returns addition of two numbers to the calling block.

def addition():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    z=n1+n2
    return z
x=addition()
print("Addition:",x)

# Note:- here, n1, n2, z are Local Variable in the function addition.

# Q:- Define a function which takes marks of two subjects as parameters and returns total marks.
#     calculate average marks using total.

def getmarks(subject1,subject2):
    total_marks=subject1+subject2
    return total_marks

subject1=int(input("Enter the marks of subject1:"))
subject2=int(input("Enter the marks of subject2:"))

t=getmarks(subject1,subject2)
print("\nTotal Marks:",t)

avg=t/2
print("Average Marks:",avg)

# Q:- Define a function which takes two numbers and gives maximum number without using return.

def maximum():
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    if n1>n2:
        print("First number is Maximum.")
    else:
        print("Second number is Maximum.")

maximum()

# Q:- Define a function which takes a number and returns its Factorial.

def fact():
    n=int(input("Enter a Number:"))
    fact=1
    for i in range(1,n+1,1):
        fact=fact*i
    return fact

z=fact()
print("Factorial is:",z)

print("------------------------------------------------------------------------------------------")

# Topic:- Global Variable & Local Variable
#         ---------------------------------

# Global Variable:- It is a variable which is define outside any function block. We can print this
#                   variable in any function block but to make any change in this variable we have
# to define it as a Global Variable.

x=100

def function():
    global x
    x+=10 # make a change in global variable

function()
print("Outside function x:",x)

# Note:- The scope of global variable througout the program.

print("------------------------------------------------------------------------------------------")

# Topic:- Recursive Function
#        -------------------- 


# Recursive:- The function calling itself is called Recursive Function that is, if we write the
#             function calling then its recursive function.

# Structure of Recursive function:-

# 1. Base Case:- The condition that stops the infinite recursion.

# 2. Recursive Case:- The part where the function calls itself.

def display(n):
    if condition: # Base Case
        return
    else:
        return condition # Recursive Case

#--------------------------------------------------------------------------------------------------

# Q:- Define a recursive function which print 1 to 5 numbers.

def show(n):
    if n==6: 
        return 1
    else:
        print(n,end=" ")
        show(n+1)

print("Numbers are:")
show(1)

print("------------------------------------------------------------------------------------------")

# Q:- Define a recursive function which will return factorial of the given number.

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1) # Formula of Factorial:- n=n*(n-1)

print("Factorial:",fact(5))
'''

