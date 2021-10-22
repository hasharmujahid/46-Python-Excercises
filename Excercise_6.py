# Exercise 6 - Sum and Multiply
# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

def sum_and_multiplies():
    input_list = []
    lenght_of_the_list = int(input('enter the lenght of the list : '))
    for number in range(0, lenght_of_the_list, 1):
        input_number = int(input(f'enter the {number+1} number : '))
        input_list.append(input_number)
    print(input_list)
    sum = 0
    multiply = 1
    for i in input_list:
        sum += i
        multiply *= i
    print(f'the sum of all the numbers in the list is {sum}')
    print(f'the multiply of all the number in the list is {multiply}')

# better way is to use inbuilt functions

sum_and_multiplies()
