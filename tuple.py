# Tuple in Python

# 1. Creating a tuple
numbers = (10, 20, 30, 20, 40)

print("Tuple:", numbers)

# 2. Accessing elements using index
print("First element:", numbers[0])
print("Third element:", numbers[2])

# 3. Negative indexing
print("Last element:", numbers[-1])

# 4. Slicing
print("Sliced tuple:", numbers[1:4])

# 5. count()
print("Count of 20:", numbers.count(20))

# 6. index()
print("Index of 30:", numbers.index(30))

# 7. len()
print("Length:", len(numbers))

# 8. Concatenation
a = (10, 20)
b = (30, 40)

c = a + b

print("Concatenated tuple:", c)

# 9. Repetition
print("Repeated tuple:", a * 2)

# 10. Checking element
print("Is 30 present?", 30 in numbers)

# 11. Tuple unpacking
student = ("Aakansha", 22, 85)

name, age, marks = student

print("Name:", name)
print("Age:", age)
print("Marks:", marks)