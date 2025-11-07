# recursion using factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #recursive call 
user_input = int(input("Enter a number to calculate its factorial: "))
result = factorial(user_input)
print(f"The factorial of {user_input} is: {result}")  # Output: The factorial of <user_input> is: <result>        