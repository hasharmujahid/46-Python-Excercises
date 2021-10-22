# Exercise 18 - Pangram A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence
# to see if it is a pangram or not.
import string
def panagram_checker():
    string_input=str(input("enter the string : ")).lower()
    alphabets=list(string.ascii_lowercase)
    for char in string_input:
        if char in alphabets:
            return True
        else:
            return False

print(panagram_checker())
