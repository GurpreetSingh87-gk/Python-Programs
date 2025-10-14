# Dictionary Functions :-

# It is a built-in function that help to work with dictionaries, which store key-value pairs.

# Dictionary Functions :-

# 01. dict()             :- Create a new dictionary.
# 02. len(dict)          :- Returns the number of key-value pairs.
# 03. dict.keys()        :- Returns all keys in the dictionary.
# 04. dict.values()      :- Returns all values in the dictionary.

# 05. dict.items()       :- Returns all key-value pairs as tuples.
# 06. dict.get()         :- Returns value for the given key or default if not found.
# 07. dict.update()      :- Updates the dictionary with another dictionary.
# 08. dict.pop()         :- Removes and returns the value of the given key.

# 09. dict.popitem()     :- It removes the last key-value pair.
# 10. dict.clear()       :- It removes all items from the dictionary.
# 11. dict.copy()        :- It creates a another duplicate dictionary.
# 12. dict.setdefault()  :- Returns value for key if missing inserts key with default value.


# Syntax of Dictionary :-

# dict={key:value}

#-------------------------------------------------------------------------------------------------
'''
# 1. dict():- 

# Create an empty dictionary:-

my_dict=dict{}
print("Empty List:",my_dict)

# Creating dictionary with key-value pairs:-

my_dct=dict(Name='Alice',Age=25,City='New York')
print("\nModified Dictionary:",my_dct)

# Creating a list of Tuples into a dictionary:-

list_of_tuples=[('Name','Alice'),('Age',24),('City','Los Santos')]

my_dict=dict(list_of_tuples)
print("\nModified Dictionary:",my_dict)

print("\n----------------------------------------------------------------------------------------")

#  2. len(dict):- 

my_dict={"Qartlib":12,"Arjan":24,"Sarjan":53}
print("Original Dictionary:",my_dict)

print("\nModified Dictionary:",len(my_dict))

print("\n----------------------------------------------------------------------------------------")

# 3. dict.keys():- 

student={"Dinesh":67,"Yogesh":56,"Pooja":78}
print("Original Dictionary:",student)

print("\nModified Dictionary:",student.keys())

print("\n----------------------------------------------------------------------------------------")

# 4. dict.values():-

student={"Dinesh":35,"Frajan":13,"Hagar":63,"Targab":87}
print("Original Dictionary:",student)

print("\nModified Dictionary:",student.values())

# To find the value of key:-

student={"Dinesh":67,"Yogesh":56,"Pooja":78}
print("\nOriginal Dictionary:",student)

print("\nModified Dictionary:",student["Yogesh"])

print("\n----------------------------------------------------------------------------------------")

# 5. dict.items():-

student={'Alice':35,'Geroge':13,'Harry':63,'Targab':87}
print("Original Dictionary:",student)

print("\nModified Dictionary:",student.items())

# To run this using For Loop:-

for i in student.items():
    print("\n",i)

print("\n----------------------------------------------------------------------------------------")

# 6. dict.get():-

my_list={'Name':'Hzzra','Age':32,'City':'California'}
print("Original Dictionary:",my_list)

# First Method to use get function:-

print("\nModified Dictionary:",my_list.get("Name",0))

# Second Method to use get function using if else:-

m=my_list.get("City",0)

if m==0:
    print("Key Not Found")

else:
    print("\nKey Found:",m)
      
print("\n----------------------------------------------------------------------------------------")

# 7. dict.update():-

student={"Dinesh":67,"Yogesh":56,"Pooja":78}
print(student)

# First Way to update dictionary:-

student.update({"Emma":56})
print(student)

# Second Way to update dictionary using For Loop:- ")

for i in range(1):
    n=input("Enter Name:")
    m=int(input("Enter Marks:"))
    student.update({n:m})
print(student) 

# To search student name in dictionary:-

student={}
num=int(input("Enter Number of Students:"))

for i in range(num):
    n=input("Enter Name:")
    m=int(input("Enter Marks:"))
    student.update({n:m})

name=input("Enter the Name to Search:")

if name in student:
    print("Student Found")

else:
    print("Student Not Found")

print("\n----------------------------------------------------------------------------------------")
'''
# 8. dict.pop():-

dct_list={'Karjila':31,'Farang':51,'Haraf':12,'Chasarn':87}
print("Original Dictionary:",dct_list)

dct_list.pop("Farang")
print("\nModified Dictionary:",dct_list)      

'''
print("\n----------------------------------------------------------------------------------------")

# 9. dict.popitem():-

my_dct={'Name':'Garrison','Age':31,'City':'Brampton'}
print("Original Dictionary:",my_dct)

my_dct.popitem()
print("\nModified Dictionary:",my_dct)


print("\n----------------------------------------------------------------------------------------")

# 10. dict.clear():-

my_dct={'Harry':24,'Garrsion':34,'Jackson':26,'Manglo':87}
print("Original Dictionary:",my_dct)

my_dct.clear()

print("\nModified Dictionary:",my_dct)


print("\n----------------------------------------------------------------------------------------")

# 11. dict.copy():-

student_list={'Name':'Ethan','Marks':89,'Class':'12th','Section':'D'}
print("Original Dictionary:",student_list)

student.copy()

print("\nModified Dictionary:",student_list)


print("\n----------------------------------------------------------------------------------------")

# 12. dict.setdefault(key,value):-

rollno_list={1:'Rehan',2:'Joseph',3:'Gerry'}
print("Original Dictionary:",rollno_list)

rollno_list.setdefault(4,'Sen al hadin')

print("\nModified Dictionary:",rollno_list)

print("\n----------------------------------------------------------------------------------------")

# Questions:-

print("Q-1")
'''


