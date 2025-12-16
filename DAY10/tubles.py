# What is a Tuple?

# A tuple is like a list, but cannot be changed.

# ✔ ordered
# ✔ immutable (cannot change)
# ✔ faster than lists

colors = ("red", "green", "blue")
print('Colors',colors)


# 2. Accessing Tuple Items
print(colors[0])
print(colors[1])
print(colors[2])


print(colors[-1])
print(colors[-2])
print(colors[-3])
# print(colors[-4])


# 3. Tuple Unpacking

person = ("Syed", 25, "Chennai")
name,age,city = person

print(name)
print(age)
print(city)


# 4. Tuple Methods

# Tuples have only two methods:

nums = (1, 2, 2, 3)

print(nums.count(2))   # 2
print(nums.count(1))   # 1
print(nums.count(3))   # 1
print(nums.index(3))   # 3
print(nums.index(2))   # 1

# 5. Tuple vs List

# | List    | Tuple     |
# | ------- | --------- |
# | Mutable | Immutable |
# | Slower  | Faster    |
# | Uses [] | Uses ()   |
