# Import statements
import math
from datetime import datetime

# Constants
PI = 3.14159
EULER_NUMBER = 2.71828

# Function definitions
def calculate_area(radius: float) -> float:
    """Calculate the area of a circle given its radius."""
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return PI * radius ** 2

def print_greeting(name: str = "World") -> None:
    """Print a greeting message."""
    print(f"Hello, {name}!")

# Class definitions
class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self.area = calculate_area(radius)
    
    def describe(self) -> str:
        return f"A circle with radius {self.radius} has an area of {self.area:.2f}"

# List comprehension
squares = [x ** 2 for x in range(10)]

# Dictionary usage
circle_info = {
    "radius": 5.0,
    "area": calculate_area(5.0),
    "created_at": datetime.now()
}

# Try-except block
try:
    invalid_area = calculate_area(-3)
except ValueError as e:
    print(f"Error: {e}")

# Lambda functions
double = lambda x: x * 2

# Main execution
if __name__ == "__main__":
    print_greeting("Pythonista")
    
    my_circle = Circle(5.0)
    print(my_circle.describe())
    
    print("Squares:", squares)
    print("Circle Info:", circle_info)
    print("Double of 5:", double(5))
