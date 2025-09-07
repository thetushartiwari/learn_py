"""
===================================================
   PRACTICE.PY – Python Revision Workbook
===================================================

Day 1 – Introduction & Data Types
Day 2 – Control Flow & Loops
Day 3 – Functions, Modules & Scope
Day 4 – Collections (Lists, Tuples, Dicts, Sets)
Day 5 – Strings & Regex
Day 6 – File Handling & Exceptions
Day 7+ – Challenges Recap
OOP Basics – Classes & Objects
OOP Advanced – Inheritance, Polymorphism,
               Encapsulation, Abstraction
===================================================
"""

# ==================================================
# Day 1 – Introduction & Data Types
# ==================================================
integer_var = 10              # int
float_var = 3.14              # float
string_var = "AI"             # string
list_var = [1, 2, 3]          # list
tuple_var = (4, 5, 6)         # tuple
dict_var = {"name": "Alice", "role": "Engineer"}  # dictionary
bool_var = True               # boolean

print("Integer:", integer_var)        # Output: Integer: 10
print("Float:", float_var)            # Output: Float: 3.14
print("String:", string_var + " Bootcamp")  # Output: String: AI Bootcamp
list_var.append(4)
print("List:", list_var)              # Output: List: [1, 2, 3, 4]
print("Tuple:", tuple_var)            # Output: Tuple: (4, 5, 6)
print("Dictionary Value:", dict_var["role"]) # Output: Dictionary Value: Engineer
print("Boolean:", bool_var)           # Output: Boolean: True


# ==================================================
# Day 2 – Control Flow & Loops
# ==================================================

# Example: Countdown using while loop
count = 5
while count > 0:
    print(count)   # Output: 5, 4, 3, 2, 1 (each on new line)
    count -= 1
print("Outside While Loop")  # Output: Outside While Loop

# Example: Loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)   # Output: apple, banana, cherry (each on new line)

# Challenge: Menu-driven calculator
def run_calculator():
    """Menu-driven calculator with input"""
    def add(a, b): return a + b
    def subtract(a, b): return a - b
    def multiply(a, b): return a * b
    def divide(a, b): return a / b if b != 0 else "Division by zero!"

    while True:
        print("\nMenu:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "5":
            print("Exiting Program.")  # Output when user chooses exit
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice.")


# ==================================================
# Day 3 – Functions, Modules & Scope
# ==================================================
import math as m

def factorial(n):
    """Recursive factorial"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def print_factorial(n):
    result = factorial(n)
    print(f"The factorial of {n} is {result}")

print_factorial(5)  
# Output: The factorial of 5 is 120

print(m.sqrt(16))  
# Output: 4.0


# ==================================================
# Day 4 – Collections
# ==================================================
def word_frequency(sentence: str):
    """Counts word frequency in a sentence"""
    words = sentence.split()
    word_count = {}
    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(word_frequency("Hello hello world world"))  
# Output: {'hello': 2, 'world': 2}


# ==================================================
# Day 5 – Strings & Regex
# ==================================================
import re

def clean_text(text):
    """Clean and normalize string"""
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = " ".join(text.split())        # normalize spaces
    return text.lower()

print(clean_text("   Hello, World.!!!   "))  
# Output: hello world

def is_palindrome(text):
    """Check if text is palindrome"""
    text = "".join(ch.lower() for ch in text if ch.isalnum())
    return text == text[::-1]

print(is_palindrome("Madam"))  
# Output: True


# ==================================================
# Day 6 – File Handling & Exceptions
# ==================================================
def count_words_and_lines(filename):
    """Count words and lines in file"""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            return len(lines), sum(len(line.split()) for line in lines)
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return 0, 0

# Example file run
lines, words = count_words_and_lines("sample.txt")
print(f"Lines={lines}, Words={words}")  
# Output depends on file content

def write_notes(filename, notes_list):
    """Write notes list to file"""
    with open(filename, "w") as file:
        for note in notes_list:
            file.write(note + "\n")
    print(f"Notes successfully written to {filename}")  
    # Output: Notes successfully written to sample.txt

def read_notes(filename):
    """Read notes from file"""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"

print(read_notes("sample.txt"))  
# Output: contents of file or "File not found!"


# ==================================================
# OOP Basics – Classes & Objects
# ==================================================
class Student:
    """Basic Student class with encapsulation"""
    def __init__(self, name, major, age):
        self.name = name
        self.major = major
        self._age = age  # protected attribute

    def introduce(self):
        print(f"Hi, my name is {self.name}, I study {self.major}, and I am {self._age} years old.")

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print("Age cannot be negative or zero.")

# Example run
s = Student("Tushar", "CSDA", 22)
s.introduce()  
# Output: Hi, my name is Tushar, I study CSDA, and I am 22 years old.
s.set_age(23)
s.introduce()  
# Output: Hi, my name is Tushar, I study CSDA, and I am 23 years old.


# ==================================================
# OOP Advanced – Inheritance, Polymorphism,
# Encapsulation, Abstraction
# ==================================================

# Inheritance
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, my name is {self.name}.")

class StudentChild(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major
    def introduce(self):
        print(f"{self.name}, majoring in {self.major}.")

child = StudentChild("Alice", "Math")
child.greet()      
# Output: Hello, my name is Alice.
child.introduce()  
# Output: Alice, majoring in Math.

# Polymorphism
class Animal:
    def __init__(self, name): self.name = name
    def make_sound(self): print(f"{self.name} makes a sound.")

class Dog(Animal):
    def make_sound(self): print(f"{self.name} barks: Woof!")

class Cat(Animal):
    def make_sound(self): print(f"{self.name} meows: Meow!")

dog, cat = Dog("Buddy"), Cat("Whiskers")
dog.make_sound()  # Output: Buddy barks: Woof!
cat.make_sound()  # Output: Whiskers meows: Meow!

# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color): self.color = color
    @abstractmethod
    def area(self): pass
    def describe(self): print(f"This is a {self.color} shape.")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self): return m.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width, self.height = width, height
    def area(self): return self.width * self.height

c, r = Circle("red", 5), Rectangle("blue", 4, 6)
c.describe()       # Output: This is a red shape.
print(c.area())    # Output: 78.53981633974483
r.describe()       # Output: This is a blue shape.
print(r.area())    # Output: 24
