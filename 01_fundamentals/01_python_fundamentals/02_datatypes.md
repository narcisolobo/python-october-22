# Python Data Types
---
## What is a Data Type?

Understanding the concept of variables is one of the first big hurdles we must overcome as programmers. Variables are dynamic—their values can *vary*.

All variables can be classified as some type of data. A data type is a classification that specifies which type of value a variable has.

There are two families of data types in Python, primitive and composite.

## Primitive Types
Primitive types are the most basic data structures. They are the building block for data manipulation. They contain pure, simple values of data.

- Strings - a sequence of characters: 
  
  ```py
  message = "Hello World!"
  file_name = "dancing_banana.gif"
  empty_string = ""
  ```
- Integers - whole numbers:
  ```py
  answer = 42
  negative_number = -23
  ```
- Floats - decimal numbers:
  ```py
  negative_float = -.01
  pi = 3.1459
  ```
- Booleans - true or false:
  ```py
  has_swag = True
  is_snowing = False
  ```

## Composite or Collection Types

Composite or collection types can hold more than one value. The two most important ones for us are lists and dictionaries.

- Lists - We called these "arrays" in Javascript. You can recognize lists by their square brackets. Each value in an array is separated by a comma.

    ```py
    mish_mash = [6, True, -90.5, 24, "banana"]
    ```

    Just like arrays in Javascript, each element in a list has an index, and the first index is always 0.

- Dictionaries - We called these "objects" in Javascript. You can recognize dicionaries by their curly braces. They are made up of key-value pairs separated by commas.

    ```py
    ezra = {
        "name": "Ezra Bridger",
        "is_jedi": True,
        "species": "human",
        "height": 1.65,
        "mass": 50
    }
    ```
