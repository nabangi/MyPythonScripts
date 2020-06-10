#!/bin/python3

#variables and methods
quote = "All is fair in love and war."
print(quote)
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #titlecase

print(len(quote))

name = "Alvaro" #string
age = 26 #int int(26)
height = 5.8 #float float(5.8)

print(int(age))
print("my name is "+ name + " and I am " + str(age) + " years old.")

age += 1
print (age)

print('\n')
#Functions
print("Here is an example of a function:")

def who_am_i(): #this is a function
	name = "Alvaro"
	age = 26
	print("my name is "+ name + " and I am " + str(age) + " years old.")
	
who_am_i()

#adding parameters
def add_one_hundred(num):
	print(num+ 100)
	
add_one_hunfred(100)

#mutliple parameters
def add(x,y):
	print(x + y)

add(7,7)

def multiply(x,y):
	return x * y
	
print(multiply(7,7))

def square_root(x):
	print(x ** .5)
	
square_root(64)

def nl():
	print('\n')

nl()

#Boolean expressions (True or False)
print("Boolean Expressions")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

nl()
#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 <7) #True
test_and2 = (7 > 5) and (5 < 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False

#Conditional Statements
def drink(money):
	if money >= 2:
		return "You got yourself a drink"
	else:
		return "No drink for you!"
		
print(drink(3))
print((1))

def alcohol(age,money):
	if (age >=18) and (money >= 2):
		return "We're getting a drink!"
	elif (age >= 18) and (money < 2):
		return "Come back with more money pal:)"
	elif (age < 18) and (money >= 2):
		return "Nice try, Kido!"
	else:
		return "You're damn broke and too young!"
		
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))

nl()
#Lists - Have Brackets [](mutable - can be changed)
movies = ["Shawshunk Redemption", "Vantage Point", "Salt","American Gangster","Inception"]

print(movies[1]) #return second item
print(movies[0]) #returns first item in list
print(movies[1:4])
print(movies[1:])
print(movies[:2])
print(movies[-1]) #returns last item

print(len(movies))
movies.append("Exorcist")
print(movies)

movies.pop()
print(movies)

print.pop(0)
print(movies)

nl()
#Tuples - immutable, Do not change and use parentheses ()
grades = ("A","B","C","D")
print(grades[1])

nl()
#Looping

#For loops - start to finish of an iterate
vegetables = ["cucumber","spinach","tomatoes"]
for x in vegetables:
	print(x)
	
#while loops - Execute as long as true

i = 1

while i < 10:
	print(i)
	i += 1
	
