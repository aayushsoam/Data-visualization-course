# write a function that print hello world
'''def print_hello_world():
    """Prints 'Hello, World!' to the console."""
    print("Hello, World!")
print_hello_world()'''    



# write a function add two numbers
'''def add_two_numbers(a, b):
    
    print("n1:", a)
    print("n2:", b)
    sum = a + b
    return sum
    
print(add_two_numbers(5, 10))'''  # Output: 15


# keyword arguments
'''def add_numbers_with_keyword_args(n1, n2):
    """Adds two numbers using keyword arguments."""
    print("n1:", n1)
    print("n2:", n2)
    return n1 + n2
print(add_numbers_with_keyword_args(n1=5, n2=10))'''  # Output: 15   # key is a (n1, n2) and value is a (5, 10)


# function with default arguments
def add_numbers_with_default_args(n1=0, n2=0):
    """Adds two numbers with default arguments."""
    print("n1:", n1)
    print("n2:", n2)
    return n1 + n2  
print(add_numbers_with_default_args(5, 10))  # Output: 15

# POSITIONAL ARGUMENTS
'''def add_numbers_with_positional_args(n1, n2):
    """Adds two numbers with positional arguments."""
    print("n1:", n1)
    print("n2:", n2)
    return n1 + n2
print(add_numbers_with_positional_args(5, 10))'''  # Output: 15


# arbitrary number of arguments
'''def add_numbers(*args):
    """Adds an arbitrary number of numbers."""
    print("Numbers:", args)
    return sum(args)
print(add_numbers(1, 2, 3, 4, 5,10))'''  # Output: 15


# function with arbitrary keyword arguments
'''def add_numbers_with_kwargs(**kwargs):
    """Adds numbers using arbitrary keyword arguments."""
    print("Keyword arguments:", kwargs)
    return sum(kwargs.values())
print(add_numbers_with_kwargs(n1=5, n2=10, n3=15))'''  # Output: 30


def studentinfo(**kwargs):
    for x ,y in kwargs.items():
        print(x, ":", y)
print(studentinfo(name="John", age=25, city="New York"))  # Output: John : 25, age : 25, city : New York
print(studentinfo(name="John", age=25, city="New York", country="USA"))  # Output: John : 25, age : 25, city : New York, country : USA        