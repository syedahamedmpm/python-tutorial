# Create a simple multiplication table.
number = int(input('Enter number = '))
for i in range(1,11):
    print(f'{i} * {number} = {i*number}')