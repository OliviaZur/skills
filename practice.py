class Array:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.size = 0 
        self.data = [None] * capacity

    def push(self, val):
         self.data[self.size] = val
         self.size = self.size + 1

    def pop(self):
        self.data[self.size - 1] = None
        self.size = self.size - 1

arr = Array(4)
arr.push('Myles')
arr.push('Olive')
arr.push('Liv')
arr.push('Zoey')
arr.pop()
print(arr.data)