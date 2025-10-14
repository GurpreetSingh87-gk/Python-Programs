# Nested if else :-

# Syntax:-

# if conditon (1):
#   if condition (2):
#       statement (1)
#   else:
#       statement (2)

# else:
#   if condition (3):
#       statement (3)
#   else:
#       statement (4)


# Questions:-
'''
print("Q-1. Program to find your grade accoding to following condition.")

print("1. Above 90 - grade A+")
print("2. Above 80 - grade A")
print("3. Above 70 - grade B")
print("4. Above 60 - grade C otherwise Fail")


Grade=int(input("\nEnter Marks:"))

if Grade>=90:
    print("Grade A+")
else:
    if Grade>=80:
        print("Grade A")
    else:
        if Grade>=70:
            print("Grade B")
        else:
            if Grade>=60:
                print("Grade C")
            else:
                print("Fail")

print("------------------------------------------------------------------------------------------")

print("Q-2. Write a program to find given year is leap year or not.")

Year=int(input("Enter Any Year:"))

if Year%4==0:
    if Year%100==0:
        if Year%400==0:
            print("This is a Leap Year.")
        else:
            print("This is not a Leap Year.")
    else:
        print("is not a Leap Year.")
else:
    print("Is not a Leap Year.")

print("------------------------------------------------------------------------------------------")

print("Q-3. Enter a number if number is Even and also divisible by 3 print 'Number is even and")
print("     also divisible by 3'. If number is even but not divisible by 3 print 'Number is even")
print("     but not divisible by 3' otherwise print 'Odd number'.")

n=int(input("Enter a Number:"))

if n%2==0:
    if n%3==0:
        print("Number is Even and also divisible by 3")
    else:
        print("Number is Even but not divisible by 3")
else:
    print("Odd number")

print("------------------------------------------------------------------------------------------")
'''
print("Q-4. 

