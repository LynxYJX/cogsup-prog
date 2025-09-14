################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")

pass
print(sum(dct.values()))
print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""

print("Exercise 4.2")

max_value_key = max(dct, key = dct.get)
print(max_value_key)

pass

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""

print("Exercise 4.3")

pass
squared_dct = {key: value**2 for key, value in dct.items()}
print(squared_dct)

print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""

print("Exercise 4.4")

pass
for key, value in dct.items():
  if value % 2 == 0:
    print(key)
print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""

print("Exercise 4.5")
dct_swap = {value: key for key, value in dct.items()}
print(dct_swap)
pass

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'

print("Exercise 4.6")
counter_s = {}
for letter in s:
  counter_s[letter] = counter_s.get(letter, 0) + 1
print(counter_s)
pass

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")

fullname = [responses_mapping[x] for x in responses]
print(fullname)
pass

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")

pass
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged_d = {**d1, **d2}
print(merged_d)
print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""

print("Exercise 4.9")

pass
d1_animals = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
d_sorted = {animals: d1_animals[animals] for animals in sorted(d1_animals)}
print(d_sorted)
print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")

pass
d_sorted_num = {animals: number for animals, number in sorted(d1_animals.items(), key = lambda item: item[1])}
print(d_sorted_num)
print("---")