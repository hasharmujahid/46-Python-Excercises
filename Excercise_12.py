# Exercise 12 - Histograms
# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
def histogram():
    input_list_1 = []
    lenght_of_the_list = int(input('enter the lenght of the list : '))
    for number in range(0, lenght_of_the_list, 1):
        input_number = int(input(f'enter the {number+1} number : '))
        input_list_1.append(input_number)
    print(input_list_1)

    for i in input_list_1:
        print('x'*i)
histogram()
