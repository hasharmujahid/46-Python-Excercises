
# Exercise 8 - Is a Palindrome
# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.
def palindrome():
    string_input = str(input("enter the string "))
    reversed_string = ''
    for i in range(len(string_input) - 1, -1, -1):
        reversed_string += string_input[i]
    print(reversed_string)
    if reversed_string==string_input:
        print("it is a palindrome")
    else:
        print('it is not a palindrome')


palindrome()