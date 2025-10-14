 # If & Else :-

# Syntax:-

# if condition:
#    statement

# else:
#    statement

# Questions :-
'''
print("Q-1. Enter the age of a person and display the message if he is 18 years of age or more than 18 ")
print("     then print 'person can vote'. If he is below 18 then print 'person can not vote'.")    

age=int(input("\nEnter the Age:"))

if age>=18:
    print("\nThis Person Can Vote:",age)
else:
    print("This Person Can't Vote:",age)

print("------------------------------------------------------------------------------------------")

print("Q-2. Input the Basic Salary of an employee and calculate gross-salary.")
print("     The TA is 10% of basic salary and HRA is 15% of basic salary.")


BS=int(input("\nEnter the Salary of Employee:"))

TA=(BS*10)/100
HRA=(BS*15)/100

GS=BS+TA+HRA

print("\nTravel Allowance     :",TA)
print("House Rent Aollwance :",HRA)
print("Gross-Salary         :",GS)

print("------------------------------------------------------------------------------------------")

print("Q-3. Enter the price of each item and number of items purchased and calculate the total bill.")

item1=int(input("\nEnter the Price of Item :"))
item2=int(input("Enter the Price of Item :"))
item3=int(input("Enter the Price of Item :"))
item4=int(input("Enter the Price of Item :"))
item5=int(input("Enter the Price of Item :"))

TB=item1+item2+item3+item4+item5

Total_Items=item1,item2,item3,item4,item5

print("\nNumber of Items Purchased:",len(Total_Items))
print("Total Bill:",TB)

print("------------------------------------------------------------------------------------------")

print("Q-4. Input any numbers and find positive and negative number.")

n=int(input("Enter Number:"))

if n>=0:
    print("This number is Positive")

else:
     print("This number is Negative")

print("------------------------------------------------------------------------------------------")

print("Q-5. Input marks of 3 subjects and calculate Total marks, Average marks and display")
print("     the result 'Pass' if average is 40 or more than 40 otherwise diplay 'Fail'.")   

English=int(input("Enter the Marks:"))
Maths=int(input("Enter the Marks:"))
Science=int(input("Enter the Marks:"))

TM=English+Maths+Science

AM=TM/3

print("Total Marks:",TM)
print("Average Marks:",AM)

if AM>40:
    print("Result:Pass")

else:
    print("Result:Fail")

print("------------------------------------------------------------------------------------------")

print("Q-6. Enter two numbers and find maximum/greater between them")

n1=int(input("Enter 1st Number:"))
n2=int(input("Enter 2nd Number:"))

if n1>n2:
    print("1st Number is Greater")

else:
    print("2nd Number is Greater")
    
print("------------------------------------------------------------------------------------------")

# Extra Questions:-

print("Q-7. Enter a number & check number is Even or Odd ?")

n=int(input("Enter the Number:"))

if n%2==0: 
    print("The Number is Even")

else:
    print("The Number is Odd")

print("------------------------------------------------------------------------------------------")

print("Q-8. Enter two numbers & check both numbers are equal or not ?")

n1=int(input("Enter 1st Number:"))
n2=int(input("Enter 2nd Number:"))

if n1==n2:
    print("Both Numbers are Equal")

else:
    print("Both Numbers aren't Equal")

print("------------------------------------------------------------------------------------------")

print("Q-9. Enter 5 subjects marks & calculate total marks & average marks if average marks is")
print("     greater than 33 then print 'Pass' otherwise 'Fail'.")   

English=int(input("\nEnter the Marks of English:"))
Hindi=int(input("Enter the Marks of Hindi:"))
Maths=int(input("Enter the Marks of Maths:"))
Science=int(input("Enter the Marks of Science:"))
Punjabi=int(input("Enter the Marks of Punjabi:"))

TM=English+Hindi+Maths+Science+Punjabi

AM=TM/5

print("\nTotal Marks:",TM)

print("Average Marks:",AM)

if AM>33:
    print("Result:Pass")

else:
    print("Result:Fail")

print("------------------------------------------------------------------------------------------")

print("Q-10. Enter a number, if number is greater than 50 calculate Square otherwise Cube.")

n=int(input("\nEnter a Number:"))

if n>50:
    print(n,"is greater than 50") 

else:
    print(n,"is not greater than 50")

Square=n*n
print("\nSquare is:",Square)

n=int(input("\nEnter a Number:"))

if n>50:
    print(n,"is greater than 50") 

else:
    print(n,"is not greater than 50")

Cube=n*n*n
print("Cube is:",Cube)

print("------------------------------------------------------------------------------------------")

print("Q-11. Enter salary, if salary is greater than 55000 calculate HRA of 4% and MA of 6%")
print("      otherwise HRA of 2% and MA of 3% and calculate total salary.")
      
Salary=int(input("Enter the Salary:"))

if Salary>55000:
    HRA=(Salary*4)/100
    MA=(Salary*6)/100

else:
    HRA=(Salary*2)/100
    MA=(Salary*3)/100

TS=Salary+HRA+MA
print("House Rent Allowance:",HRA)
print("Medicial Allowance  :",MA)
print("Total Salary        :",TS)

print("------------------------------------------------------------------------------------------")

