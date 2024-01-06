# Dictionaries in Python

In Python, a dictionary is a mutable and versatile collection that allows you to store key-value pairs. Here are key points about dictionaries in Python:

## Creating a Dictionary

You can create a dictionary using curly braces `{}` and specifying key-value pairs separated by colons `:`.

```python
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```

## Accessing Values

You can access the values in a dictionary using the keys.

```python
print(my_dict['name'])  # Output: John
print(my_dict['age'])   # Output: 25
```

## Modifying Values
Dictionaries are mutable, so you can modify values using their keys.

```python
my_dict['age'] = 26
print(my_dict['age'])  # Output: 26
```

## Adding New Key-Value Pairs
You can add new key-value pairs to a dictionary.

```python
my_dict['gender'] = 'Male'
print(my_dict)
# Output: {'name': 'John', 'age': 26, 'city': 'New York', 'gender': 'Male'}
```

## Dictionary Methods
Python dictionaries come with various methods such as keys(), values(), and items().

```python
keys_list = my_dict.keys()
values_list = my_dict.values()
items_list = my_dict.items()

print(keys_list)    # Output: dict_keys(['name', 'age', 'city', 'gender'])
print(values_list)  # Output: dict_values(['John', 26, 'New York', 'Male'])
print(items_list)   # Output: dict_items([('name', 'John'), ('age', 26), ('city', 'New York'), ('gender', 'Male')])
```

## iteration on dictonaries

```python
# iteration on dictonaries

for items in my_dict: # similar to for items in my_dict.keys()
    # print(items)
    print(f"{items}:{my_dict[items]}")

for items in my_dict.values(): # similar to for items in my_dict.keys()
    print(items)

for keys,values in my_dict.items(): # this is called destructing
    print(keys,values)```

## Checking if a Key Exists

You can use the in keyword to check if a key exists in a dictionary.

```python
print('name' in my_dict)  # Output: True
print('email' in my_dict) # Output: False

```

## Dictionary Comprehension

Similar to list comprehension, you can use dictionary comprehension to create dictionaries in a concise way.

```python
squared_numbers_dict = {number: number**2 for number in range(1, 6)}
print(squared_numbers_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```