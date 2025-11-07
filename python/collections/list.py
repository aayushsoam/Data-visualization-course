fruits=["apple", "banana", "cherry"]
print("List of fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice of fruits:", fruits[1:3]) # fruits[start:end]
fruits.append("orange")
print("After appending orange:", fruits)
fruits.remove("banana")
print("After removing banana:", fruits)
fruits.insert(1, "kiwi")              # Insert kiwi at index 1
print("After inserting kiwi at index 1:", fruits)
fruits.sort()                         # Sort the list in ascending order

print("After sorting:", fruits)
fruits.reverse()
print("After reversing:", fruits)
print("Length of the list:", len(fruits))
print("Index of 'cherry':", fruits.index("cherry"))
print("Count of 'apple':", fruits.count("apple"))
print("Is 'kiwi' in the list?", "kiwi" in fruits)
print("Is 'grape' not in the list?", "grape" not in fruits)
print("List of fruits after all operations:", fruits)
print(len(fruits))