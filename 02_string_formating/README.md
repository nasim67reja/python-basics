# String Formatting in Python

This repository provides a brief explanation of string formatting in Python using the `format()` method. Understanding string formatting is crucial for building clear and dynamic strings in your Python programs.

## Usage Examples

### Providing Values in Order

```python
greeting = "Hello {} {}".format("John", "How are You.?")
# Output: "Hello John How are You.?"
```
### Providing Values by Position

```python
greeting = "Hello {1} {0}".format("How are You.?", "nasim")
# Output: "Hello nasim How are You.?"
```
### Reusing Values
```python
greeting = "Hello {0} {0}".format("nasim")
# Output: "Hello nasim nasim"
```
### Variable Substitution
```python
name = "nasim"
greeting = "Hello {}".format(name)
# Output: "Hello nasim"
```
### Missing or Extra Values
```python
# IndexError (not enough values)
greeting = "Hello {} {}".format("nasim")
```
```python
greeting = "Hello {} {}".format("nasim", "How are You.?", "Extra Value")
# "Extra Value" will be ignored
# Output: "Hello nasim How are You.?"

greeting="Hello {name} {ask}".format(ask,name) #KeyError: 'name'
```

### Named Arguments

```python
greeting = "Hello {name} {message}".format(name="nasim", message="How are You.?")
# Output: "Hello nasim How are You.?"
```

### instead of string we can put any expression
```python
add="2+2={}"
print(add.format(2+2))
```