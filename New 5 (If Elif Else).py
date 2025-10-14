# If Elif Else :-

# Snytax:-

# if condition:
#   statement

# elif condition:
#   statement

# else:
#   satement

# Questions:-
'''
print(" Q-1. Input any character and check whether it is vowel or consonent.")

ch=input("Enter Character:")

if ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
    print("Its Vowel") 

else:
    print("Its Consonent")

print("-----------------------------------------------------------------------------------------")

print(" Q-2. Find the Maximum number between 3 numbers")

X=int(input("Enter First Number X:"))
Y=int(input("Enter Second Number Y:"))
Z=int(input("Enter Third Number Z:"))

if X>Y and X>Z:
    print("X is greater")

elif Y>X and Y>Z:
    print("Y is grater")

else:
    print("Z is greater")

print("-----------------------------------------------------------------------------------------")

print("Q-3. Check the given number whether it is Zero, Positive or Negative ")

n=int(input("Enter a Number:"))

if n==0:
    print("This number is Zero")

elif n>0:
    print("This number is Positive")

else:
    print("This number is Negative")

print("-----------------------------------------------------------------------------------------")

print("Q-3. Input a number and check whether it is Even or Odd.")

n=int(input("Enter a Number:"))

if n%2==0:
    print("This number is Even")

elif n%3==0:
    print("This number is Odd")

else:
    print("This is Invalid")

print("-----------------------------------------------------------------------------------------")

print("Q-4. Input marks of 3 subjects and calculate Total marks, Average marks and display the")
print("     Grade according to following condition:-\n")

print("1. If grade is in between 80 to 100 then give 'A' ")
print("2. If grade is in between 60 to 80 then give 'B' ")
print("3. If grade is in between 40 to 60 the give 'C' ")
print("4. If grade is in between 33 to 40 then give 'D' ")
print("5. If grade is less then 33 give 'Fail' or 'Compartment'\n ")

English=int(input("Enter the marks of English:"))
Maths=int(input("Enter the marks of Maths:"))
Science=int(input("Enter the marks of Science:"))

Total_Marks=English+Maths+Science

print("\nTotal Marks:",Total_Marks)

Average_Marks=Total_Marks/3

print("Average Marks:",Average_Marks)

if Average_Marks>=80 and Average_Marks<=100:
    print("Grade A")

elif Average_Marks>=60 and Average_Marks<=80:
    print("Grade B")

elif Average_Marks>=40 and Average_Marks<=60:
    print("Grade C")

elif Average_Marks>=33 and Average_Marks<=40:
    print("Grade D")

else:
    print("Fail or Compartment")

print("-----------------------------------------------------------------------------------------")

print("Q-5. Input Basic Salary and calculate Gross-Salary according to the following conditions:-\n")

print("1. Basic Salary is 15,000 to 20,000 and TA 10%, HRA 15%")

print("2. Basic Salary is 20,000 to 25,000 and TA 15%, HRA 20%")

print("3. Greater than 25,000 and TA 20%, HRA 30%\n")

Basic_Salary=int(input("Enter Basic Salary:"))

if Basic_Salary>=15000 and Basic_Salary<=20000:
    TA=(Basic_Salary*10)/100
    HRA=(Basic_Salary*15)/100

elif Basic_Salary>=20000 and Basic_Salary<=25000:
    TA=(Basic_Salary*15)/100
    HRA=(Basic_Salary*20)/100

elif Basic_Salary>=25000:
    TA=(Basic_Salary*20)/100
    HRA=(Basic_Salary*30)/100

Gross_Salary=Basic_Salary+TA+HRA

print("\nTravel Allowance    :",TA)
print("House Rent Allowance:",HRA)    
print("Gross-Salary        :",Gross_Salary)

print("-----------------------------------------------------------------------------------------")

print("Q-6. Write a programm to display Alphabet, Character and Digit")

Ch=input("Enter Alphabet/Character/Digit:")

if Ch>='A' and Ch<='Z':
    print("Its Alphabet")

elif Ch>='0' and Ch<='9':
    print("Its Digit")

else:
    ("Its a Special Symbol") 

print("-----------------------------------------------------------------------------------------")

print("Q-7. Enter a number and check whether the number is Positive or Negative using")
print("     Logical 'Not' operator.")  


n=int(input("Enter a Number:"))

if not n>0:
    print("Its Positive")# 34 (It will show Negative)

else:
    print("Its Negative")# -34 (It will show Positive)

print("-----------------------------------------------------------------------------------------

# Extra Questions :- 

print("Q-1. Enter week number & print week days ?")

Week_Number=input("Enter Week Number:")

if Week_Number=="Week of the Month":
    print("No. of days: 7 days")
    
elif Week_Number in ("1st week of the month"):
    print("No. of days: 7 days")

elif Week_Number in ("2st week of the month"):
    print("No. of days: 7 days")

elif Week_Number in ("3st week of the month"):
    print("No. of days: 7 days")

elif Week_Number in ("4st week of the month"):
    print("No. of days: 7 days")

else:
    print("Invalid Week")

print("-----------------------------------------------------------------------------------------")

print("Q-2. Enter month name & print total number of days ?")

Month_Number=input("Enter Month Name:")

if Month_Number=="February":
    print("No. of days: 28 or 29 days")

elif Month_Number in ("April","June","September","November"):
    print("No. of days: 30 days")

elif Month_Number in ("January","March","May","July","August","October","December"):
    print("No. of days: 31 days")

else:
    print("Invalid Week")

print("-----------------------------------------------------------------------------------------")

print("Q-03. Enter a number & check number is Positive, Negative or Zero using if-elif-else?")

n=int(input("Enter a Number:"))

if n>0:
    print("Its Positive")

elif n<0:
    print("Its Negative")
      
elif n==0:
    print("Its Zero")

else:
    print("It isn't Positive or Negative or Zero")

print("-----------------------------------------------------------------------------------------")

print("Q-04. Enter 5 subjects marks and calculate their total marks & average marks. Give grade")
print("      according to the following conditions:-\n")

print("1. If average marks is > 90 print A")
print("2. If average marks is > 75 print B")
print("3. If average marks is > 60 print C")
print("4. If average marks is > 50 print D otherwise F\n")

Internet_Of_Things=int(input("Enter IOT's Marks:"))
Web_Designing=int(input("Enter Web Designing's Marks:"))
Python=int(input("Enter Python's Marks:"))
Java=int(input("Enter Java's Marks:"))
IT_Tools=int(input("Enter IT Tool's Marks:"))

Total_Marks=Internet_Of_Things+Web_Designing+Python+Java+IT_Tools

print("\nTotal Marks:",Total_Marks)

Average_Marks=Total_Marks/5

print("Average Marks:",Average_Marks)


if Average_Marks>=90:
    print("\nGrade A")

elif Average_Marks>=75:
    print("Grade B")

elif Average_Marks>=60:
    print("Grade C")

elif Average_Marks>=50:
    print("Grade D")

else:
    print("Grade F")
    
print("-----------------------------------------------------------------------------------------")

print("Q-05 Enter a number if number is less than 10 then print 'one digit', if number is")
print("     greater than or equal to 10 but less than 100 then print 'two digit' otherwise")
print("     'integer'.")

n=int(input("Enter a Number:"))

if n<10:
    print("One Digit")

elif n>=10 and n<100:
    print("Two Digit")

else:
    print("Integer")

print("-----------------------------------------------------------------------------------------")

print("Q-06. Enter a number if number is Even and also divisible by 3 print 'Number is even and")
print("     also divisible by 3'. If number is even but not divisible by 3 print 'Number is")
print("     even but not divisible by 3' otherwise print 'Odd number'")
     
n=int(input("Enter a Number:"))
if n%2==0:
    if n%3==0:
        print("Number is Even and also divisible by 3")
    else:
        print("Number is Even but not divisible by 3")

else:
    print("Number is Odd")

print("-----------------------------------------------------------------------------------------")

print("Q-07. Enter temperature in centigrade and display a suitable message according to the")
print("      temperature state below:-\n")
      
print("1. Temperature less than 0 then Freezing Weather.")
print("2. Temperature 0 to 10 then Very Cold Weather.")
print("3. Temperature 10 to 20 then Cold Weather.")
print("4. Temperature 20 to 30 then Normal in Temperature.")
print("5. Temperature 30 to 40 then Its Hot.")
print("6. Temperature greater than 40 then Its Very Hot.\n")

Temperature=int(input("Enter Weather:"))

if  Temperature<0:
    print("Freezing Weather")

elif Temperature>=0 and Temperature<=10:
    print("Very Cold Weather")

elif Temperature>=10 and Temperature<=20:
    print("Cold Weather")

elif Temperature>=20 and Temperature<=30:
    print("Normal in Temperature")

elif Temperature>=30 and Temperature<=40:
    print("Its Hot")
    
elif Temperature>=40:
    print("Its Very Hot")

else:
    print("No Weather")


print("-----------------------------------------------------------------------------------------")

print("Q-08. Enter 3 number & find which one is greater?")

# With 'Elif' Function:-

n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))

if n1>n2:
    print("First Number is greater.")

elif n2>n3:
    print("Second Number is greater.")

else:
    print("Third Number is greater.")

# With 'And' Logical Operator:-

n1=int(input("\nEnter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))

if n1>n2 and n1>n3:
    print("First Number is greater.")

elif n2>n3 and n2>n1:
    print("Second Number is greater.")

else:
    print("Third Number is greater.")

print("-----------------------------------------------------------------------------------------")

print("Q-9. Write a program and diplay days name.")

Days=input("Enter Days Number:")
    
if Days=="Days_Name":
    print("No of days 7")

elif Days in ("1st Day"):
    print("Monday")

elif Days in ("2nd Day"):
    print("Tuseday")

elif Days in ("3rd Day"):
    print("Wednesday")

elif Days in ("4th Day"):
    print("Thursday")

elif Days in ("5th Day"):
    print("Friday")

elif Days in ("6th Day"):
    print("Saturday")

elif Days in ("7th Day"):
    print("Sunday")

else:
    print("Invalid Days Name")

print("-----------------------------------------------------------------------------------------")

print("Q-10. Enter a date of particular month and display the 'Day/Month/Year' of that month.")

Date=input("Enter a Date:")

if Date=="Days_Name":
    print("No of days 31")

elif Date in ("Monday"):
    print("01-01-2025")
    
elif Date in ("Tuseday"):
    print("02-01-2025")

elif Date in ("Wednesday"):
    print("03-01-2025")

elif Date in ("Thursday"):
    print("04-01-2025")

elif Date in ("Friday"):
    print("05-01-2025")

elif Date in ("Saturday"):
    print("06-01-2025")

elif Date in ("Sunday"):
    print("07-01-2025")

else:
    print("Invalid Date")










