# Variable wired use cases


```python
print(name*3) 
print(name+3) # TypeError: can only concatenate str (not "int") to str

```

- in first cases : If the operand is a string, the * operator repeats the string by the specified number of times. 

- in second cases : If one operand is a string and the other is a numeric type (int or float), Python will raise a TypeError. In this case, you are trying to concatenate a string with a numeric value without converting the numeric value to a string explicitly.

`python dosen't perfom type coersion like javascript`