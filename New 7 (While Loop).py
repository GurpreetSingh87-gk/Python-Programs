# While Loop :-

# Syntax :-

# variable initialization 

# While condition:
#        statement
#        increment/decrement

# Questions:-
'''
print("Q-1. Print 1 to 10 Natural Numbers.")

start=1

while start<=10:
    print("Natural Numbers:",start)
    start=start+1

print("------------------------------------------------------------------------------------------")

print("Q-2. Print Sum of Natural Numbers from 1 to 10.")

i=1
sm=0

while i<=10:
    sm=sm+i
    i=i+1
    print("Natural Numbers:",i)

print("\nSum of Natural Number:",sm)

print("------------------------------------------------------------------------------------------")

print("Q-3. Print 1 to 10 Even Numbers.")

start=1

while start<=10:
    if start%2==0:
        print("Even Numbers:",start)
    start=start+1
        
print("------------------------------------------------------------------------------------------")

print("Q-4. Print 1 to 10 Odd Numbers.")

start=1

while start<=10:
    if start%3==0:
        print("Odd Numbers:",start)
    start=start+1
    
print("------------------------------------------------------------------------------------------")

print("Q-5. Display Sum of Even Numbers between 1 to 20.")

Even=1
sm=0

while Even<=20:
    if Even%2==0:     
        print("Even Numbers:",Even)
        sm=sm+Even
    Even=Even+1
    
print("\nSum of Even Numbers:",sm)

print("------------------------------------------------------------------------------------------")

print("Q-6. Display Sum of Odd Numbers between 1 to 30.")

Odd=1
sm=0

while Odd<=30:
    if Odd%3==0:
        print("Odd Numbers:",Odd)
        sm=sm+Odd
    Odd=Odd+1
print("\nSum of Odd Numbers:",sm)    

print("------------------------------------------------------------------------------------------")

print("Q-7. Write a program to display sum of even and odd numbers.")

Even=1

Odd=1

while Even<=20 and Odd<=30:
    if Even%2==0:
        if Odd%3==0:
            print("Odd no:",Odd)
        Odd=Odd+1
        print("Even no:",Even)         
    Even=Even+1    

print("------------------------------------------------------------------------------------------")

# Extra Questions :-

print("Q-8. Sum of natural numbers between 1 to N(Stop Point).")

N=int(input("Enter a Number:"))

start=1
sm=0
while start<=N:
    sm=sm+start
    start=start+1
    print(start)

print("\nSum of N numbers:",sm)

print("------------------------------------------------------------------------------------------")

print("Q-9. Enter a number and print it into reverse order.")

n=123456789
reverse=0
while n>0:
    d=n%10
    n=n//10
    reverse=reverse*10+d
print(reverse)    

print("------------------------------------------------------------------------------------------")

print("Q-10. Count Digits.")

n=int(input("Enter a Number:"))

cd=0

while n>0:
    d=n%10
    n=n//10
    cd+=1
print("Total Number of Digits:",cd) # It gives Total Number of Digits Like:- 12453=5  

print("------------------------------------------------------------------------------------------")

print("Q-11. Sum of Digits.")

n=int(input("Enter some Digits:"))
sod=0

while n>0:
    d=n%10
    n=n//10
    sod+=d
print("Sum of Digits:",sod) # It gives sum of Single Digits Like:- 1+2+3+4+1+0=11    
    
print("------------------------------------------------------------------------------------------")

print("Q-12. Multiplication of Digits.")

n=int(input("Enter some Digits:"))
mod=1

while n>0:
    d=n%10
    n=n//10
    mod*=d
print("Multiplication of Digits:",mod) # It Multiply Every Digits Like:- 1*2*5=10    

print("------------------------------------------------------------------------------------------")

print("Q-13. Enter a Number and Check it is Armstrong or Not.")

n=int(input("Enter a Number:"))

t=n
Arm=0

while n>0:
    d=n%10
    n=n//10
    Arm=Arm+(d**3)

if t==Arm:
    print(Arm,"is a Armstrong Number")

else:
    print(Arm,"isn't a Armstrong Number")

print("------------------------------------------------------------------------------------------")
'''
print("Q-14. Write a program to display the following statements using While Loop.")

print("\n1. First 10 Even Numbers.")
print("2. First 10 Odd Numbers.")
print("3. First 10 Natural Numbers.")
print("4. First 10 Whole Numbers.")
print("5. First 10 Factorial Numbers.")

print("\n(a) First 10 Even Numbers.")

start=1

while start<=10:
    if start%2==0:
        print(start)
    start=start+1

print("\n(b) First 10 Odd Numbers.")

start=1

while start<=10:
    if start%3==0:
        print(start)
    start=start+1    

print("\n(c) First 10 Natural Numbers.")

start=1

while start<=10:
    print(start)
    start=start+1

print("\n(d) First 10 Whole Numbers.")

start=0

while start<=10:
    print(start)
    start=start+1

print("\n(e) First 10 Factorial Numbers.")

n=int(input("Enter a Number:"))
cf=1

while n>0:
    cf=cf*n
    n=n-1
print("Factorial is:",cf) # Formula of Factorial:- n!= n*(n-1)*(n-2)*(n-3)......   
                          #                        4 = 4*3*2*1= 24
