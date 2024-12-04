# Create an empty list called my_list
my_list = []
print("Step 1: Empty list:", my_list)

# Append elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Step 2: After appending:", my_list)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print("Step 3: After inserting 15 at index 1:", my_list)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("Step 4: After extending with [50, 60, 70]:", my_list)

# Remove the last element from my_list
my_list.pop()
print("Step 5: After popping the last element:", my_list)

# Sort my_list in ascending order
my_list.sort()
print("Step 6: After sorting:", my_list)

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Step 7: The index of 30 is:", index_of_30)

# Print the final sorted list
print("The final sorted list is:", my_list)
