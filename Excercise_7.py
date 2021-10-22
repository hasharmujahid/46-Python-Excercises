# Exercise 7 - Reverse a String
# Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse_string(string=(str(input('enter the string : ')))):
    reverse = ''
    for i in range(len(string) - 1, -1, -1):
        reverse += string[i]
    return reverse


print(reverse_string())
