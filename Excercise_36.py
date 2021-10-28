# Exercise 36 - Hapax Legomenon A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in
# either the written record of a language, the works of an author, or in a single text. Define a function that given
# the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.

def hapax():
    words=[]
    file=open(input("enter the file name : "))
    for  line in file:
        words +=line.lower().split()

    hapaxes=list(filter(lambda x: x if words.count(x)==1 else None,words))
    return hapaxes
print(hapax())