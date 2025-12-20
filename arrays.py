import numpy as np

numbers = [8, 2, 16, 3, 9, 11, 18, 1, 6, 22]
max_value = max(numbers)
print("The biggest number is:", max_value)


numbers = [3, 2, 8, 5, 10, 6, 22, 45, -1, 4]
smallest_number = min(numbers)
print("The smallest number is:", smallest_number) 


n = np.array([4, 6, 2, 5, 3])
print(n.mean())  


a = np.random.normal(0, 1, 5)
print("Data:", a)
print("Mean:", np.mean(a))