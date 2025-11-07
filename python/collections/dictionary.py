"""dictionary = {
     "name": "John",   # Key-value pair    
     "age": 30,       # Key-value pair
     "city": "New York" # Key-value pair
 }
print(dictionary)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}



n={ 
    
    "name": "Alice",  # Key-value pair
    "age": 25,  # Key-value pair
    "city": "Los Angeles"  # Key-value pair 
}
print("Dictionary n:", n)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}"""


'''n={
    "name": "Bob",  # Key-value pair
    "name1": "Bob",  # Duplicate value for the key "name"
}
print("Dictionary n with duplicate key:", n) ''' # Output: {'name': 'Charlie'}

'''# Accessing values in a dictionary
print( n["name"])  # Output: Bob
print(n["age"])  # Output: 25


#updating values in a dictionary
n["age"] = 26  # Updating the value for the key "age"
print("Updated age:", n["age"])  # Output: 26
# Adding a new key-value pair to the dictionary
n["country"] = "USA"  # Adding a new key-value pair
print("Dictionary after adding country:", n)  # Output: {'name': 'Bob', 'age': 26, 'city': 'Los Angeles', 'country': 'USA'}
# Removing a key-value pair from the dictionary
del n["city"]  # Removing the key "city"
print("Dictionary after removing city:", n)  # Output: {'name': 'Bob', 'age': 26, 'country': 'USA'}
#clearing the dictionary
n.clear()  # Clearing all key-value pairs from the dictionary       '''



"""for x in n:
    print("Key:", x)  # Iterating through the keys of the dictionary
    print("Value:", n[x])  # Accessing the value for each key
    
    
    
# nested dictionary
nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles"
    }
}    

print("Nested Dictionary:", nested_dict)  # Output: {'person1': {'name': 'Alice', 'age': 30, 'city': 'New York'}, 'person2': {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}}
# Accessing values in a nested dictionary
print("Person 1 Name:", nested_dict["person1"]["name"])  # Output: Alice
print("Person 2 Age:", nested_dict["person2"]["age"])  # Output: 25


#sum of values in a dictionary
n={
    "a": 10,
    "b": 20,
    "c": 30
}
sum_values = sum(n.values())  # Summing the values in the dictionary
print("Sum of values in the dictionary:", sum_values)  # Output: 60
# mirror  changed a to z % b to y 

"""


