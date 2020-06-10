#!/bin/python3
import sys #system functions and parameters
from datetime import datetime as dt #import with alias


print(sys.version)
print(dt.now())

my_name = "Alvaro"
print(my_name[0]) #prints first letter of my name
print(my_name[-1]) #prints last letter

sentence = "This is a sentence"
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = '' .join(sentence_split)
print(sentence_join)

quote = "He said, \"come over here\""
print(quote)

too_much_space = "        hello"
print(too_much_space.strip())

print ("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = "The Butler"
print("My favorite movie is {}.".format(movie))


#Dictionaries - Key/Value pairs {}
drinks = {"Jameson Whiskey":7,"Ciroc Vodka":10, "Old monk Rum":8}#drink is key price is value
print(drinks)

employees = {"Finance":["Dickson","Daniel","Fiona"],"IT":["Gene","Louise","Bob"], "HR": ["Martin"]}
print (employees)

drinks['Jameson Whiskey'] = 8
print(drinks)

print(drinks.get("Jameson Whiskey"))
