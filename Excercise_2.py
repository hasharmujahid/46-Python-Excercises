# Exercise 2 - Max of Three
# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def maximum_of_three(number_1=int(input("enter the number : ")),number_2=int(input("enter the second number : ")),number_3=int(input("enter the Third number : "))):
    if number_1>number_2 and number_3: print(f"{number_1} is largest")
    if number_2> number_1 and number_2>number_3: print(f"{number_2} is largest")
    if number_3> number_2 and number_3>number_1: print(f"{number_3} is largest")
    if number_1==number_2 == number_3:print("Both are equal ")
# better way is to use the max() function and return the message
maximum_of_three()