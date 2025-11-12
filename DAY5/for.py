for i in range(5):
    print('Hello')

for i in range(10):
    print(i)

for i in range(1,10):
    print('1,10',i)

# range(start, stop, step)
for i in range(1,10,2):
    print(i)



fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# break and continue
for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)



for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
