# Find the Squares from the given List

# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]


lst = [4 ,5, 2, 9] 

print("original list:",lst)

square_lst = list(map(lambda lst: lst ** 2 ,lst))

print("square of the elements of list:")

print(square_lst)