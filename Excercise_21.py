# Exercise 21 - Char Frequency
# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
def char_freq(string=str(input("enter the string : "))):
    frequency = {}
    count = 0
    for i in string:
        for j in string:
            if i == j:
                count += 1
                frequency.update({i: count})
            else:
                pass
        count = 0

    return frequency


print(char_freq())
