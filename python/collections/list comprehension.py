'''#normal method
marks=[10, 20, 30, 40, 50]
new_marks = []
for mark in marks:
    new_marks.append(mark + 5)
print(new_marks)    




#list comprehension
marks = [10, 20, 30, 40, 50]
new_marks = [mark + 5 for mark in marks]
print(new_marks)'''




marks = [11, 21, 31, 41, 51]
new_marks = [mark for mark in marks if mark in [100] ]
print(new_marks)
print(type(new_marks))
# check elements in present in list
marks = [11, 21, 31, 41, 51]
new_marks = [mark for mark in marks if mark in [11, 21, 31]]
print(new_marks)