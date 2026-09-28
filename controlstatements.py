# CONTROL FLOW STATEMENTS IN PYTHON

# --------------------------------
# 1. IF STATEMENT
# --------------------------------

age = 20

# Check if age is 18 or above
if age >= 18:
    print("You are an adult")


# --------------------------------
# 2. IF-ELSE STATEMENT
# --------------------------------

marks = 35

# Check whether student passed or failed
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# --------------------------------
# 3. IF-ELIF-ELSE STATEMENT
# --------------------------------

marks = 75

# Check grade according to marks
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


# --------------------------------
# 4. FOR LOOP
# --------------------------------

# Print numbers from 1 to 5
for i in range(1, 6):
    print("For loop:", i)


# --------------------------------
# 5. WHILE LOOP
# --------------------------------

i = 1

# Repeat while i is less than or equal to 5
while i <= 5:
    print("While loop:", i)
    i = i + 1


# --------------------------------
# 6. BREAK STATEMENT
# --------------------------------

for i in range(1, 6):

    # Stop the loop when i becomes 3
    if i == 3:
        break

    print("Break:", i)


# --------------------------------
# 7. CONTINUE STATEMENT
# --------------------------------

for i in range(1, 6):

    # Skip number 3
    if i == 3:
        continue

    print("Continue:", i)


# --------------------------------
# 8. PASS STATEMENT
# --------------------------------

for i in range(1, 4):

    if i == 2:
        pass       # Do nothing

    print("Pass:", i)