# # 
# Day 1: Python Basics for Java/JavaScript Developers
# ====================================================
# Author: Kenon Sahirani
# Purpose: Python Mastery

# This file is a complete hands-on tutorial. Run each section
# and modify the code to experiment!

# Run with: python3 01_python_basics.py
# # 

# =============================================================================
# SECTION 1: Variables and Data Types
# =============================================================================
print("=" * 60)
print("SECTION 1: Variables and Data Types")
print("=" * 60)
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

# =============================================================================
# SECTION 2: Strings and F-Strings
# =============================================================================
print("=" * 60)
print("SECTION 2: Strings and F-Strings")
print("=" * 60)
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

# =============================================================================
# SECTION 3: Collections - Lists, Tuples, Sets, Dicts
# =============================================================================

print("=" * 60)
print("SECTION 3: Collections - Lists, Tuples, Sets, Dicts ")
print("=" * 60)

# -----------------------------------------------------------------------------
# LISTS (like Java ArrayList, JavaScript Array) - Mutable, ordered
# -----------------------------------------------------------------------------
print("\n ---- List ----")

# Without type hints
skills = ["React", "Java", "PostgreSQL"]

# WITH type hints (production-ready)
skills: list[str] = ["React", "Java", "PostgreSQL", "Python"]

print(f"Skills: {skills}")
print(f"First skill: {skills[0]}") # React (0 - indexed like java)
print(f"Last Skill: {skills[-1]}") # Python (negative indexing!)
print(f"First two: {skills[:2]}")  # ['React, 'Java'] (slicing)
print(f"Length: {len(skills)}")

# Modifying lists
skills.append("FastAPI") # Add to end
skills.insert(0, "TypeScript") # Insert at position
removed = skills.pop() # Remove and return last
skills.remove("Java") # Remove by value

print(f"After modifications: {skills}")

# List comprehension (PYTHON SUPERPOWER - learn this well!)
numbers: list[int] = [1, 2, 3, 4, 5]
squared: list[int] = [n ** 2 for n in numbers]
print(f"Squared: {squared}") #[1, 4, 9, 16, 25]

# With Condition
evens: list[int] = [n for n in numbers if n % 2 == 0]
print(f"Evens only: {evens}") #[2, 4]

# COMPARISON:
# Java:   List<Integer> squared = numbers.stream().map(n -> n * n).collect(Collectors.toList());
# Python: squared = [n ** 2 for n in numbers]

# -----------------------------------------------------------------------------
# TUPLES - Immutable, ordered (use for fixed data)
# -----------------------------------------------------------------------------
print("\n--- Tuples ---")

#Tuples are like lists but CANNOT be changed
coordinates: tuple[float, float] = (14.5995, 120.9842)
rgb_color: tuple[int, int, int] = (255, 128, 0)

print(f"Coordinates: {coordinates}")
print(f"Latitude: {coordinates[0]}")

#Tuple unpacking (very Pythonic!)
lat, lng = coordinates
print(f"Lat: {lat}, Lng: {lng}")

#Use tuples for 
# - Function returning multiple values
# - Dictionary keys (lists can't be keys)
# - Data that shouldn't change

# -----------------------------------------------------------------------------
# SETS - Unique values, unordered (like Java HashSet)
# -----------------------------------------------------------------------------
print("\n--- Sets ---")

languages: set[str] = {"Python", "Java", "Javascript", "Python"} # Duplicate ignored
print(f"Languages: {languages}") # Python appears once

#Set operations
frontend: set[str] = {"React", "Vue", "Angular"}
backend: set[set] = {"Django", "Spring", "React"} # React is full-stack

print(f"Union: {frontend | backend}")  # All unique
print(f"Intersection: {frontend & backend}") # Common (React)
print(f"Difference: {frontend - backend}") # In frontend, not backend

# Check membership (O(1) - very fast!)
print(f"Is React in frontend? {'React' in frontend}")  # True

# -----------------------------------------------------------------------------
# DICTIONARIES - Key-value pairs (like Java HashMap, JS Object)
# -----------------------------------------------------------------------------
print("\n--- Dictionaries ---")

# Basic dictionary
developer : dict[str, any] = {
    "name": "Kenon",
    "age": 25,
    "skills": ["React", "Java", "Python"],
    "is_Employed": False
}

print(f"Developer: {developer}")
print(f"Name: {developer['name']}")
print(f"Skills: {developer['skills']}")

# Safe access with .get() (returns None if key missing)
print(f"Salary: {developer.get('salary')}") # None
print(f"Salary: {developer.get('salary', 'N/A')}") # 'N/A' (default)

#Modifying
developer["is_Employed"] = True
developer["company"] = "LGI Tech"

# Dictionary methods
print(f"Keys: {list(developer.keys())}")
print(f"Values: {list(developer.values())}")
print(f"Items: {list(developer.items())}")

#Dictionary comprehension
numbers: list[int] = [1, 2, 3, 4, 5]
squared_dict: dict[int, int] = {n: n**2 for n in numbers}
print(f"Squared dict: {squared_dict}") #{1: 1, 2: 4, 3: 9, ...}

#Nested dictionaries (common in APIs)
user_data: dict = {
    "user": {
    "profile": {
        "name": "Kenon",
        "location": "Philippines"
        }
    }
}
print(f"Location: {user_data['user']['profile']['location']}")
print()