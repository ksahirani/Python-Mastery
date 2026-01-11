# # 
# Day 2: Functions & Object-Oriented Programming
# ====================================================
# Author: Kenon Sahirani
# Purpose: Python Mastery

# Topics
# 1. Advanced function concepts (*args, **kwargs)
# 2. Type hints in depth
# 3. Classes and OOP principles
# 4. Dunder methods (__str__, __repr__, __eq__, etc.)
# 5. Decorators (@property, @staticmethod, @classmethod)
# 6. Inheritance and composition

# Run with: python3 01_functions_oop.py
# # 

print("=" * 60)
print("DAY 2: Functions & Object-Oriented Programming")
print("=" * 60)

# =============================================================================
# SECTION 1: Advanced Function Parameters
# =============================================================================
print("\n" + "=" * 60)
print("Section 1: Advanced Function Parameters")
print("=" * 60)

# -----------------------------------------------------------------------------
# Default Parameters
# -----------------------------------------------------------------------------
print("\n--- Default Parameters ---")

def create_user(
        name: str,
        role: str = "Developer",
        active: bool = True
) -> dict:
    return {"name": name, "role": role, "active": active}

# Different ways to call
print(create_user("Kenon"))
print(create_user("Kenon", "Full-Stack"))
print(create_user("Kenon", role="Backend", active=False))

"""Create a user dictionary with optional defaults.
    
    Args:
        name: User's name (required).
        role: User's role (default: "Developer").
        active: Whether user is active (default: True).
        
    Returns:
        Dictionary containing user data.
    """


# IMPORTANT: Mutable default argument trap!
# DON'T do this:
def bad_append(item, items=[]):  # BUG: Same list reused!
    items.append(item)
    return items

# DO this instead:

def good_append(item: str, items: list | None = None) -> list:
    # Safely append to a list with None default.
    if items is None:
        items = []
    items.append(item)
    return items

print(f"\nGood append: {good_append('a')}")
print(f"Good append: {good_append('b')}") #Fresh list each time

# -----------------------------------------------------------------------------
# *args - Variable Positional Arguments
# -----------------------------------------------------------------------------
print("\n--- *args (Variable Positional Arguments) ---")

def sum_all(*numbers: int)-> int:
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2): {sum_all(1, 2)}")
print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")

# Unpacking a list into args
numbers = [10, 20, 30]
print(f"sum_all(*[10, 20, 30]): {sum_all(*numbers)}")

"""Sum any number of integers.
    
    Args:
        *numbers: Variable number of integers.
        
    Returns:
        Sum of all numbers.
    """