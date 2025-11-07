# pass by value
def addone(x):
    """Adds one to the input value."""
    x += 1
    print("Inside addone function, x:", x)
    
x = 5
addone(x)
print("Outside addone function, x:", x)  # x remains unchanged, demonstrating pass
    
    