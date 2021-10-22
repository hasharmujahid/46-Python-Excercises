# Exercise 1 - Max of Two
# Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
def maximum(numer_1=int(input("enter the number : ")),number_2=int(input("enter the second number : "))):
    if numer_1>number_2: print(f"{numer_1} is largest")
    elif numer_1==number_2:print("Both are equal ")
    else:print(f"{number_2} is largest")
    # better way is to use the max() function and return the message

maximum()