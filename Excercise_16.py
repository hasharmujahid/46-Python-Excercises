# Exercise 16 - Filter Long Words
# Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

def filter_long_words():
    maximum_lenght = int(input("enter the maximum length to filter : "))
    word_list = ['hashar', 'tayyab', 'blue', 'green', 'representing']
    filtered_list = []
    for i in word_list:
        if len(i) >= maximum_lenght:
            filtered_list.append(i)
        else:
            pass
    return filtered_list


print(filter_long_words())
