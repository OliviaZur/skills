# GOAL: Make an "Array" class with these methods below:
# ✓ - Done
    # [-] Push - Adds a new element to array
    # [-] Pop - Removes the last element in array
    # [-] Get - Returns the item at the spec. at index
    # [-] Set - Overwrites/Pushes the value spec. at index
    # [-] Resize - Remove/Allocate memory based on size/capacity

# SYNTAX:
    # "()" = a place where parameters are "passed in"
        # Q: How to "pass in" a parameter
        # A: set a parameter = variable
        # Example: def my_function(variable1, variable2)
    # ":" = lets the program know that we are writing logic inside of the defined snippet
    # "def" = lets the program know that we are defining a function (python's keyword)
    # "<array_name>[x]" where "x" refers to the index (the position in the array)

# TERMINOLOGY:
    # Zero-Value - A representation of a value = no value (aka "None" in Python)
    # Class - A data type that has a customized set of instructions (methods)
    # Method - A reusable function that a custom data type can use
    # Index - The i-th position in the array = (n-1); where "n" refers to the place you want to put the value in the array

# VARIABLES:
    # capacity - refers to how many Bytes we are allocating in our array

class Array:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity
        self.length = 0

    def push(self, value):
        self.data[self.length] = value
        self.length = self.length + 1

    def pop(self):
        self.data[self.length - 1] = None
        self.length = self.length - 1

# TODO: Guard ourselves from overflowing or popping a value that isn't there
# TODO: Grow the array if the size is almost at the capacity
# TODO: Shrink the array if the size is a fraction of the capacity

arr = Array(3)
arr.push("Olive")
arr.push("Zoey")
arr.push("Teddy")
arr.pop()
print(arr.data)
