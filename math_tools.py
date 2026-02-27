def add(a, b):
    return a + b

def multiply(a, b ):
    return a * b

def is_even(n):
    return n%2==0

def subtract(a, b):
    return a - b

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
def is_palindrome(s):
    # Remove spaces first
    s_no_spaces = s.replace(" ", "")
    return s_no_spaces == s_no_spaces[::-1]

def find_min(numbers):
    min_val = numbers[0]  # Start with the first item, NOT 0!
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def remove_duplicates(items):
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list