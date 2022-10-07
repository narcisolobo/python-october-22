""" 
Countdown - Create a function that accepts a number
as an input. Return a new list that counts down by one,
from the number (as the 0th element) down to 0 (as the last element).
Example: countdown(5) should return [5,4,3,2,1,0]
"""

def countdown(num):
    new_list = []
    for i in range(num, -1, -1):
        new_list.append(i)
    return new_list

print(countdown(5))

""" 
Print and Return - Create a function that will receive
a list with two numbers. Print the first value and return the second.
Example: print_and_return([1,2]) should print 1 and return 2
"""

def print_and_return(lst):
    print(lst[0])
    return lst[1]

result = print_and_return([1, 2])
print('result is', result)

""" 
First Plus Length - Create a function that accepts a list
and returns the sum of the first value in the list plus
the list's length.
Example: first_plus_length([1,2,3,4,5]) should return 6
(first value: 1 + length: 5)
"""

def first_plus_length(lst):
    return lst[0] + len(lst)

result = first_plus_length([5,2,3,4,5])
print(result)