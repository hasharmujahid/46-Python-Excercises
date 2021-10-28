# Exercise 38 - Average Words in File Write a program that will calculate the average word length of a text stored in
# a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).

def average_word_length():
    words = []
    total_character_count = 0
    total_words_count = 0
    file = open(input("enter the file nmae : "))
    for line in file:
        words += line.split()
        for i in words:
            total_character_count += len(i)
            total_words_count += 1
    average_word_lengths = total_character_count // total_words_count
    print(f'Total words count was {total_words_count} and total character count in file was {total_character_count} so average length of the word is {average_word_lengths}')


average_word_length()
