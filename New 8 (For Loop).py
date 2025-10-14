# For Loop :-

# Syntax :-

# for variable_name in range(start,stop,step):
#       statement


# Hetrogenious:- int,float,str.

# What is Range?:- It is used to generate the range of numbers between given range. It accepts only
#                  integers(whole numbers).



# Questions:-   
'''
print("Q-1. Print 1 to 10 numbers using For Loop.")

for a in range(1,11,1):
    print(a)

print("------------------------------------------------------------------------------------------")

print("Q-2. Print 10 to 1 numbers using For Loop.")

for s in range(10,0,-1):
    print(s)

print("------------------------------------------------------------------------------------------")

print("Q-3. Write a program to display Even Numbers using For Loop.")

for i in range(2,21,2):
    print(i)

print("------------------------------------------------------------------------------------------")

print("Q-4. Write a program to display Odd Numbers using For Loop.")

for i in range(3,31,3):
    print(i)

print("------------------------------------------------------------------------------------------")

print("Q-5. Print Even Numbers Reverse using For Loop.")

for q in range(20,1,-2):
    print(q)

print("------------------------------------------------------------------------------------------")

print("Q-6. Print Odd Numbers Reverse using For Loop.")

for q in range(30,2,-3):
    print(q)

print("------------------------------------------------------------------------------------------")

print("Q-7. Display the Factorial Numbers using For Loop.")

n=int(input("Enter a Number:"))
fact=1

for s in range(1,n+1,1): # Factorial:- 5*4*3*2*1
    fact=fact*s
    print("Factorial is:",fact)

print("------------------------------------------------------------------------------------------")

print("Q-8. Print 1 to N numbers using For Loop.")

n=int(input("Enter a Number:"))

for e in range(1,n,1):
    print(e)

print("------------------------------------------------------------------------------------------")

print("Q-9. Print Even Numbers using For Loop and If function.")

for w in range(2,21): # Second Method to print Even & Odd Numbers.
    if w%2==0:
        print("Even Numbers:",w)

print("------------------------------------------------------------------------------------------")

print("Q-10. Print Odd Numbers using For Loop and If function.")

for w in range(3,31):
    if w%3==0:
        print("Odd Numbers:",w)
        
print("------------------------------------------------------------------------------------------")
'''
print("Q-11. Write a program to execute 1 to N numbers divisible by 3 and 6.")

n=int(input("Enter a Number:"))

for g in range(1,n+1):
    if g%3==0 and g%6==0:
        print(g,"number is divisible by 3 and 6.")
    
print("------------------------------------------------------------------------------------------")


