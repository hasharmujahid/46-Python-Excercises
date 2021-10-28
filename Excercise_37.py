# Exercise 37 - Text Novice Write a program that given a text file will create a new text file in which all the lines
# from the original file are numbered from 1 to n (where n is the number of lines in the file).

def text_novice():
    file_orignal = open(input("enter the file name : "))
    i = 1
    for line in file_orignal:
        file_text_novice = open("text_novice.txt", 'a')
        file_text_novice.write(str(i) + " : " + str(line))
        file_text_novice.write('\n')
        i += 1
        file_text_novice.close()
    file_orignal.close()
    return


text_novice()
