################################################################################
"""
Recommended readings: 
  Chapter on lists: https://automatetheboringstuff.com/3e/chapter6.html 
  List comprehension: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
"""
################################################################################

"""
Exercise 3.1

Task:
------
Write code that prints the sum of the elements in the following list.
[1, 4, -6, 7, 2, 3, 9, 11, 6]
"""

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6] # In all exercises in this script, you will work with this list

print("Exercise 3.1")

print(sum(lst))

print("---")

"""
Exercise 3.2

Task:
------
Print the product of the elements in the list.
"""

print("Exercise 3.2")

product = 1
for i in lst:
  product *= i 
print(product)

print("---")

"""
Exercise 3.3

Task:
------
Print the sum of the squares of the list.
"""

print("Exercise 3.3")

sum_squares_lst = sum([i**2 for i in lst])
print(sum_squares_lst)

print("---")

"""
Exercise 3.4

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.4")

pass
print(max(lst))
print("---")

"""
Exercise 3.5

Task:
------
Print the largest element of the list.
"""
# Seem like exercise 3.5 the same as exercise 3.4. I try to use a different method to resolve this question. 
print("Exercise 3.5")

pass
lst_2 = lst.copy()
lst_2.sort()
largest_num = lst_2[-1]
print(largest_num)

print("---")