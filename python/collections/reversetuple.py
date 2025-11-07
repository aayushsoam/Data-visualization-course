'''input_n=(1,2,3,4,5)
list=[]  # Convert tuple to list
for x in reversed(input_n):
    list.append(x)  # Append each element to the list
output_n=tuple(list)  # Convert list back to tuple    type casting method
print(output_n)  # Output: (5, 4, 3, 2, 1)'''


#list to tuple conversion 
n=[1, 2, 3, 4, 5]
output_n=tuple(n)  # Using reversed function to reverse the list and convert to tuple
print(type(output_n))  # Output: (5, 4, 3, 2, 1)