# # 
# Day 1: Python Basics for Java/JavaScript Developers
# ====================================================
# Author: Kenon Sahirani
# Purpose: Python Mastery

# This file is a complete hands-on tutorial. Run each section
# and modify the code to experiment!

# Run with: python3 01_python_basics.py
# # 

print("=" * 60)
print("SECTION 1: Variables and Data Types")
print("=" * 60)

# result
# =============================================================================
# SECTION 1: Variables and Data Types
# =============================================================================

# Python is dynamically typed (like JavaScript, unlike Java)
# Without type hints (works, but not production-ready)

name = "Kenon"
age = 25
is_developer = True

# With type hints (recommended for production code)
name: str = "Kenon"
age: int = 32
height: float = 5.9
is_developer: bool = True
nothing: None = None # Python's null

print(f"Name: {name}, Age: {age}, Developer: {is_developer}")

# Type checking at runtime is (useful for debugging)
print(f"Type of name: {type(name)}") # <class 'str'>
print(f"Type of age: {type(age)}") # <class 'int'>

# COMPARISON WITH JAVA:
# Java:   String name = "Kenon";    int age = 25;
# Python: name: str = "Kenon"       age: int = 25

print()

# ####################################################
print("=" * 60)
print("SECTION 2: Strings and F-Strings")
print("=" * 60)
# =============================================================================
# SECTION 2: Strings and F-Strings
# =============================================================================

# F-Strings (Python 3.6+)- Your new best friend!
first_name: str = "Kenon"
last_name: str = "Sahirani"
years_exp: int = 2

# Old way (like Java's String.format or concatenation)
message_old = "Hello" + " " + first_name + " " + last_name
print(f"Old way: {message_old}")

# F-string way (ALWAYS use this!)
message_new: str = f"Hello, {first_name} {last_name}!"
print(f"F-String: {message_new}")

# F-string can contain expressions!
print(f"In 5 years, you'll have {years_exp + 5} years of experience")
print(f"Your name in uppercase: {first_name.upper()}")
print(f"Name length: {len(first_name)} characters")

#Formatting numbers
pi: float = 3.14159265359
print(f"Pi to 2 decimals: {pi:.2f}") #3.14
print(f"Percentage: {0.856:.1%}") # 85.6%

# Multi-line strings (triple qoutes)
bio: str = """
Name: Kenon Sahirani
Role: Full-Stack Developer
Skills: React, Java Spring Boot, PostgreSQL
"""
print(bio)

# Common String methods
text: str = " Hello World "
print(f"strip(): '{text.strip()}'")  #Remove whitespace
print(f"lower(): '{text.lower()}'") #Lowercase
print(f"upper(): '{text.upper()}'") #Uppercase
print(f"replace(): '{text.replace('World', 'Kenon')}'")
print(f"split():  {text.split()}") # Returns List

print()


