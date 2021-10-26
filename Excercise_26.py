# Exercise 26 - Reduce or Max Using the higher order function reduce(), write a function max_in_list() that takes a
# list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just
# as well call the reduce() function directly?
from functools import reduce
def max_in_list(lis1):

    return reduce(lambda x,y:x if x>y else y,lis1)
print(max_in_list([1,22,33,44,324,566453,34565453]))