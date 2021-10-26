# Exercise 23 - Spell Check Define a simple "spelling correction" function correct() that takes a string and sees to
# it that 1) two or more occurrences of the space character is compressed into one, and 2) inserts an extra space
# after a period if the period is directly followed by a letter. E.g. correct("This is very funny and cool.Indeed!")
# should return "This is very funny and cool. Indeed!" Tip: Use regular expressions!
def correct(input1=str(input("enter the string : "))):
    res=''
    for i in range(0, len(input1), 1):

        if input1[i]== '.':
                if input1[i + 1]!= ' ':
                    res+=input1.replace(input1[i],'. ')
    return res
print(correct())