"""
fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits:
  print(x)
  #we can as well print the only list upto banana
fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits:
  print(x)
  if x == "banana":
    break
"""
#we can print the list before banana
"""
fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  """
  # we can as well print the list before banana, jump and print the list after banana
"""
  fruits = ["apple", "banana", "cherry", "mango"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  """
 #We can print the list after banana.
#1. We can use the flag after 
fruits = ["apple", "banana", "cherry", "mango"]
print_after = False  # Flag to track our position

for x in fruits:
    if print_after:
        print(x)
    
    # Once we hit banana, set the flag to True for the *next* iterations
    if x == "banana":
        print_after = True
  