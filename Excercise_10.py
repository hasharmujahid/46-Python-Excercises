# Exercise 10 - Overlapping
# Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.

def overlapping():
    input_list_1 = []
    lenght_of_the_list = int(input('enter the lenght of the list : '))
    for number in range(0, lenght_of_the_list, 1):
        input_number = int(input(f'enter the {number+1} number : '))
        input_list_1.append(input_number)
    print(input_list_1)

    input_list_2 = []
    lenght_of_the_list = int(input('enter the lenght of the list : '))
    for number in range(0, lenght_of_the_list, 1):
        input_number = int(input(f'enter the {number+1} number : '))
        input_list_2.append(input_number)
    print(input_list_2)

    for i in input_list_1:
        if i in input_list_2:
            return True
        else:
            return False
print(overlapping())