# A list is a collection of items stored in a single variable.
fruits = ["apple", "banana", "cherry"]
print(fruits)

print(fruits[0])  # apple
print(fruits[2])  # cherry
print(fruits[-1])  # cherry

# Lists can be modified.
fruits[1] = "mango"
print(fruits)


# Adding Items
fruits.append("orange")  # Add at end
print(fruits)


fruits.insert(1, "grape")  # Add at specific position
print(fruits)


# Removing Items


fruits.remove("apple")  # Remove by value
print(fruits)

fruits.pop()  # Removes last item
print(fruits)

del fruits[0]  # Removes item by index
print(fruits)

fruits.clear()  # Empties the list
print(fruits)


fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)


# List Slicing 

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[3:])    # [40, 50, 60]
