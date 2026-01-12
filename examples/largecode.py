"""
Big Example Code for Python Code Analyzer
This file contains multiple classes, functions, imports, decorators,
async functions, nested functions, and error handling.
"""

import os
import sys
import json
import math
import random
import datetime
from collections import defaultdict, Counter
from typing import List, Dict, Any, Optional, Tuple


# -------------------------
# Utility Functions
# -------------------------

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def get_env_variable(key: str, default: str = "") -> str:
    """Fetch environment variable safely."""
    return os.environ.get(key, default)


def factorial(n: int) -> int:
    """Compute factorial using loop."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> List[int]:
    """Generate fibonacci sequence up to n terms."""
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
    """Calculate simple statistics from a list of numbers."""
    if not numbers:
        return {"mean": 0.0, "min": 0.0, "max": 0.0}

    return {
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }


def pretty_print(data: Any) -> None:
    """Print JSON style output nicely."""
    print(json.dumps(data, indent=2, ensure_ascii=False))


# -------------------------
# Decorators
# -------------------------

def logger(func):
    """Decorator to log function call."""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper


def time_it(func):
    """Decorator to measure execution time."""
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        print(f"[TIME] {func.__name__} took: {end - start}")
        return result
    return wrapper


# -------------------------
# Classes
# -------------------------

class Person:
    """A basic person class."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        """Check if person is adult."""
        return self.age >= 18

    def birthday(self):
        """Increase age by 1."""
        self.age += 1


class Student(Person):
    """Student class inherits Person."""

    def __init__(self, name: str, age: int, roll_no: str):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks: Dict[str, int] = {}

    def add_mark(self, subject: str, mark: int):
        """Add marks for subject."""
        self.marks[subject] = mark

    def average(self) -> float:
        """Calculate average marks."""
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def top_subject(self) -> Optional[str]:
        """Return subject with max marks."""
        if not self.marks:
            return None
        return max(self.marks, key=self.marks.get)


class Calculator:
    """Simple calculator class."""

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def sub(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def mul(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def power(a: float, b: float) -> float:
        return a ** b


class DataStore:
    """Stores and manages data using dictionary."""

    def __init__(self):
        self.data: Dict[str, Any] = {}

    def set_value(self, key: str, value: Any):
        self.data[key] = value

    def get_value(self, key: str, default=None):
        return self.data.get(key, default)

    def remove_value(self, key: str):
        if key in self.data:
            del self.data[key]

    def keys(self):
        return list(self.data.keys())


# -------------------------
# Advanced Features
# -------------------------

class FileManager:
    """File manager for reading/writing files."""

    def __init__(self, base_path: str):
        self.base_path = base_path

    def build_path(self, filename: str) -> str:
        return os.path.join(self.base_path, filename)

    def save_text(self, filename: str, content: str):
        path = self.build_path(filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def read_text(self, filename: str) -> str:
        path = self.build_path(filename)
        with open(path, "r", encoding="utf-8") as f:
            return f.read()


class TaskManager:
    """Task manager for adding and completing tasks."""

    def __init__(self):
        self.tasks: Dict[int, Dict[str, Any]] = {}
        self.counter = 0

    def add_task(self, title: str, priority: int = 1) -> int:
        self.counter += 1
        self.tasks[self.counter] = {
            "title": title,
            "priority": priority,
            "done": False
        }
        return self.counter

    def complete_task(self, task_id: int):
        if task_id in self.tasks:
            self.tasks[task_id]["done"] = True

    def get_pending_tasks(self) -> List[Dict[str, Any]]:
        return [t for t in self.tasks.values() if not t["done"]]

    def sort_by_priority(self) -> List[Dict[str, Any]]:
        return sorted(self.tasks.values(), key=lambda x: x["priority"], reverse=True)


# -------------------------
# Async function example
# -------------------------

async def async_task(name: str) -> str:
    """Example async function."""
    return f"Async Task Completed for: {name}"


# -------------------------
# Complex Functions
# -------------------------

@logger
@time_it
def generate_random_data(size: int = 100) -> List[int]:
    """Generate list of random integers."""
    return [random.randint(1, 1000) for _ in range(size)]


def group_numbers(numbers: List[int]) -> Dict[int, List[int]]:
    """Group numbers by last digit."""
    groups = defaultdict(list)
    for n in numbers:
        groups[n % 10].append(n)
    return dict(groups)


def analyze_text(text: str) -> Dict[str, Any]:
    """Analyze a string and return stats."""
    words = text.split()
    counter = Counter(words)
    return {
        "word_count": len(words),
        "unique_words": len(counter),
        "most_common": counter.most_common(3)
    }


def nested_function_example(x: int) -> int:
    """Nested function demo."""
    def inner(y: int) -> int:
        return y * y
    return inner(x) + inner(x + 1)


# -------------------------
# Main Runner
# -------------------------

def main():
    """Main execution logic."""
    print(greet("Harishlal"))

    # Math demo
    nums = generate_random_data(50)
    stats = calculate_statistics(nums)
    print("Stats:", stats)

    # Group numbers
    grouped = group_numbers(nums)
    print("Grouped keys:", grouped.keys())

    # Student demo
    student = Student("Harishlal", 19, "CSE1023")
    student.add_mark("Math", 95)
    student.add_mark("Python", 98)
    print("Student avg:", student.average())
    print("Top subject:", student.top_subject())

    # Task manager demo
    tm = TaskManager()
    tm.add_task("Complete analyzer project", priority=5)
    tm.add_task("Push to GitHub", priority=4)
    tm.complete_task(1)
    print("Pending tasks:", tm.get_pending_tasks())

    # Text analysis demo
    txt = "python analyzer python tool analyzer code python"
    print("Text analysis:", analyze_text(txt))

    # Nested function demo
    print("Nested func output:", nested_function_example(5))

    # Env variable demo
    print("PATH snippet:", get_env_variable("PATH")[:40], "...")

    # System info
    print("Python version:", sys.version)


if __name__ == "__main__":
    main()
