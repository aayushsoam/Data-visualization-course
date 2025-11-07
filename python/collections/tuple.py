"""#tuple 
colours=("red","green","yellow")


#creating tuple in 1 item using in last , define its a tuple
fruits=("apple",)


print(type(colours))



print(len(colours))
print(colours[0])  # Accessing the first element
print(colours[1])  # Accessing the second element   
print(colours[2])  # Accessing the third element
print(colours[-1])  # Accessing the last element
print(colours[-2])  # Accessing the second last element
print(colours[0:2])  # Slicing from index 0 to 1 (inclusive of 0, exclusive of 2)
print(colours[1:])  # Slicing from index 1 to the end
print(colours[:2])  # Slicing from the start to index 1 (inclusive
print(colours[::2])  # Slicing with a step of 2
print(colours[::-1])  # Reversing the tuple
#second reversing the tuple
print(colours[::-2])  # Reversing the tuple with a step of 2


#concatenating tuples
new_colours = colours + ("blue", "purple")            #using + operator to concatenate
print(new_colours)  # Output: ('red', 'green', 'yellow', 'blue', 'purple')


#unpacking tuples
red, green, yellow = colours  # Unpacking the tuple into variables
print(red)     # Output: red
print(green)   # Output: green
print(yellow)  # Output: yellow"""

n=(1,2,3,4,5)
#concatenating tuples
new_n = n + (6, 7, 8)  # Concatenating tuples
print(new_n)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)
#reversing the tuple
print(n[::-1])  # Output: (5, 4, 3, 2, 1)
#reversing the tuple using reversed function

print(reversed(n))