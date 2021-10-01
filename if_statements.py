    #Using Boolean
is_cold = False
is_windy = True

if is_cold and is_windy:
    print("It is cold and Windy")
elif is_cold and not (is_windy):
    print("It is just chilly not windy")
elif not(is_cold) and is_windy:
    print("It is not cold but windy")
else:
    print("It is neither cold, windy nor both")
if is_cold or is_windy:
    print("It is either cold, windy or both")
else:
    print("It is neither cold nor windy")

    #if_statements and Comparisons (using comparison operators e.g > = < == !=)

def max_num(num1, num2, num3):
    if num1 >= num2 and num1>= num3: 
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2 
    else:
        return num3

print(max_num(12, 21, 27))
