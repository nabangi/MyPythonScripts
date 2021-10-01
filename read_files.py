
employee_file = open("../employees.txt", "r") #Read
print(employee_file.readable()) #check if file is readable
print(employee_file.read())
print(employee_file.readline()) #read firstline in that order
print(employee_file.readlines()[1])# will display lines in an array

for employee in employee_file.readlines(): #additional filter by employee
    print(employee)

employee_file.close()

open("/opt/employees.txt", "w") #Write
open("employees.txt", "a") #Append
open("employees.txt", "r+")#Read&Write