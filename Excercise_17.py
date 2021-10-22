# Exercise 17 - Advanced Palindrome Checker Write a version of a palindrome recognizer that also accepts phrase
# palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets",
# "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it
# as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation,
# capitalization, and spacing are usually ignored.
def palindrome():
    string_input = str(input("enter the string "))
    filterd_string = ''
    for i in string_input:
        if i == ' ':
            pass
        else:
            filterd_string += i.lower()
    print(filterd_string)
    reversed_string = ''
    for i in range(len(filterd_string) - 1, -1, -1):
        reversed_string += filterd_string[i]
    print(reversed_string)
    if reversed_string == filterd_string:
        print("it is a palindrome")
    else:
        print('it is not a palindrome')


palindrome()
