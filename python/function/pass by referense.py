# pass by reference
def change_list(lst):
    lst.append(4)
    print("Inside function:", lst)

my_list = [1, 2, 3]
change_list(my_list)
print("Outside function:", my_list)
# Output: Inside function: [1, 2, 3, 4]
# Output: Outside function: [1, 2, 3, 4]
 