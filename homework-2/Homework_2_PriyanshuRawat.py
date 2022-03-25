#QUESTION 1

i = 2000
List = []
#Loop to find desired numbers b/w 2000 and 3201 (both included)
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        List.append(i)
    i = i +1
print(List) #Prints desired numbers

#QUESTION 2

n = int(input('Enter a postive integer: '))
m=n-1
Factorial = n
if n>0:
    while m>0:
        Factorial = Factorial*m
        m=m-1
    print('The Factorial of ' + str(n) +' is ' + str(Factorial))
elif n==0:
    print('The Factorial of ' + str(n) +' is ' + str(1))
else:
    print ('Invalid Number; Enter a Positive Integer.')

#QUESTION 3

Number = int(input('Enter a Number: '))
Dictionary = {}
n=1
while Number>=n:
    Square = n*n
    Dictionary.update({n:Square})
    n=n+1
print (Dictionary)

#QUESTION 4

Input = input("Enter comma-seprated numbers :")
List = Input.split(",")
Tuple = tuple(List)
print('List : ',List)
print('Tuple : ',Tuple)

#QUESTION 5

class Demo_Class():
    def __init__(self):
        self.str_1 = ""
    def getString(self):
        self.str_1 = input("Type a string: ")
    def printString(self):
        print(self.str_1.upper())

str_1 = Demo_Class()
str_1.getString()
str_1.printString()

#QUESTION 6

import math
C = 50
H = 30
numbers = input('Enter numbers: ')
numbers = numbers.split(",")
print(numbers)
answers = []
for D in numbers:
    D = float((D))
    Q = answers.append(round(math.sqrt((2*C*D) / H)))
print(answers)

#QUESTION 7

X = int(input('Enter X: '))
Y = int(input('Enter Y: '))
Array = [[0 for j in range(Y)] for i in range(X)]
for i in range(X):
    for j in range(Y):
        Array[i][j]=i*j
print(Array)

#QUESTION 8

X=sorted(input('Enter Words: ').split(","))
print(X)

#QUESTION 9

X=input('Enter words to be capitilized:' )
X = X.upper()
print(X)

#QUESTION 10

Input=input('Enter:' ).split(" ")
Words = []
for i in Input:
    if i not in Words:
        Words.append(i)
    else:
        continue
Words.sort()
print((' ').join(Words))

#QUESTION 25

class student:                      # defining a class
    name = "Student"                # 'name' is the class parameter

    def __init__(self, name=None):
        self.name = name            # self.name is the instance parameter

#QUESTION 35

def mydict():
    dict = {}
    n = 1
    while n <= 20:
        dict.update({n: n**2})
        n = n+1
        values = dict.values()
    print(values)
mydict()

#QUESTION 36

def mydict():
    dict = {}
    n = 1
    while n <= 20:
        dict.update({n: n**2})
        n = n+1
        keys = dict.keys()
    print(keys)
mydict()

#QUESTION 37

def print_squared_list():
    list = []
    for n in range (1,21):
        list.append(n**2)
    print (list)
print_squared_list()

#QUESTION 43

given_tuple = (1,2,3,4,5,6,7,8,9,10)
even_list = []
for i in given_tuple:
    if i % 2 == 0:
        even_list.append(i)
even_tuple = tuple(even_list)
print(even_tuple)
print(type(even_tuple))

#QUESTION 51

class American():
    pass
class NewYorker(American):
    pass

american = American()
newyorker = NewYorker()

print(american)
print(newyorker)

#QUESTION 53

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def area_of_rectangle(self):
        return self.length*self.width

rectangle_1 = Rectangle(12, 10)
print(rectangle_1.area_of_rectangle())

#QUESTION 54

class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length
    def area(self):
        return self.length * self.length

print(Square().area())  # prints zero as default area
area_of_square = Square(10)
print(area_of_square.area())  # prints 100 as per given argument

#QUESTION 56

def compute():
    return 5 / 0
try:
    divide()
except ZeroDivisionError as e:
    print("Error...diving a number by Zero!")
except:
    print("Other exception")

#QUESTION 94

def remove_duplicate_items(lists):
    new_list=[]
    seen = set()
    for item in lists:
        if item not in new_list:
            new_list.append(item)
    return new_list

list=[12,24,35,24,88,120,155,88,120,155]
print(remove_duplicate_items(list))    #prints the list after removing all duplicate values with original order reserved