

# **Decorators**  
- A decorator is a function that takes another function (or method) as its argument, adds some kind of functionality to that function, and returns a new function. 
- The new function is often referred to as a "decorated" function.
- You can think of a decorator as a "wrapper" around the original function 
- This is useful for tasks like logging, access control, caching, and input validation.

### **How Decorators Work**
- **Function as First-Class Citizens**: In Python, functions are first-class citizens, meaning you can pass them as arguments, return them from other functions, and assign them to variables.
- **Wrapping Functions**: A decorator is itself a function that takes another function as an argument, adds some functionality to it, and returns a new function.


``` python
def my_decorator(func):
    def wrapper(name):
        print("Something is happening before the function is called.")
        result = func(name)  # Call the original function with an argument
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# behind the scenes, this is equivalent to: greet = my_decorator(greet)

```

### Why Do We Create the `wrapper` Function?

The main reason we create the `wrapper` function is **to modify or extend the behavior** of the original function, while still being able to call the original function itself. This lets us:

1. **Add code before and after** the original function runs (e.g., logging, timing, input validation).
2. **Control how the original function is executed** (e.g., limiting access, retrying on failure).
3. **Preserve the original function’s behavior** (calling the original function as part of the `wrapper`).

The `wrapper` function effectively "wraps" around the original function, allowing us to add this extra functionality while still calling the original.

### Example with `wrapper`

Here’s an example of a decorator with a `wrapper` function that adds behavior before and after calling the original function:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)  # Call the original function
        print("After the function runs")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))
```

**Output**:
```
Before the function runs
After the function runs
Hello, Alice!
```

Here’s what’s happening:
- **`my_decorator(func)`**: This takes the `say_hello` function as an argument.
- **`wrapper(*args, **kwargs)`**: This new `wrapper` function runs code before and after calling `say_hello()`.
- **`func(*args, **kwargs)`**: Calls the original `say_hello` function inside `wrapper` with the same arguments it was passed.
- The decorator returns the `wrapper` function, effectively replacing `say_hello` with `wrapper`.

### What Happens if You Don’t Use a `wrapper`?

If you **don’t create the `wrapper` function**, you won’t have the ability to intercept and modify the behavior of the original function. The decorator would simply return the function without doing anything extra. Here’s what it would look like:

```python
def my_decorator(func):
    return func  # Just returns the original function without modification

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))
```

**Output**:
```
Hello, Alice!
```

In this case:
- The decorator **does nothing** except return the original function. It doesn’t add any behavior before or after the function runs.
- This is essentially a no-op decorator—it doesn’t modify the behavior of `say_hello()`.

### The Purpose of the `wrapper` Function

The `wrapper` function is necessary if you want to:

- **Add additional logic** before or after the function is executed (e.g., logging, validation).
- **Modify the input arguments** before passing them to the original function.
- **Change the result** returned by the original function.
- **Control the flow** (e.g., skip execution in certain cases, or retry).

### Example: No `wrapper` Means No Added Functionality

Here’s another example to demonstrate the difference:

```python
def my_decorator(func):
    print("Decorator is applied")
    return func  # No wrapper here, just returning the original function

@my_decorator
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
```

**Output**:
```
Decorator is applied
Hello, Alice
```

- The only effect is that `my_decorator` runs when the function is decorated. But **there’s no added behavior** before or after calling `greet()`. The function runs exactly as if it were undecorated.

### When Is `wrapper` Not Needed?

You can skip creating a `wrapper` function if:
- You don’t need to **modify the function’s behavior**.
- You simply want the decorator to apply some transformation once, when the decorator is applied, but not every time the function is called.

For instance, if you just want to print something once when the function is defined (and not every time it’s called), you wouldn’t need a `wrapper`.

### Summary

- **`wrapper` is needed**: When you want to **add extra functionality** (before, during, or after) to the original function, such as logging, validation, timing, etc.
- **Without `wrapper`**: If you don’t have a `wrapper`, the decorator won’t modify the behavior of the function—it’ll just return the original function as-is.

By using the `wrapper`, you are able to customize how the function behaves **every time it is called**. If you still have any confusion or would like more examples, feel free to ask!


----

### What are `*args`?

- `*args` allows a function to accept **any number of positional arguments** (arguments passed without explicitly naming them).
- It packs all the extra positional arguments into a **tuple**.

#### Example of `*args`:
```python
def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")
```

**Output**:
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

### What are `**kwargs`?

- `**kwargs` allows a function to accept **any number of keyword arguments** (arguments passed with a key=value pair).
- It packs all the extra keyword arguments into a **dictionary**.

#### Example of `**kwargs`:
```python
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce(name="Alice", age=25, city="New York")
```

**Output**:
```
name: Alice
age: 25
city: New York
```

### Using `*args` and `**kwargs` Together

You can use both `*args` and `**kwargs` in the same function to accept any combination of positional and keyword arguments.

#### Example with `*args` and `**kwargs`:
```python
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function(1, 2, 3, name="Alice", age=25)
```

**Output**:
```
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 25}
```

- `*args` captures `(1, 2, 3)` as a tuple.
- `**kwargs` captures `{'name': 'Alice', 'age': 25}` as a dictionary.

### Why Use `*args` and `**kwargs`?

1. **Flexibility**: These constructs make your functions more flexible because they can accept any number of arguments. This is especially useful when you don’t know in advance how many arguments will be passed.

2. **Handling Optional Arguments**: You can use `*args` and `**kwargs` to define optional parameters, allowing users to provide extra arguments as needed.

3. **Passing Arguments to Other Functions**: They are also useful when you want to pass arguments from one function to another without explicitly defining all the parameters.

#### Example: Passing `*args` and `**kwargs` to another function
```python
def display_info(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

def call_display():
    names = ["Alice", "Bob"]
    info = {"age": 30, "city": "New York"}
    display_info(*names, **info)  # Unpacking arguments

call_display()
```

**Output**:
```
Positional: ('Alice', 'Bob')
Keyword: {'age': 30, 'city': 'New York'}
```

### When to Use `*args` and `**kwargs`?

- **When you want a function to handle an arbitrary number of arguments**: Functions like `print()` and `sum()` are good examples that use `*args`.
- **When you need flexibility in handling optional or additional arguments**: You might use `**kwargs` when you want to support options without making them mandatory.

### Summary

- `*args`: Used to capture **any number of positional arguments** passed to a function, stored as a tuple.
- `**kwargs`: Used to capture **any number of keyword arguments** passed to a function, stored as a dictionary.
- They provide flexibility to functions and allow passing variable-length arguments without explicitly defining them in the function signature.
