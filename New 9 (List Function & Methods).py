# (List Function & Methods - 01):-

# What is List Function?

# A list is a collection of multiple values stored in a sequence. Lists are Mutable.


# Syntax :-

# List=[elements]
#   print()


# 01. Sum         :- (It gives sum of the elements.)
# 02. Min         :- (It gives the minimum element from the list.)
# 03. Max         :- (It gives the maximum element from the list.)
# 04. Len(length) :- (To count total number of elements in the list.)

# 05. Append      :- (To insert new element. It inserts at the last position of list.)
# 06. Insert      :- (To insert new element at the position given by user.) 
# 07. Pop         :- (It deletes the last index element by default.)
# 08. Remove      :- (It removes the element given by user to remove.)

# 09. Index       :- (To know the element's index position.)
# 10. Count       :- (It used to count elements given by user.)
# 11. Copy        :- (It creates a another duplicate list.)
# 12. Reverse     :- (To reverse the elements.)

# 13. Extend      :- (It adds the new element at the last position given by user.)
# 14. Sort        :- (It arranges the list into ascending and descending.)
# 15. Clear       :- (It deletes all the elements of the list.)
# 16. Del         :- (It deletes particular element given by user.)

'''
# 1. Sum :- 

lst=[99,82,57,36,89]
print('\nOriginal List:',lst)

print('Total:',sum(lst)) 

print("------------------------------------------------------------------------------------------")

# 2. Min :- 

lst=[23,75,69,35,10]
print('\nOriginal List:',lst)

print('Minimum:',min(lst))

print("------------------------------------------------------------------------------------------")

# 3. Max :- 

lst=[561,817,351,236,792]
print('\nOriginal List:',lst)

print('Maximum:',max(lst))

print("------------------------------------------------------------------------------------------")

# 4. Len (lenght) :-

lst=['Barnes','Aileen','Bethany','Tommy','Greg','Coltan','Peter']
print('\nOriginal List:',lst)

print('Number of Elements:',len(lst))

print("------------------------------------------------------------------------------------------")

# 5. Append :-

lst=['George',25,'Elija',35,'Zewer',85,'Walton',90,'Colofell',]
print('\nOriginal List:',lst)

lst.append(35)
print('Modified List:',lst)

print("------------------------------------------------------------------------------------------")

# 6. Insert :-

lst=[35,47,67,78,81]
print('\nOriginal List:',lst)

lst.insert(2,566)
print('Modified List:',lst)

print("------------------------------------------------------------------------------------------")

# 7. Pop :-

lst=[78,23,16,37,66]
print('\nOriginal List:',lst)

lst.pop()
print('Modified List:',lst)

print("------------------------------------------------------------------------------------------")

# 8. Remove :-

lst=[78,25,47,90,234]
print('\nOriginal List:',lst)

lst.remove(47)
print('Modified List:',lst)

print("------------------------------------------------------------------------------------------")

# 9. Index :-

lst=[788,655,251,549,315]
print('\nOriginal List:',lst)

print('Modified List:',lst.index(549))

print("------------------------------------------------------------------------------------------")

# 10. Count :-

lst=['Alice 26','Conner 25','Steve',35,'Alice 26','Conner 43']
print("\nOriginal List:",lst)

n=input("Enter a Number:")
print("In the above List",n,"repeated",lst.count(n),"times.")

print("------------------------------------------------------------------------------------------")

# 11. Copy :-

lst=['Jesica','Age',25,'Jason','Age',27,'Felladef',32]
print("\nOriginal List:",lst)

# List With Copy function:-

print("\nWith Copy Function:",lst.copy())

# List Without Copy function:-

ab=lst
print("Without Copy Function:",ab)

print("------------------------------------------------------------------------------------------")

# 12. Reverse :-

lst=[91,92,93,94,95,96,97,98,99,100]
print("\nOriginal Number:",lst)

lst.reverse()
print("Reverse Number:",lst)

print("------------------------------------------------------------------------------------------")

# 13. Extend :-

list1=['Qutalib',24,'Wazar',53,'Tylor',34,'Juliya',45]
print("\nOriginal List:",list1)

lst2=['George',55]

list1.extend(lst2)
print("Modified List:",list1)

print("------------------------------------------------------------------------------------------")

# 14. Sort :-

lst=[653,465,124,118,233,432]
print("\nOriginal List:",lst)

# Ascending Order:-

lst.sort()
print("\nAscending Order:",lst)

# Descending Order:-

lst.sort(reverse=True)
print("Descending Order:",lst)

print("------------------------------------------------------------------------------------------")

# 15. Clear :-

lst=[24,61,12,36,57,6,86,78,21,19,65]
print("\nOriginal List:",lst)

lst.clear()
print("Modified List:",lst)


print("------------------------------------------------------------------------------------------")

# 16. Del :-

lst=['Alice',23,'Harwad',25,'Jackson',35,'Leoshan',32]
print("\nOriginal List:",lst)

del lst[3]
print("Modified List:",lst)

print("------------------------------------------------------------------------------------------")


# (List Function & Methods - 02) (New Topic) :----->

# 1. Joining
# 2. Slicing
# 3. Replication (Repeat)

# ---------------------------

# 1. Joining

lst1=[45,96,85,43,12,35]

print('\nOriginal Number:',lst1)

lst2=['A','B']

print('\nAfter Joining List:',(lst1+lst2))

# ---------------------------

# 2. Slicing :- To access multiple elements according to given range.

# Syntax of Slicing :---->

#   variable[start:stop:step]

lst=['A','B',45,96,85,43,12,35,77,23,54,90,277,'C','D',66,33,251]

print('\nOriginal Number:',lst)

print('\nAfter Slicing List-1:',(lst[4:]))

print('\nAfter Slicing List-2:',(lst[:9])) # (Here lat index element is not include.)

print('\nAfter Slicing List-3:',(lst[2:10:3]))

# ---------------------------

# 3. Replication(Repeat)

lst=[45,96,85,43,12,35]

print('\nOriginal Number:',lst)

print('\nAfter Replication:',(lst*2))


# ------------------------------------------------------------

# Questions :--->

# Q-01. Create a lsit and print index wise element.
# Q-02. Create a list and print skip by 4 element.

# Ans-01.
lst=[20,50,72,14,298,89,90]
print('\nOriginal Number:',lst)

lst.sort()
print('\nAscending Order:',lst)

# Ans-02. 
lst=[20,50,72,14,298,89,90]
print('\nOriginal Number:',lst)

print('\nSkip by Four:',(lst[4:]))


# ------------------------------------------------------------

#(List Function & Methods - 03) (New topic)----->

# 1. Create a list according to the user using "For Loop".

# Method First :-

now=int(input("\nHow Many Elments Do You Want To Hold:"))
lst=[]

for p in range (now):
    s=int(input("Enter Element:"))
    lst.append(s)
print("\nList is Created")
print(lst)

# ---------------------------

# 2. Create a list according to the user using "While Loop".

# Method Second :-

now=int(input("\nHow Mnay Elements Do You Want To Hold:"))
lst=[]

while True:
    s=int(input("Enter Element:"))
    lst.append(s)
    ch=input("Continue Again Yes/No:")
    if ch=="no" or ch=="No":
        break
print("\nList is Created")
print(lst)

# ------------------------------------------------------------

# Questions :--->

# Q-01. Create a list and calculate Sum of all Elements.? 
# Q-02. Create a list and calculate Product of all Elements.?
# Q-03. Create a list count and count how many Positive and Negative Elements.?
# Q-04. Create a list calculate and count how many Odd and Even Elements.?
# Q-05. Create a list and print Traversing Order.?
# Q-06. Create a list and print Indexing wise Elements.?
# Q-07. Create a list and calculate Sum of all Even and Odd Elements Separatlly.?

# Ans-01.

lst=[22,76,45,86,94,54,70,158,124]
print('\nOriginal List:',lst)

print('Sum of Elements:',sum(lst))

# ---------------------------

# Ans-02.
def lstProduct(mylist):

    res=1
    for i in range (0,len(mylist)):
        res=res*mylist[i]
    print(res)
    
lst1=[22,76,45,86,94,124]
lst2=[45,76,45]

print(lstProduct(lst1))
print(lstProduct(lst2))

# ---------------------------
'''
# Ans-03.

lst1=[76,-18,45,99,-35,65,-88,-140,43,-589,352,75]
print('\nOriginal Number:',lst1)

pos_count, neg_count = 0,0

for num in lst1:
    if num >=0:
        pos_count += 1
    else:
        neg_count += 1

print('\nPositive Elements in the List :',pos_count)
print('Negative Elements in the List :',neg_count)

# ---------------------------

# Ans-04.

lst1=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,233]

print('\nOriginal Number:',lst1)

Even_count, Odd_count = 0,0

for num in lst1:
    if num%2==0:
        Even_count +=1
    else: 
        Odd_count +=1

    
print('\nEven Elements in the List:',Even_count)
print('Odd Elements in the List :',Odd_count)

# ---------------------------

# Ans-05.

number_list=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,18]
print('\nOriginal Number:',number_list)

def calculate_odd_even(odd_number,even_number):
    odd_number  = 0
    even_number = 0
    t1 = tuple()
    for i in number_list:
        if i % 2 == 0:
           even_number = even_number + number_list[i]
           t1.append(i)
        else: 
           odd_number = odd_number + number_list[i]
           t1.append(i)

    
    return odd_number
    return even_number
 

print("------------------------------------------------------------------------------------------")

# Questions:-

print("Q:- 1. Create a list of three persons with their age insert a new person in the list.")

# By using Append:--

lst=['Ravi',53,'Qurtalib',24,'Talib',30,'Harjan']
print("\nOriginal List:",lst)

lst.append(21)
print("Modified List:",lst)

# By using Insert:--

lst=['Ravi',53,'Qurtalib',24,'Talib',30,'Harjan']

lst.insert(7,21)
print("\nBy using Insert:",lst)

# By using Extend:--

lst2=["Alice",24]
lst.extend(lst2)
print("By using Extend:",lst)

print("------------------------------------------------------------------------------------------")
