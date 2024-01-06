my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}


## accessing values
key="name"
# print(my_dict[key]) # my_dict[any_valid_expression]

## modifying values

my_dict[key]="Nasim"

## adding key-values

my_dict["profession"]="Programmer"
print(my_dict)

# Dictionary Methods

keys_list=my_dict.keys()
values_list=my_dict.values()
items_list=my_dict.items()

# iteration on dictonaries

for items in my_dict: # similar to for items in my_dict.keys()
    # print(items)
    print(f"{items}:{my_dict[items]}")

for items in my_dict.values(): # similar to for items in my_dict.keys()
    print(items)

for keys,values in my_dict.items(): # this is called destructing
    print(keys,values)


# Checking if a key exist
    
print("name" in my_dict) # True
print("email" in my_dict) # False

# Dictionary Comprehension

squared_numbers_dict = {number: number**2 for number in range(1, 6)}
print(squared_numbers_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}