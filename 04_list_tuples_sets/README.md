# Python Data Structures Overview

## Lists
- Ordered collection of elements.
- Mutable: Elements can be added, removed, or modified.
- Defined using square brackets `[]`.
- Example: `numbers = [1, 2, 3, 4, 5]`

## Tuples
- Ordered collection of elements.
- Immutable: Once created, elements cannot be added, removed, or modified.
- Defined using parentheses `()`.
- Example: `coordinates = (10, 20)`

## Sets
- Unordered collection of unique elements.
- Mutable: Elements can be added or removed, but individual elements are immutable.
- Defined using curly braces `{}`.
- Example: `unique_numbers = {1, 2, 3, 4, 5}`

### Key Differences
- **Mutability:**
  - Lists are mutable (can be modified).
  - Tuples are immutable (cannot be modified after creation).
  - Sets are mutable (can be modified).

- **Order:**
  - Lists and tuples maintain the order of elements.
  - Sets do not guarantee any specific order.

- **Uniqueness:**
  - Lists and tuples can contain duplicate elements.
  - Sets only contain unique elements.

Choose the appropriate data structure based on your specific use case. Lists are versatile, tuples provide immutability, and sets ensure uniqueness.


# Python List Methods

Here are some commonly used methods for Python lists:

1. **append:** Adds a single element to the end of the list.
2. **clear:** Removes all elements from the list.
3. **copy:** Returns a shallow copy of the list.
4. **count:** Returns the number of occurrences of a specified element.
5. **extend:** Adds the elements of an iterable to the end of the list.
6. **index:** Returns the index of the first occurrence of a specified element.
7. **insert:** Inserts an element at the specified position.
8. **pop:** Removes and returns the element at the specified index (default is the last element).
9. **remove:** Removes the first occurrence of a specified element.
10. **reverse:** Reverses the order of elements in the list.
11. **sort:** Sorts the elements of the list in ascending order.
