# Exercise 9 - Is a member
# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)
def is_member(value=int(input('enter the number '))):
    input_list = []
    lenght_of_the_list = int(input('enter the lenght of the list : '))
    for number in range(0, lenght_of_the_list, 1):
        input_number = int(input(f'enter the {number+1} number : '))
        input_list.append(input_number)
    if value in input_list:
        return True
    else:
        return False


print(is_member())
