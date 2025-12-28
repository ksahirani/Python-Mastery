"""
Day 1: Practice Exercises
=========================
Complete these exercises to solidify your Python basics.
Each exercise has hints and a solution at the bottom.

Run with: python3 02_exercises.py
"""

print("=" * 60)
print("DAY 1 EXERCISES")
print("=" * 60)
# =============================================================================
# EXERCISE 1: F-String Practice
# =============================================================================
print("\n--- Exercise 1: F-String Practice ---")
# TODO: Create variables and use f-strings to print:
# "Kenon is a Full-Stack Developer with 2 years of experience."

#Your code here:
name: str = "Kenon"
role: str = "Full-Stack Developer"
years: int = 2

#TODO: Print using f-string
result: str = f"{name} is a {role} with {years} years of experience."
print (result)

# =============================================================================
# EXERCISE 2: List Operations
# =============================================================================
print("\n --- Exercise 2: List Operations ---")

# Given the list of scores:
scores: list[int] = [85, 92, 78, 95, 88, 76, 90]

#TODO: Complete these operations:
# 1. Find the average score
average: float = sum(scores) / len(scores)
print(f"Average: {average:.2f}")

#2. Find scores above 85 using list comprehension
above_85: list[int] = [s for s in scores if s > 85]
print(f"Scores above 85: {above_85}")

#3. Create a new list with 5 bonus points added to each score
with_bonus: list[int] = [s + 5 for s in scores]
print(f"With bonus: {with_bonus}")

# =============================================================================
# EXERCISE 3: Dictionary Practice
# =============================================================================
print("\n --- Exercise 3: Dictionary Practice ---")

#TODO: Create a dictionary representing yourself as a developer
#Include: name, skills (list), years_experience, is_available

developer: dict[str, any] = {
    "name": "Kenon",
    "skills": ["React", "Java", "Spring Boot", "PostgreSQL", "Python"],
    "years_experience": 2,
    "is_available": True
}

#TODO: Print each skill on a new line using a loop
print("Skills:")
for skill in developer["skills"]:
    print(f" - {skill}")

#TODO: Add a new key "target_company" with value "LGI Tech"
developer["target_company"] = "LGI Tech"
print(f"\nTarget: {developer['target_company']}")

# =============================================================================
# EXERCISE 4: Function with Type Hints
# =============================================================================
print("\n --- Exercise 4: Functions ---")

#TODO: Write a function that takes a list of numbers
# and returns a dictionary with 'min', 'max', 'sum', 'average'

def analyze_numbers(numbers: list[int]) -> dict[str, float]:
    """Analyze a list of numbers and return statistics.
    
    Args:
        numbers: A list of integers to analyze.
        
    Returns:
        A dictionary containing min, max, sum, and average.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot analyze empty list")
    
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers)
    }

#Test your function
test_numbers: list[int] = [10, 20, 30, 40, 50]
stats: dict = analyze_numbers(test_numbers)
print(f"Stats: {stats}")

# =============================================================================
# EXERCISE 5: List Comprehension Challenge
# =============================================================================
print("\n --- Exercise 5: List Comprehension Challenge ---")

# Given a list of words:
words: list[str] = ["python", "java", "react", "spring", "postgresql"]

#TODO: Create a list of words that have more than 5 characters, in uppercase
long_words: list[str] = [w.upper() for w in words if len(w) > 5]
print(f"Long words (uppercase): {long_words}")

#TODO: Create a dictionary mapping each word to its length
word_lengths: dict[str, int] = {w: len(w) for w in words}
print(f"Word lengths: {word_lengths}")

# =============================================================================
# EXERCISE 6: Pixel Grid (Assessment Preview)
# =============================================================================
print("\n --- Exercise 6: Pixel grid(Assessment Preview) ---")

def create_pixel_grid(width: int, height: int, fill_value: int = 0) -> list[list[int]]:
    """Create a 2D pixel grid filled with a value.
    
    Args:
        width: Grid width.
        height: Grid height.
        fill_value: Value to fill each pixel (default 0).
        
    Returns:
        2D list representing the pixel grid.
    """
    return[[fill_value for _ in range(width)] for _ in range(height)]

def count_non_zero_pixels(grid: list[list[int]]) -> int:
    """Count pixels that are not zero.
    
    Args:
        grid: 2D pixel grid.
        
    Returns:
        Count of non-zero pixels.
    """
    count: int = 0

    for row in grid:
        for pixel in row:
            if pixel != 0:
                count += 1

    return count

# Alternative using sum and comprehension:
def count_non_zero_pixels_v2(grid: list[list[int]]) -> int:
    """Count non-zero pixels using comprehension."""
    return sum(1 for row in grid for pixel in row if pixel != 0)


# Test
grid: list[list[int]] = create_pixel_grid(10, 10)
print(f"Created 10x10 grid")
print(f"Non-zero pixels: {count_non_zero_pixels(grid)}")

# Set some pixels
grid[0][0] = 255
grid[5][5] = 128
grid[9][9] = 64
print(f"After setting 3 pixels, non-zero count: {count_non_zero_pixels(grid)}")

# =============================================================================
# EXERCISE 7: Error Handling Preview
# =============================================================================
print("\n --- Exercise 7: Error Handling ---")

def safe_divide(a: float, b: float) -> float | None:
    """Safely divide two numbers.
    
    Args:
        a: Numerator.
        b: Denominator.
        
    Returns:
        Result of division, or None if division by zero.
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

