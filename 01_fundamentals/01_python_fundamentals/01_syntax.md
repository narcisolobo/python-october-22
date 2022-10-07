# Syntax
---
## Indentation and Line-Endings

Unlike what you may have seen in other languages, like JavaScript, *Python has no brackets or braces*. Instead, the most important aspect of Python is indentation to indicate which lines belong to which code blocks.

```py
    x = 10
    if x > 50:
        print("bigger than 50")
    else:
        print("smaller than 50")
```

## Pass

If we start a code block, there must be at least one line of indented code immediately following. If we try to run a file with a hanging code block, we'll get a syntax error. Luckily, Python has provided us with the pass statement for situations where we know we need the block statement, but we aren't sure what to put in it yet.

```py
class EmptyClass:
    pass
```
```py
for val in my_string:
    pass
```

## A Word About Python Conventions

Every programming language has its own naming and style conventions. Python is no different. Readability is one of the hallmarks of Python code, so it's important for us to do our best to adhere to the [PEP 8 Style Guide](https://peps.python.org/pep-0008/).

In short, all variable and function names will be lowercase, with each word separated by an underscore. This is called "snake-case".

```py
my_name = "Narciso"

def add_numbers(num1, num2):
    return num1 + num2
```

Each word in a class name begins with a capital letter, with no underscores between words. This is called "Pascal Case".

```py
class PokemonCard:
    pass
```

[Here's a great page that sums up the important points of PEP 8.](https://realpython.com/python-pep8/)