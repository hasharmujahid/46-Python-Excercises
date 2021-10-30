# Exercise 40 - Anagram An anagram is a type of word play, the result of rearranging the letters of a word or phrase
# to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse,
# A decimal point = I'm a dot in place. Write a Python program that, when started 1) randomly picks a word w from
# given list of words, 2) randomly permutes w (thus creating an anagram of w), 3) presents the anagram to the user,
# and 4) enters an interactive loop in which the user is invited to guess the original word. It may be a good idea to
# work with (say) colour words only. The interaction with the program may look like so:
#
# import anagram
#
# Colour word anagram: onwbr
# Guess the colour word!
# black
# Guess the colour word!
# brown
# Correct!

def anagram():
    import random
    list_of_words = ['Black', 'Brown', 'Blue', 'Green', 'Pink', 'Yellow', 'Red']
    random_word = random.choice(list_of_words)
    anagram = ''
    for i in range(0, len(random_word), 1):
        anagram = ''.join(random.sample(random_word, len(random_word)))

    while True:
        print("The anagram is {} ".format(anagram))
        guessed_word = str(input("enter the guess : "))
        if random_word == guessed_word:
            print("you got it boss")
            break
        else:
            print("Try again")


anagram()
