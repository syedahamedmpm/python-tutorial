# 1.Print numbers 1 to 10 using a for loop.
for i in range(1,11):
    print('1==>i==>',i)


# Print all even numbers between 1 and 20.

for i in range(1,21):
    if i%2==0:
        print('2==>Even Number==>',i)


# Using while loop, print 5 to 1 (reverse).

n = 5
while n>=1:
    print('REVERSE 5 to 1==>',n)
    n-=1


# Print each name in the list using a for loop.
    names = ["Apple", "BALL", "CAT", "DOG"]
    for name in names:
        print('Name==>',name)


# Use break to stop loop when number becomes 7.
for i in range(1,11):
    if i == 7:
        break
    print('BREAK at 7==>',i)