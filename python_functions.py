def get_name():
    name = input("Enter a name: ")

    print(f"The name you entered: {name}.")


def greeting():
    name = input("Please enter your name: ")
    print("Hello {}!".format(name))


def add(num1, num2):
    print("{} + {} = {}".format(num1, num2, num1+num2))


def subract(num1, num2):
    print("{} - {} = {}".format(num1, num2, num1-num2))

def multiply(num1, num2):
    print("{} * {} = {}".format(num1, num2, num1*num2))

def divide(num1, num2):
    if(num2 == 0):
        print("You cannot divide by zero")
    else:
        print("{} / {} = {}".format(num1, num2, num1/num2))


greeting()

add(1, 2)
subract(1, 2)
multiply(1, 2)
divide(1, 0)

# Create a calculator to add, subtract, divide, multiply
# display appropriate messages with the computation values as to what the outcome is from each funtion
# create a greeting function by taking user input as the user name and display it with the greeting message
