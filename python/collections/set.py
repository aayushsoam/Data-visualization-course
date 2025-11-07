'''#creating a set
n={1, 2, 3, 4, 5}  # Using curly braces to create a set
print("Set n:", n)  

print("Type of n:", type(n))  # Output: <class 'set'>
print("Length of n:", len(n))  # Output: 5

for x in n:
    print("Element in n:", x)  # Iterating through the set
    '''
 
'''#add elements to set
n={1, 2, 3, 4, 5}   
n.add(6)  # Adding an element to the set
print("Set after adding 6:", n)  # Output: {1, 2, 3, 4, 5, 6}
n.add(7)  # Adding another element to the set
print("Set after adding 7:", n)  # Output: {1, 2, 3, 4, 5, 6, 7}
#remove elements from set
n.remove(2)  # Removing an element from the set
print("Set after removing 2:", n)  # Output: {1, 3, 4, 5, 6, 7}

#discard elements from set
n.discard(3)  # Discarding an element from the set (no error if not found)
print(n)  # Output: {1, 4, 5, 6, 7}    


#join two sets
n1={8, 9, 10}
n2={11, 12, 13}
n3=n1.union(n2)  # Joining two sets using union
print("Joined set n3:", n3)  # Output: {8, 9, 10, 11, 12, 13}


n1.update(n2)  # Joining two sets using update
print("Set n1 after update with n2:", n1)  # Output: {  8, 9, 10, 11, 12, 13}




#intersection of two sets
n4={1, 2, 3, 4, 5}
n5={4, 5, 6, 7, 8}
n6=n4.intersection(n5)  # Intersection of two sets
print("Intersection of n4 and n5:", n6)  # Output: {4, 5}'''







#using sets to find intersection of three sets
# This code finds the intersection of three sets created from lists.
# It converts three lists to sets and then finds the common elements among them.
l1=[1, 2, 3, 4, 5]
l2=[4, 5, 6, 7, 8]
l3=[9, 10, 11, 12, 13]
s1=set(l1)  # Converting list to set
s2=set(l2)  # Converting another list to set
s3=set(l3)  # Converting third list to set
#intersection of three sets
s4=s1.intersection(s2)
final=s4.intersection(s3)# Intersection of three sets
print("Intersection of s1, s2, and s3:", s4)  # Output: set() (empty set since no common elements)



