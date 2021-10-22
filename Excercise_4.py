# Exercise 4 - Vowel Checker
# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
def vowel_checker(character=str(input('enter the character')).lower()):
    list_vowel = ['a', 'e', 'i', 'o', 'u']
    for i in list_vowel:
        if i == character:
            return True
        else:
            return False


print(vowel_checker())
