# Exercise 3 - Length of String
# Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
def length_of_the_string(string=str(input("enter the string "))):
    count =0
    for i in string:
        count+=1
    print(f"the lenght of {string} is {count}")
length_of_the_string()