# OOP and Functions
One important guideline for programming is DRY - **D**on't **R**epeat **Y**ourself. That means that we don't want a load of repeated bit of code all over the place that essentially does the same thing. One method of avoiding repeating code is using loops. This works fine for things like lists when you want to work on all the items at one time. But what if you have a piece of code that runs at the beginning of the programme that you want to run later...

```python
name_1 = input("Enter a name: ")

print(f"The name you entered: {name_1}.")

# ... many lines of code later

name_7 = input("Enter a name: ")

print(f"The name you entered: {name_7}.")
```
In this example code, the programmer has essentially written the same lines of code seven times! With funtions, we only need to write it once, then *call* the function whenever we need it.

## Functions
The previous example can be turned into a function like so:
```python
def get_name():
    name = input("Enter a name: ")
    print(f"The name you entered: {name}.")

get_name() # this is how you call a function - the code inside the function definition will be run
```
This drastically reduces the amout of code one needs to write.

### Parameters and Arguments
When you define a function, *parameters* are the variables for a given function.
When a function is called, they can take *arguments*. These are values that become variables for the function.  

```python
# this variable, name, is called a parameter when you declare the function
def say_hello(name):
    print(f"Hello {name}")

say_hello("Katalyst") # The string "Katalyst" is an argument
# This value will be held by name and be printed by the function
```

Functions can have more than one parameter
```python
# use commas to separate 
def add(num1, num2):
    print(num1 + num2)

add(3, 5)
```

### ``return``
You can use the ``return`` statement to send a value to a variable.  
One something is returned, the function ends. Nothing runs after ``return`` in a function.