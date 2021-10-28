# Exercise 34- Terminal Character Frequency Write a procedure char_freq_table() that, when run in a terminal,
# accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a
# sorted and nicely formatted character frequency table to the screen.
from Excercise_33 import filter_string


def char_freq_table():
    file = open('Excercise_33.txt')
    freq = {}
    for line in file:
        filterd_line = filter_string(line)
        charactercount = 0
        for character in filterd_line:
            if character not in freq:
                charactercount += 1
                freq.update({character: charactercount})
                charactercount = 0
            else:
                for keys in freq:
                    if keys == character:
                        charactercount = freq[keys]
                        charactercount += 1
                        freq.update({keys: charactercount})
                        charactercount = 0
                        break
    return freq


print(char_freq_table())
