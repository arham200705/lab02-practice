from math_tools import add, multiply, is_even, subtract, max_of_three, is_palindrome, find_min, remove_duplicates
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("test_add: ALL PASSED")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    print("test_multiply: ALL PASSED")

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("test_is_even: ALL PASSED")

test_add()
test_multiply()
test_is_even()
print("--- All tests passed! ---")

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 10) == 0
    assert subtract(-5, 5) == -10
    print("test_subtract: ALL PASSED")

test_subtract()

def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(10, 5, 2) == 10
    assert max_of_three(4, 9, 7) == 9
    assert max_of_three(6, 6, 2) == 6  
    assert max_of_three(8, 8, 8) == 8  
    print("test_max_of_three: ALL PASSED")
    
def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True          # Empty string
    assert is_palindrome("z") == True         # Single character
    assert is_palindrome("nurses run") == True # String with spaces
    assert is_palindrome("Racecar") == False  # Case-sensitive (R vs r)
    print("test_is_palindrome: ALL PASSED")

test_is_palindrome()    

def test_find_min():
    assert find_min([5, 2, 9, 1]) == 1
    assert find_min([10, 20, 30]) == 10  
    assert find_min([-5, -10, 0]) == -10
    print("test_find_min: ALL PASSED")

def test_remove_duplicates():
    assert remove_duplicates([]) == []                       # Empty list 
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]         # No duplicates 
    assert remove_duplicates([1, 1, 1, 1]) == [1]            # All duplicates 
    assert remove_duplicates([1, "1", 1, "1"]) == [1, "1"]   # Mixed types 
    assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
    print("test_remove_duplicates: ALL PASSED")

test_find_min()
test_remove_duplicates()