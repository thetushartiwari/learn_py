# 🐍 Python Revision Notes (Interview & Revision Friendly)

A structured summary of Python basics → OOP, with common interview Q&A.  
Use alongside `practice.py` for practical reinforcement.

---

## 📌 Day 1 – Data Types & Variables
- **Variables**: No explicit type declaration.  
- **Data Types**:
  - `int` → whole numbers  
  - `float` → decimals  
  - `str` → text  
  - `bool` → True/False  
  - `list` → ordered, mutable  
  - `tuple` → ordered, immutable  
  - `dict` → key-value pairs  
  - `set` → unique, unordered

### 🔹 Interview Q&A
**Q: Difference between list and tuple?**  
A: Lists are mutable (changeable), tuples are immutable (fixed once created).

**Q: How are Python variables stored?**  
A: Python variables are references to objects in memory (everything is an object).

---

## 📌 Day 2 – Control Flow & Loops
- **Conditionals**: `if`, `elif`, `else` → decision making.  
- **Loops**:  
  - `for` → iterate over items.  
  - `while` → repeat until condition is false.  
- **Break & Continue** → control loop flow.

### 🔹 Interview Q&A
**Q: What’s the difference between `break` and `continue`?**  
A: `break` exits the loop completely, `continue` skips current iteration and moves to next.

**Q: Python has switch-case?**  
A: No. Use `if-elif-else` or dictionaries to simulate.

---

## 📌 Day 3 – Functions, Scope & Modules
- **Functions**: Reusable blocks (defined using `def`).  
- **Arguments**: Positional, keyword, default, `*args`, `**kwargs`.  
- **Return**: Functions may return values.  
- **Scope**:  
  - Local, Enclosing, Global, Built-in (LEGB).  
- **Modules**: Reusable code files (`import math`).

### 🔹 Interview Q&A
**Q: Difference between local and global variables?**  
A: Local → defined inside a function. Global → accessible across program unless shadowed.  

**Q: What is recursion?**  
A: Function calling itself to solve subproblems (e.g., factorial).

---

## 📌 Day 4 – Collections
- **List**: Ordered, mutable, duplicates allowed.  
- **Tuple**: Ordered, immutable.  
- **Set**: Unordered, unique elements only.  
- **Dict**: Key-value pairs, fast lookups.

### 🔹 Interview Q&A
**Q: Difference between shallow copy and deep copy?**  
A: Shallow copy → copies references (changes affect original). Deep copy → full independent copy.

**Q: Can dict keys be mutable?**  
A: No. Keys must be immutable (int, str, tuple, etc.).

---

## 📌 Day 5 – Strings & Regex
- Strings → immutable sequences of characters.  
- Regex (`re` module) → pattern matching.

Common regex:  
- `\d` → digit  
- `\w` → alphanumeric  
- `.` → any char  
- `^` / `$` → start / end of string  

### 🔹 Interview Q&A
**Q: How to check if a string is palindrome?**  
A: Compare string with its reverse.  

**Q: Difference between `is` and `==`?**  
A: `==` checks value equality, `is` checks object identity (memory address).

---

## 📌 Day 6 – File Handling & Exceptions
- **File Modes**:  
  - `'r'` → read  
  - `'w'` → write (overwrite)  
  - `'a'` → append  
- Use `with open(...)` for safety (auto-close).  
- **Exception Handling**: `try-except-finally`.

### 🔹 Interview Q&A
**Q: Difference between checked and unchecked exceptions?**  
A: Python only has runtime (unchecked) exceptions, not compile-time checked ones.  

**Q: Why use `with open()`?**  
A: Ensures file closes automatically, even on error.

---

## 📌 OOP Basics – Classes & Objects
- **Class** → blueprint.  
- **Object** → instance of class.  
- **Attributes** → data (variables).  
- **Methods** → behaviors (functions).  
- **Encapsulation**: restrict access using `_protected` or `__private`.  

### 🔹 Interview Q&A
**Q: Difference between `__init__` and normal methods?**  
A: `__init__` is constructor, auto-called when object is created.  

**Q: How to implement encapsulation in Python?**  
A: By using naming conventions (`_var`, `__var`) and getter/setter methods.

---

## 📌 OOP Advanced – Key Principles

### 🔹 Inheritance 🧬
- Child class inherits attributes/methods from parent.  
- Promotes reusability.  

**Q: Types of inheritance in Python?**  
A: Single, Multiple, Multilevel, Hierarchical, Hybrid.

---

### 🔹 Polymorphism 🎭
- Same method, different implementations.  
- Achieved via method overriding or operator overloading.

**Q: Example of polymorphism in Python?**  
A: `len()` works for strings, lists, tuples, etc.

---

### 🔹 Encapsulation 📦
- Bundle data + methods.  
- Hide internal details, expose only via public methods.  

**Q: How does Python enforce encapsulation?**  
A: By convention (`_protected`, `__private`) + name mangling.

---

### 🔹 Abstraction ☁️
- Hide implementation, show only essential features.  
- Achieved using **Abstract Base Classes (ABC)** with `@abstractmethod`.

**Q: Difference between abstraction & encapsulation?**  
A: Encapsulation → *how* data is hidden. Abstraction → *what* functionality is exposed without implementation details.

---

# ⚡ Interview-Style Practice Set
1. What are Python’s key features? (Dynamic typing, interpreted, OOP support, huge libraries).  
2. Difference between `list`, `set`, `tuple`, `dict`.  
3. Explain Python’s memory management. (Garbage collector, reference counting).  
4. Difference between `is` vs `==`.  
5. What are Python’s OOP principles? (Encapsulation, Abstraction, Inheritance, Polymorphism).  
6. How are exceptions handled? (`try-except-finally`, custom exceptions).  
7. Explain LEGB rule with example.  
8. Difference between shallow copy and deep copy.  
9. Mutable vs Immutable objects in Python.  
10. Explain how Python is both object-oriented and functional.  

