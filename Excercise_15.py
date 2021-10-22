# Exercise 15 - Longest Word
# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
def  find_longest_word():
    word_list = ['hashar', 'tayyab', 'blue', 'green', 'representing']
    maximum_word_len=''
    for i in word_list:
        for j in word_list:
            if len(i)>len(j):
                maximum_word_len = str(i)
    print(f'maximum word is {maximum_word_len}, and lenght is {len(maximum_word_len)} ')
print(find_longest_word())