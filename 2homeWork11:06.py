list_1 = [1, 2, 3, 4, 5, 6,7]
list_2 = [0, 9, 8, 7, 6, 5]
list_3 = list_1 + list_2
print("First:", list_1)
print("Second:", list_2)
print("Thrid:", list_3)

# Task3 creating a third list without repeating elements
list_3_1 = sorted(list(set(list_1 + list_2)))
print("third1", list_3_1)

# Task4 creating a third list with common elements
list_3_2 = sorted(list(set(list_1) & set(list_2)))
print("Third2:", list_3_2)

# Task5 creating a third list only with unique elements
list_3_3 = sorted(list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1)))
print("Third3:", list_3_3)

#Task6 creating third list with max and min value of lists
list_3_4 = []
list_3_4.append(min((list_1), list_2)) 
list_3_4.append(max((list_1), list_2))
print("Third4:", list_3_4)

#""""""""""""""RESULT""""""""""""""""""""""""""""
#First: [1, 2, 3, 4, 5, 6, 7]
#Second: [0, 9, 8, 7, 6, 5]
#Thrid: [1, 2, 3, 4, 5, 6, 7, 0, 9, 8, 7, 6, 5]
#third1 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#Third2: [5, 6, 7]
#Third3: [0, 1, 2, 3, 4, 8, 9]
#Third4: [[0, 9, 8, 7, 6, 5], [1, 2, 3, 4, 5, 6, 7]]