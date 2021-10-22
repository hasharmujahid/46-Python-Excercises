# Exercise 13 - Max in List
# The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.

def Max_in_list():
    input_list = []
    lenght_of_the_list = int(input('enter the lenght of the list : '))
    for number in range(0, lenght_of_the_list, 1):
        input_number = int(input(f'enter the {number+1} number : '))
        input_list.append(input_number)
    print(input_list)
    return max(input_list)
print(Max_in_list())
