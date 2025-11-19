# 1. FOR LOOP
for i in range(5):
    print("Iteration:", i)


# 2. Looping through a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)


# 3. Looping through a String
name = 'syed'

for char in name:
    print("Character:", char)


# 4. Looping through a Dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key,value in person.items():
    print(f"{key}: {value}")


# 5. range() Function

# | Example             | Meaning   |
# | -----------------   | --------- |
# | range(5)            | 0 to 4    |
# | range(2, 8)         | 2 to 7    |
# | range(1, 10, 2)     | 1,3,5,7,9 |


# 6. WHILE LOOP

# Used when you don’t know how many times loop will run.

m = 1
while m <= 5:
    print("M Iteration:", m)
    m += 1


# 7. break, continue, pass

for i in range(10):
    if i == 5:
        break
    print('BREAK',i)


for i in range(10):
    if i == 5:
        continue
    print('CONTINUE',i)


for i in range(5):
    pass
# Used as a placeholder for future code.