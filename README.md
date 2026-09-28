# 🐍 Python Programming Repository

This repository contains Python programs covering **basic Python concepts, operators, control flow, functions, data structures, exception handling, file handling, and Object-Oriented Programming (OOPs).**

---

## 🔢 1. Fundamentals & Basics

* **`hello.py`** – Basic Python program and "Hello, World!" output.
* **`comment.py`** – Single-line and multi-line comments.
* **`variable.py`** – Variables, naming rules, assignment, and scope.
* **`datatype.py`** – Python data types such as `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, and `dict`.
* **`inputoutput.py`** – Taking input using `input()` and displaying output using `print()`.

---

## ➕ 2. Operators & Expressions

* **`arithmetic.py`** – Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
* **`assignment.py`** – Assignment operators: `=`, `+=`, `-=`, `*=`, `/=`, `%=` and `**=`.
* **`comparison.py`** – Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`.
* **`logical.py`** – Logical operators: `and`, `or`, `not`.
* **`identity.py`** – Identity operators: `is`, `is not`.
* **`membership.py`** – Membership operators: `in`, `not in`.
* **`bodmas.py`** – Operator precedence and BODMAS calculations.

---

## 🔀 3. Control Flow Statements

* **`controlstatements.py`** – Decision-making, looping, and jump statements.

  * `if`
  * `if-else`
  * `if-elif-else`
  * `for`
  * `while`
  * `break`
  * `continue`
  * `pass`

---

## 🔧 4. Functions

* **`function.py`** – Defining and calling functions.
* Function arguments and parameters.
* Return values.
* Local and global variables.
* Default and keyword arguments.
* `*args` and `**kwargs`.
* Lambda functions.
* Decorators.
* Generators and `yield`.

---

## 📊 5. Data Structures

### String

* **`string.py`** – String creation, indexing, slicing, and string methods.

### List

* **`list.py`** – List creation, indexing, slicing, iteration, and list methods.

### Tuple

* **`tuple.py`** – Immutable ordered collections and tuple operations.

### Set

* **`set.py`** – Unique values and set operations such as union, intersection, difference, and symmetric difference.

### Dictionary

* **`dict.py`** – Key-value pairs, dictionary methods, and dictionary iteration.

### Array

* **`array.py`** – Working with arrays and sequence-based data.

---

## ⚠️ 6. Exception Handling

* **`exception.py`** – Handling errors and exceptions in Python.

Topics covered:

* `try`
* `except`
* `else`
* `finally`
* `raise`
* `as`
* Built-in exceptions
* User-defined exceptions
* `ValueError`
* `TypeError`
* `ZeroDivisionError`
* `IndexError`
* `KeyError`
* `FileNotFoundError`
* `SyntaxError`

### Example concepts

```python
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program completed")
```

---

## 📁 7. File Handling

* **`filehandling.py`** – Working with files in Python.

Topics covered:

* Creating files
* Opening files
* Reading files
* Writing files
* Appending data
* Closing files
* File modes:

  * `r` – Read
  * `w` – Write
  * `a` – Append
  * `x` – Create
  * `r+` – Read and write
  * `w+` – Write and read
  * `a+` – Append and read
* `read()`
* `readline()`
* `readlines()`
* `write()`
* `writelines()`
* `with open()`

### Example

```python
with open("student.txt", "w") as file:
    file.write("Aakansha")
```

---

# 🏗️ 8. Object-Oriented Programming (OOPs)

OOPs is a programming approach based on **classes and objects**.

### Classes & Objects

* **`classobject.py`** – Creating classes and objects.
* **`constructor.py`** – Using the `__init__()` constructor.
* **`typesofconstructor.py`** – Default, parameterized, and custom constructor concepts.
* **`self.py`** – Understanding the `self` parameter.

### Four Pillars of OOP

#### 🔒 Encapsulation

* **`encapsulation.py`** – Data hiding and controlled access.
* Public attributes
* Protected attributes `_variable`
* Private attributes `__variable`
* Getters and setters

#### 🧬 Inheritance

* **`inheritance.py`** – Reusing properties and methods from another class.
* Single inheritance
* Multiple inheritance
* Multilevel inheritance
* Hierarchical inheritance
* Hybrid inheritance

#### 🔄 Polymorphism

* **`polymorphism.py`** – One interface with different behaviors.
* Method overriding
* Operator overloading
* Duck typing
* Method overloading concepts

#### 🎭 Abstraction

* **`abstraction.py`** – Hiding implementation details.
* Abstract classes
* Abstract methods
* `ABC`
* `@abstractmethod`

---

## 📚 9. OOP Concepts

The OOP section covers:

```text
                 OOP
                  |
        ┌─────────┴─────────┐
        |                   |
      Class               Object
        |
   ┌────┴─────────────────────────┐
   |            |          |       |
Encapsulation Inheritance Polymorphism Abstraction
```

Important concepts include:

* Class
* Object
* Constructor
* `__init__()`
* `self`
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
* Method overriding
* Method overloading
* Operator overloading

---

## 📂 10. Complete Python Learning Structure

```text
Python
│
├── Fundamentals
│   ├── hello.py
│   ├── comment.py
│   ├── variable.py
│   ├── datatype.py
│   └── inputoutput.py
│
├── Operators
│   ├── arithmetic.py
│   ├── assignment.py
│   ├── comparison.py
│   ├── logical.py
│   ├── identity.py
│   ├── membership.py
│   └── bodmas.py
│
├── Control Flow
│   └── controlstatements.py
│
├── Functions
│   └── function.py
│
├── Data Structures
│   ├── string.py
│   ├── list.py
│   ├── tuple.py
│   ├── set.py
│   ├── dict.py
│   └── array.py
│
├── Exception Handling
│   └── exception.py
│
├── File Handling
│   └── filehandling.py
│
└── OOPs
    ├── classobject.py
    ├── constructor.py
    ├── typesofconstructor.py
    ├── self.py
    ├── encapsulation.py
    ├── inheritance.py
    ├── polymorphism.py
    └── abstraction.py
```

---

## 🎯 Topics Covered

This repository covers the complete journey from **Python basics to OOPs**:

**Basics → Operators → Control Flow → Functions → Data Structures → Exception Handling → File Handling → OOPs**
