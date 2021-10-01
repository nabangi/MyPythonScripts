
employee_file = open("employees.txt", "w") #help create new file as well
#employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Devops Department") #'\n' an escape character to ensure the input goes to the last entry
employee_file.close()