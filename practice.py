# Day 1:introduction to python and data types

# Define variables of different data types
integer_var = 10
float_var = 3.14
string_var = "AI"
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
dict_var = {"name": "Alice", "role": "Engineer"}
bool_var = True

# Print and manipulate variables
print("Integer: ", integer_var)
print("Float: ", float_var)
print("String: ", string_var + " Bootcamp")
list_var.append(4)
print("List: ", list_var)
print("Tupple: ", tuple_var)
print("Dictionary Value:", dict_var["role"])
print("Boolean: ", bool_var)


# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)


# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# print("Outside For Loop")

# Count down from 5
# count = 5
# while count > 0:
#     print(count)
#     count -= 1

# print("Outside While Loop")

#Syntax while
# while True:
#     # Code block


# Loop through a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
    
# Loop with range
# for i in range(10): #[0,1,2,3,4]
#     print(i)

#Syntax for for-loop

# for item in sequence:
#     #Code block


# Example 1: Checking a condition
# num = -50
# if num > 0:
#     print("Positive Number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative Number")
    
# Example 2: Nested conditions
# age = 3
# if age > 18:
#     if age < 30:
#         print("Young Adult")
#     else:
#         print("Adult")

# Day 2:control flow and loops

# creare a menu based cal 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"
    
while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "5":
        print("Exiting Program.")
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        print("Result: ", add(num1, num2))
    elif choice == "2":
        print("Result: ", subtract(num1, num2))
    elif choice == "3":
        print("Result: ", multiply(num1, num2))
    elif choice == "4":
        print("Result: ", divide(num1, num2))
    else:
        print("Invclid choice. Please try again.")

# day 3:functions, modules and scope

import math as m
print(m.sqrt(16))



# # Global Scope

# greeting = "Hi"

# def say_hello():
#     print(greeting + " from inside the function")
    
# say_hello()
# print(greeting + " from outside the function")



# # Local Scope
# def greet():
#     message = "Hello World"
#     print(message)
    
# greet()
# #print(message)


# FUnction with parameters and return value
# def add_numbers():
#     c = a + b
#     return c

# result = add_numbers()
# print("Sum: ", c)

# def function_name(parameters):
#     #Code block
#     return result


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# print(set1 - set2)




# student = {"name": "Alice", "age": 25, "grade": "A"}


# for key, value in student.items():
#     print(key, value)


# student["subject"] = "Math"
# student["age"] = 32

# print(student)

# del student["grade"]

# print(student)

# student.pop("subject")

# print(student)











# colors = ("red", "green", "blue")
# single_item = ("glass",)

# print(colors[0])
# print(colors[-1])









# numbers = [1, 2, 3, 4]

# fruits = ["apple", "banana", "cherry"]

# mixed = [1, "apple", True]

# # print(numbers[2])
# # print(fruits[-1])
# # print(mixed[1])

# fruits.append("orange")
# fruits.insert(1, "grape")

# print(fruits)

# sliced_fruits = fruits[2:4]
# print(sliced_fruits)

# fruits.remove("banana")

# print(fruits)

# del fruits[0]

# print(fruits)

# fruits.pop()
# fruits.pop()

# print(fruits)

# ex1-
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def print_factorial(n):
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
    
print_factorial(2)

# ex2-
import math_operations as mo

num1 = 10
num2 = 5

print("Addition: ", mo.add(num1, num2))
print("Subtraction: ", mo.subtract(num1, num2))
print("Multiplication: ", mo.multiply(num1, num2))
print("Division: ", mo.divide(num1, num2))



# day-4 :functions, modules and scope

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# print(set1 - set2)




# student = {"name": "Alice", "age": 25, "grade": "A"}


# for key, value in student.items():
#     print(key, value)


# student["subject"] = "Math"
# student["age"] = 32

# print(student)

# del student["grade"]

# print(student)

# student.pop("subject")

# print(student)











# colors = ("red", "green", "blue")
# single_item = ("glass",)

# print(colors[0])
# print(colors[-1])









# numbers = [1, 2, 3, 4]

# fruits = ["apple", "banana", "cherry"]

# mixed = [1, "apple", True]

# # print(numbers[2])
# # print(fruits[-1])
# # print(mixed[1])

# fruits.append("orange")
# fruits.insert(1, "grape")

# print(fruits)

# sliced_fruits = fruits[2:4]
# print(sliced_fruits)

# fruits.remove("banana")

# print(fruits)

# del fruits[0]

# print(fruits)

# fruits.pop()
# fruits.pop()

# print(fruits)

# ex- 3- Word Frequency Counter
sentence = input("Enter a Sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize Dictionary
word_count = {}

# Count word frequence
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print(word_count)


# day-5: working with strings, regex
import re


# split()

sentence = "Python is fun"
words = sentence.split()
#print(words)

# join()
new_sentence = "|".join(words)
#print(new_sentence)

# ex-000 - String Replacement and Trimming
text = "I love Java"
updated_text = text.replace("Java", "Python")
#print(updated_text)

messy = "     Hello, World     "
print(messy)
cleaned_text = messy.strip()
print(cleaned_text)

# ex-001 - Extracting Digits and Replacing Them

text = "Contact me at 123-456-7890"
digits = re.findall(r"\d+", text)
print(digits)

updated_text = re.sub(r"\d", "X", text)
print(updated_text)

# ex-001 - Clean and Normalize Text
def clean_text(text):
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = " ".join(text.split())
    # Convert to lowercase
    return text.lower()

input_text = "   Hello, World.!!! Welcome to Python, Programming....    "
cleaned_text = clean_text(input_text)
print("Cleaned Text: ", cleaned_text)


# ex-002 - Palindrome Checker
def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome.')
else:
    print(f'"{input_text}" is not a palindrome.')






# Challenge 1: Write a Python script that does the following:
# Creates a variable my_name and assigns your name to it.
# Creates a variable my_age and assigns your age to it.
# Creates a list called hobbies with at least three of your hobbies.
# Creates a dictionary called personal_info that stores your name, age, and hobbies from the variables you just created.
# Prints out the contents of the personal_info dictionary.

my_name = "Tushar"
my_age = 22
hobbies = ["coding", "learning", "writing"]

personal_info = {
    "name": my_name,  # The key is a string "name", and the value is the variable `my_name`
    "age": my_age,    # The key is a string "age", and the value is the variable `my_age`
    "hobbies": hobbies # The key is a string "hobbies", and the value is the variable `hobbies`
}

print(personal_info)

# Challenge 2: Write a script that checks your age and prints a message based on it.
# Use the my_age variable you already created.
# Write an if statement that checks if your age is greater than 18.
# If it is, print a message like "You are an adult."
# Add an else statement to print "You are a minor."
# (Bonus) Try to add an elif (else if) statement to check for a different age range, like "You are a young adult."

if my_age > 18:
    print("You are an adult.")
elif my_age > 12 and my_age <= 18:
    print("You are a young adult.")
else:
    print("You are a minor.")

# --- Notes on For Loops ---
# A 'for' loop iterates over each item in a sequence.
# It makes repetitive tasks simple, like printing every item in a list.
# Syntax: `for <item> in <sequence>:`
# The '<item>' is a temporary variable that holds the current item during each loop.

# --- Challenge 3: Using a For Loop ---

# Your task:
# 1. Write a 'for' loop that goes through each item in the 'hobbies' list.
# 2. Inside the loop, print out a message for each hobby.
# For example, the first line would print: "My hobby is coding"

# Write your code below this line:

for hobby in hobbies:
    print(f"My hobby is {hobby}")
# Short Notes:
# - f-string (`f"..."`): Used for string interpolation. Place variables inside {} to include their values in the string.
#   Example: print(f"My name is {my_name}")  # Output: My name is Tushar
#
# - Printing a single item from a list: Use the index to access a specific item.
#   Example: print(hobbies[0])  # Prints the first hobby

# --- Notes on Functions ---
# `def` defines the function.
# `(item_list)` is an argument, a variable that holds the data we pass into the function.
# The code inside the function is indented.

# --- Challenge 4: Write a Function with a Loop ---

# Your task:
# 1. Define a function called `print_hobbies` that takes one argument, which we'll call `item_list`.
# 2. Inside the function, write the 'for' loop we just did to iterate through `item_list`.
# 3. Call your function at the end, passing it the `hobbies` list we created earlier.
# The output should be the same as before, but this time it's being generated by a function call.

# Write your code below this line:

def print_hobbies(hobby_list):
    for hobby in hobby_list:
        print(f"My hobby is {hobby}")
print_hobbies(hobbies)

# --- Notes on the New Challenge ---
# The goal is to build a function that takes a list of numbers,
# squares each one, and returns a new list of the results.
# Remember to use the `**` operator for exponents (e.g., `2 ** 2` is 4).
# Your `return` keyword should be at the end of the function, after the loop.

# --- Challenge 5: Square a List of Numbers ---

# Your task:
# 1. Define a function called `square_numbers` that takes one argument: a list of numbers.
# 2. Inside the function, create an empty list to hold the squared numbers.
# 3. Loop through the input list.
# 4. For each number, calculate its square and add it to your new list.
# 5. After the loop is finished, return the new list of squared numbers.
# 6. Finally, create a sample list of numbers (e.g., `[1, 2, 3, 4]`), call your function with it, and then print the result.

# 1. DEFINE THE FUNCTION
def square_numbers(number_list):
    # 2. CREATE AN EMPTY BUCKET
    squared_numbers = []

    # 3. LOOP THROUGH THE INPUT LIST
    for number in number_list:
        
        # 4. SQUARE AND STORE
        squared_numbers.append(number ** 2)

    # 5. RETURN THE RESULT
    return squared_numbers

numbers = [1, 2, 3, 4]  # Sample list of numbers
result = square_numbers(numbers)  # Call the function
print(result)  # Print the result of the squared numbers

# --- Notes on List Comprehensions ---
# The format is: [what_to_do for_each_item in the_list_you_have]
# This single line of code replaces the empty list, the for loop, and the .append() method.
# It's a very powerful tool used extensively in data science and machine learning.

# --- Challenge 6: Rewrite `square_numbers` with a List Comprehension ---

# Your task:
# 1. Define a function called `square_numbers_comprehension` that takes a list.
# 2. Inside the function, use a list comprehension to square each number.
# 3. Return the new list.
# 4. Create a list of numbers and call your new function with it, then print the result.

# Write your code below this line:

def square_numbers_comprehension(number_list):
    return [number ** 2 for number in number_list]  
print(square_numbers_comprehension(numbers))  # Call the function and print the result

# --- Notes on Dictionaries ---
# Dictionaries use curly braces `{}`.
# Each item is a `key: value` pair.
# Keys must be unique and immutable (like strings or numbers).

# --- Challenge 7: Create a Dictionary from Two Lists ---

# Here are two lists. One contains names (keys) and the other contains ages (values).
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Your task:
# 1. Create an empty dictionary called `people_age`.
# 2. Use a `for` loop to iterate through the `names` list.
# 3. Inside the loop, add a key-value pair to your dictionary.
#    The `name` from the `names` list should be the key.
#    The corresponding `age` from the `ages` list should be the value.
#    Hint: You'll need to use the index of the lists to get the right age for each name.
# 4. Print the final `people_age` dictionary.

# Write your code below this line:

people_age = {}  # Step 1: Create an empty dictionary
for i in range(len(names)):  # Step 2: Loop through the names list
    people_age[names[i]] = ages[i]  # Step 3: Add key-value pairs to the dictionary
print(people_age)  # Step 4: Print the final dictionary

# --- Challenge 8: Dictionary Comprehension Solution ---

# This is the dictionary comprehension:
# It iterates through pairs of (name, age) from the zipped lists.
# For each pair, it creates a dictionary entry where 'name' is the key
# and 'age' is the value.
people_age_comprehension = {name: age for name, age in zip(names, ages)}

print(people_age_comprehension)

# --- Additional Notes ---
# - The `zip()` function combines two lists into pairs. 
#   For example, `zip(names, ages)` creates pairs like `("Alice", 25)`.
# - The dictionary comprehension is a concise way to create dictionaries from lists.
# - It can be used to transform data efficiently, especially in data science tasks.     


# --- Notes on Error Handling (`try-except`) ---
# `try`: This block contains the code that you want to monitor for errors.
# `except ZeroDivisionError`: This block runs ONLY if a `ZeroDivisionError` occurs in the `try` block.
#                          You can specify different error types to catch specific issues.
# A function that performs division is a good example where you might encounter this error.

# --- Challenge 9: Handle a DivisionByZeroError ---

# Your task:
# 1. Define a function called `divide_numbers` that takes two arguments: `numerator` and `denominator`.
# 2. Inside the function, use a `try` block.
# 3. Inside the `try` block, attempt to divide `numerator` by `denominator`.
#    If successful, print the result: `f"The result is: {result}"`.
# 4. Add an `except ZeroDivisionError` block. If this specific error occurs,
#    print a friendly message like: `"Error: Cannot divide by zero!"`.
# 5. Test your function with a division that works (e.g., `divide_numbers(10, 2)`).
# 6. Test your function with a division that *causes* an error (e.g., `divide_numbers(10, 0)`).

# Write your code below this line:
def divide_numbers(numerator, denominator):
    try:
        result =  numerator / denominator
        print(f"The result is: {result}") 
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test the function with valid and invalid input
divide_numbers(10, 2)
divide_numbers(10, 0)

# --- Notes on File I/O (Input/Output) ---
# Use `with open(...) as file:` for safe and automatic file closing.
# `'w'` mode for writing: Creates/overwrites the file.
# `'r'` mode for reading: Reads from an existing file.
# Remember to add `\n` (newline character) when writing to ensure each piece of text
# appears on its own line in the file.
# `file.write(string)` writes text.
# `file.read()` reads the entire file content as one string.

# --- Challenge 10: Write and Read a Simple Text File ---

# Your task:
# 1. Decide on a simple filename (e.g., "my_thoughts.txt").
#
# 2. **Define a function `write_notes(filename, notes_list)`:**
#    a. Inside this function, open the specified `filename` in **write mode ('w')**.
#    b. Loop through each string (note) in the `notes_list`.
#    c. For each `note`, use `file.write()` to write the `note` to the file,
#       and **immediately append a newline character (`\n`)** so that each note
#       appears on a separate line in the text file.
#
# 3. **Define a function `read_notes(filename)`:**
#    a. Inside this function, open the specified `filename` in **read mode ('r')**.
#    b. Read the **entire content** of the file using `file.read()` into a variable.
#    c. Print the content you just read to the console.
#
# 4. **Create a sample list of notes (strings):**
#    Example: `my_diary_entries = ["Had a great day today.", "Learned about file I/O!", "Ready for more Python."]`.
#
# 5. **Call `write_notes`:** Pass your chosen `filename` and your `sample list of notes` to this function.
#    This will save your notes to the file.
#
# 6. **Call `read_notes`:** After writing, call this function with the same `filename`.
#    This will read the content back and print it, allowing you to verify that it was saved correctly.

# Write your code below this line:
# --- Solution for Challenge 10: Write and Read a Simple Text File ---

# 1. Choose a filename
FILE_NAME = "my_important_notes.txt"

# 2. Define the function to write notes
def write_notes(filename, notes_list):
    # 'w' mode will create the file if it doesn't exist, or overwrite it if it does.
    with open(filename, 'w') as file:
        for note in notes_list:
            # Write each note followed by a newline character to put them on separate lines.
            file.write(note + '\n')
    print(f"Notes successfully written to {filename}")

# 3. Define the function to read notes
def read_notes(filename):
    try:
        # 'r' mode for reading.
        with open(filename, 'r') as file:
            # Read the entire content of the file.
            content = file.read()
            print(f"\n--- Content of {filename} ---")
            print(content)
            print("--------------------------")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


# 4. Create a sample list of notes
my_diary_entries = [
    "Had a fantastic day learning Python!",
    "File I/O is super useful for data handling.",
    "Remember to always use 'with open()' for safety.",
    "Looking forward to mastering OOP next."
]

# 5. Call write_notes to save the notes
write_notes(FILE_NAME, my_diary_entries)

# 6. Call read_notes to read and print the content back
read_notes(FILE_NAME)


# --- Notes on Classes and Objects ---
# `class ClassName:`: Defines a new class. Class names are typically TitleCase.
# `def __init__(self, ...):`: This is the constructor method. It's automatically called
#                             when a new object (instance) of the class is created.
# `self`: This keyword refers to the instance of the class itself. It's the first
#         parameter in every method and is used to access attributes and other methods
#         belonging to that specific object (e.g., `self.attribute_name`).
# Attributes: Variables associated with the object (e.g., `self.name`).
# Methods: Functions associated with the object (e.g., `self.greet()`).

# --- Challenge 11: Create a 'Student' Class ---

# Your task:
# 1. Define a class named `Student`.
# 2. Inside the `Student` class, define the `__init__` (constructor) method.
#    This method should accept `self`, `name`, and `major` as arguments.
# 3. Inside `__init__`, initialize two attributes for the `Student` object:
#    `self.name` and `self.major`, using the values passed as arguments.
# 4. Define another method inside the `Student` class called `introduce(self)`.
#    This method should print a message like:
#    `f"Hi, my name is {self.name} and I am studying {self.major}."`
# 5. Outside the class, create an object (an instance) of your `Student` class.
#    Pass your name and your desired major (e.g., "Computer Science Data Analytics")
#    as arguments when creating the object.
# 6. Call the `introduce()` method on your newly created student object.

# Write your code below this line:
class Student:
    def __init__(self, name, major):
        self.name = name  # Initialize the name attribute
        self.major = major  # Initialize the major attribute

    def introduce(self):
        # Print a message introducing the student
        print(f"Hi, my name is {self.name} and I am studying {self.major}.")

# Create an instance of the Student class
my_student = Student("Tushar", "Computer Science Data Analytics")
# Call the introduce method on the student object
my_student.introduce()

# --- Additional Notes on Classes ---
# Classes are blueprints for creating objects.  
# An object is an instance of a class.
# You can think of a class as a template, and an object as a specific instance of
# that template.
# Classes can have attributes (data) and methods (functions).
# Attributes are like variables that belong to the class.
# Methods are functions that define behaviors of the class.
# Classes can also inherit from other classes, allowing for code reuse and organization.
# Inheritance allows one class (child) to inherit attributes and methods from another class (parent).
# This is useful for creating a hierarchy of classes and sharing functionality.

# --- Notes on Inheritance ---
# `class ChildClass(ParentClass):`: This is how you define a class that inherits from another.
# `super().__init__(...)`: This is crucial! It calls the `__init__` method of the parent class.
#                        You use this to make sure the parent's attributes are initialized.
# Overriding methods: A child class can redefine a method that already exists in the parent.

# --- Challenge 12: Implement Inheritance with 'Person' and 'Student' ---

# Your task:
# 1. Define a `Person` class:
#    a. It should have an `__init__` method that takes `self` and `name` as arguments.
#    b. It should initialize `self.name`.
#    c. It should have a method `greet(self)` that prints `f"Hello, my name is {self.name}."`.
#
# 2. Modify your existing `Student` class to inherit from `Person`:
#    a. Change `class Student:` to `class Student(Person):`.
#    b. In `Student`'s `__init__` method:
#       i. It should now accept `self`, `name`, and `major` (just like before).
#       ii. **Crucially**, call the parent's `__init__` method using `super().__init__(name)`.
#       iii. Initialize `self.major` (as before).
#    c. Keep the `introduce(self)` method in `Student` as it was.
#
# 3. Create an instance of your new `Student` class (e.g., `my_special_student`).
#    Pass your name and major.
#
# 4. Call *both* `my_special_student.greet()` (inherited from Person) and
#    `my_special_student.introduce()` (from Student).

# Write your code below this line:

# 1. Define the Parent Class: Person
class Person:
    # The __init__ method for the Person class initializes the 'name' attribute.
    def __init__(self, name):
        self.name = name  # Every Person has a name

    # The greet method is a behavior common to all Persons.
    def greet(self):
        print(f"Hello, my name is {self.name}.")

# 2. Define the Child Class: Student, inheriting from Person
# Notice `(Person)` after `Student`, which indicates it inherits from Person.
class Student(Person):
    # The Student's __init__ method now takes 'name' (for the Person part) and 'major'.
    def __init__(self, name, major):
        # Crucial step: Call the parent's (Person's) __init__ method using super().
        # This initializes the 'name' attribute that Student inherits from Person.
        super().__init__(name)
        
        # Now, initialize attributes specific to the Student class.
        self.major = major  # Only Students have a major

    # The introduce method is specific to the Student class.
    # It uses 'self.name' (inherited) and 'self.major' (Student's own attribute).
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am studying {self.major}.")

# 3. Create an instance of the Student class
# When creating a Student object, you pass arguments for both the Person's __init__ (name)
# and the Student's __init__ (major).
my_special_student = Student("Tushar", "Computer Science Data Analytics")

# 4. Call methods from both the parent and child classes
print("--- Calling inherited method ---")
# Call the 'greet' method, which was inherited from the Person class.
my_special_student.greet()

print("\n--- Calling Student's own method ---")
# Call the 'introduce' method, which is defined in the Student class itself.
my_special_student.introduce()

# You can also access attributes directly, whether inherited or specific:
print(f"\nAccessing attributes: Name: {my_special_student.name}, Major: {my_special_student.major}")

# --- Notes on Polymorphism ---
# Polymorphism allows different objects to respond to the same method call in unique ways.
# This often relies on a common base class (parent) or simply having methods with the same name
# across different classes.
# The core idea is that you can treat objects of different types uniformly.

# --- Challenge 13: Demonstrate Polymorphism with Animal Sounds ---

# Your task:
# 1. Define a base class called `Animal`.
#    a. Give it an `__init__` method that takes `self` and `name`.
#    b. Initialize `self.name`.
#    c. Define a method `make_sound(self)` that simply prints `f"{self.name} makes a sound."`.
#
# 2. Define two child classes that inherit from `Animal`: `Dog` and `Cat`.
#    a. For both `Dog` and `Cat`:
#       i. Their `__init__` method should take `self` and `name`.
#       ii. They should call `super().__init__(name)` to initialize the `name` from the `Animal` parent.
#    b. For `Dog`:
#       i. Override the `make_sound(self)` method to print `f"{self.name} barks: Woof!"`.
#    c. For `Cat`:
#       i. Override the `make_sound(self)` method to print `f"{self.name} meows: Meow!"`.
#
# 3. Create instances of `Dog` and `Cat` (e.g., `my_dog`, `my_cat`).
# 4. Create a list containing these `Animal` objects (e.g., `[my_dog, my_cat]`).
# 5. Loop through the list of animals and call the `make_sound()` method on each one.
#    Observe how Python calls the correct, specialized `make_sound()` for each object.

# Write your code below this line:


# 1. Define the base class Animal
class Animal:       

    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def make_sound(self):
        print(f"{self.name} makes a sound.")  # Default sound behavior

# 2. Define the Dog class inheriting from Animal
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  # Call the parent class's __init__ method

    def make_sound(self):
        print(f"{self.name} barks: Woof!")  # Dog-specific sound behavior

# 2. Define the Cat class inheriting from Animal
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)  # Call the parent class's __init__ method

    def make_sound(self):
        print(f"{self.name} meows: Meow!")  # Cat-specific sound behavior


# 3. Create instances of Dog and Cat
my_dog = Dog("Buddy")  # Create a Dog object named Buddy
my_cat = Cat("Whiskers")  # Create a Cat object named Whiskers
# 4. Create a list of Animal objects
animals = [my_dog, my_cat]  # List containing both Dog and Cat objects
# 5. Loop through the list and call make_sound on each animal
for animal in animals:
    animal.make_sound()  # Calls the appropriate make_sound method for each animal

# --- Notes on Encapsulation ---
# Encapsulation is bundling data and methods, and restricting direct access to data.
# In Python, 'protected' attributes conventionally start with a single underscore (`_`).
# You provide 'getter' methods to read the data and 'setter' methods to modify it.

# --- Challenge 14: Encapsulate the Student's Age ---

# Your task:
# 1. Start with your `Student` class (from Challenge 11, without inheritance for simplicity,
#    or you can adapt your Person/Student if you prefer a challenge!).
#    Let's simplify and use: `class Student:`
#    `__init__(self, name, major, age)`
#    Initialize `self.name`, `self.major`, and `self.age`.
#
# 2. **Make the `age` attribute protected**:
#    Change `self.age = age` to `self._age = age`.
#    (Remember, this is a convention, not a strict enforcement in Python).
#
# 3. **Create a 'getter' method for age**:
#    Define a method `get_age(self)` that returns `self._age`.
#
# 4. **Create a 'setter' method for age**:
#    Define a method `set_age(self, new_age)`.
#    Inside this method, add a basic **validation**:
#    If `new_age` is positive (greater than 0), update `self._age = new_age`.
#    Otherwise, print an error message (e.g., "Age cannot be negative or zero.").
#
# 5. Create an instance of your `Student` class with a name, major, and an initial age.
# 6. Try to:
#    a. Print the age using the `get_age()` method.
#    b. Update the age using `set_age()` with a valid age. Print again to confirm.
#    c. Try to update the age using `set_age()` with an invalid age (e.g., -5). Observe the error message.
#    d. (Optional): Try to directly access and modify `my_student._age` (to see that it's possible but discouraged).

# Write your code below this line: 


class Student:
    def __init__(self, name, major, age):
        self.name = name  # Initialize the name attribute
        self.major = major  # Initialize the major attribute
        self._age = age  # Initialize the protected age attribute

    def get_age(self):
        return self._age  # Getter method to access the protected age

    def set_age(self, new_age):
        if new_age > 0:  # Basic validation for age
            self._age = new_age  # Update the protected age attribute
        else:
            print("Age cannot be negative or zero.")  # Error message for invalid age

# Create an instance of the Student class
my_student = Student("Tushar", "Computer Science Data Analytics", 22)       
# Print the initial age using the getter method
print(f"Initial age: {my_student.get_age()}")

# Update the age using the setter method with a valid age
my_student.set_age(23)
# Print the updated age
print(f"Updated age: {my_student.get_age()}")

# Try to update the age with an invalid value
my_student.set_age(-5)  # This should print an error message
# Attempt to directly access the protected attribute (not recommended)
print(f"Directly accessing protected age: {my_student._age}")  # This is
# discouraged but possible in Python


# --- Notes on Abstraction and Abstract Base Classes (ABCs) ---
# Abstraction: Showing only essential information and hiding complex details.
# ABCs: In Python, used to define abstract classes and methods that *must* be implemented by subclasses.
# `from abc import ABC, abstractmethod`: Import these to create ABCs.
# `class AbstractClassName(ABC):`: Inherit from ABC to make a class abstract.
# `@abstractmethod`: Decorator placed above a method definition to make it abstract.
#                   An abstract method has no implementation (no body), only a definition.
# Concrete classes: Classes that inherit from an ABC must implement all abstract methods.
#                   You cannot create an instance of an abstract class directly.

# --- Challenge 15: Implement Abstraction with Shapes ---

# Your task:
# 1. Import `ABC` and `abstractmethod` from the `abc` module.
#
# 2. Define an **Abstract Base Class** called `Shape`:
#    a. It should inherit from `ABC`.
#    b. Define an `__init__` method that takes `self` and `color` as arguments, and initializes `self.color`.
#    c. Define an `@abstractmethod` called `area(self)`. This method should only have `pass` as its body.
#       (It's a placeholder, indicating that subclasses *must* provide their own implementation).
#    d. Define a concrete (non-abstract) method `describe(self)` that prints `f"This is a {self.color} shape."`.
#
# 3. Define a concrete class `Circle` that inherits from `Shape`:
#    a. Its `__init__` method should take `self`, `color`, and `radius`.
#    b. It should call `super().__init__(color)` to initialize the `color`.
#    c. It should initialize `self.radius`.
#    d. **Implement** the `area(self)` method to calculate the area of a circle (`pi * radius^2`).
#       You can use `3.14159` for pi or `math.pi` (if you `import math`).
#
# 4. Define a concrete class `Rectangle` that inherits from `Shape`:
#    a. Its `__init__` method should take `self`, `color`, `width`, and `height`.
#    b. It should call `super().__init__(color)`.
#    c. It should initialize `self.width` and `self.height`.
#    d. **Implement** the `area(self)` method to calculate the area of a rectangle (`width * height`).
#
# 5. Create instances of `Circle` and `Rectangle` (e.g., `my_circle`, `my_rectangle`).
# 6. Call the `describe()` method on both.
# 7. Call the `area()` method on both and print their calculated areas.
# 8. (Optional Challenge): Try to create an instance of the `Shape` class directly (e.g., `s = Shape("green")`)
#    and observe the `TypeError` you get, proving it's an abstract class.

# --- Your Perfect Solution for Challenge 15 (Abstraction) ---

from abc import ABC, abstractmethod
import math # Good practice to import math for pi if using it

# 1 & 2. Define the Abstract Base Class Shape
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        # This method has no implementation here; it MUST be implemented by subclasses.
        pass

    def describe(self):
        print(f"This is a {self.color} shape.")

# 3. Define the concrete class Circle, inheriting from Shape
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color) # Initialize inherited 'color'
        self.radius = radius

    # Implement the abstract 'area' method for Circle
    def area(self):
        return math.pi * (self.radius ** 2) # Using math.pi for better precision

# 4. Define the concrete class Rectangle, inheriting from Shape
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color) # Initialize inherited 'color'
        self.width = width
        self.height = height

    # Implement the abstract 'area' method for Rectangle
    def area(self):
        return self.width * self.height

# 5. Create instances of Circle and Rectangle
my_circle = Circle("red", 5)
my_rectangle = Rectangle("blue", 4, 6)

# 6. Call the describe method on both shapes
my_circle.describe()
my_rectangle.describe()

# 7. Call the area method on both shapes and print the results
print(f"Circle area: {my_circle.area():.2f}") # Formatted to 2 decimal places
print(f"Rectangle area: {my_rectangle.area()}")

# 8. Attempt to create an instance of the abstract class Shape (this correctly raises a TypeError)
try:
    s = Shape("green")
except TypeError as e:
    print(f"Error: {e}")

