# Exercise 14 - Words into Integers
# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
def map_words_lenght():
    word_list = ['hashar', 'tayyab', 'blue', 'green', 'representing']
    list_length = []
    for i in word_list:
        list_length.append(len(i))
    return list_length


print(map_words_lenght())
