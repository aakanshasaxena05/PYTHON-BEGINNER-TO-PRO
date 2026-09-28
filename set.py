# Set in Python

# Creating a set
numbers = {10, 20, 30, 20, 40}

print("Set:", numbers)

# Add an element
numbers.add(50)
print("After add:", numbers)

# Add multiple elements
numbers.update([60, 70])
print("After update:", numbers)

# Remove an element
numbers.remove(20)
print("After remove:", numbers)

# Discard an element
numbers.discard(30)
print("After discard:", numbers)

# Check if element exists
print("Is 40 present?", 40 in numbers)

# Length
print("Length:", len(numbers))

# Two sets
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

# Union
print("Union:", a.union(b))

# Intersection
print("Intersection:", a.intersection(b))

# Difference
print("Difference:", a.difference(b))

# Clear
numbers.clear()
print("After clear:", numbers)