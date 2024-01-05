# List Comprehension

List comprehension is a concise way to create lists in Python. It provides a more readable and often more efficient way to generate lists compared to using traditional loops. The basic syntax of a list comprehension looks like this:

```python
new_list = [expression for item in iterable if condition]
```

- expression: The expression to evaluate and include in the new list.
- item: The variable representing each item in the iterable (e.g., a list, tuple, or string).
- iterable: The sequence of items to iterate over.
- condition (optional): A
  n optional condition to filter items based on a specified criteria.

### Here's a simple example:

```python
# Using a loop
squared_numbers = []
for number in range(1, 6):
    squared_numbers.append(number**2)

# Using list comprehension
squared_numbers_comp = [number**2 for number in range(1, 6)]

print(squared_numbers)        # Output: [1, 4, 9, 16, 25]
print(squared_numbers_comp)   # Output: [1, 4, 9, 16, 25]
```

In this example, both the traditional loop and the list comprehension generate a list of squared numbers from 1 to 5. The list comprehension is more concise and often considered more Pythonic.

### List comprehensions can also include an optional if condition to filter elements:

```python
even_squares = [number**2 for number in range(1, 6) if number % 2 == 0]
print(even_squares)  # Output: [4, 16]
```

This list comprehension generates a list of squared numbers but only includes those where the original number is even.

List comprehensions are a powerful tool in Python, allowing you to create succinct and readable code for list generation and transformation.
