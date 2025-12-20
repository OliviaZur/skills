class Array:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.data = [None] * capacity

    def push(self, value):
        self.data[self.size] = value
        self.size = self.size + 1

    def __str__(self):
        # Return a string representation of the array (only filled elements)
        return str(self.data)


newArray = Array(10)
newArray.push("Olive")
newArray.push("Zoey")
newArray.push("Teddy")
newArray.push("Remi")

print(newArray)
print(newArray.size)