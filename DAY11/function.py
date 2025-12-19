def greet():
    print('Hello')


greet()
greet()


# 3. Function with Parameters
def greet1(name):
    print("Hello", name)

greet1("Syed")
greet1("Ali")

# 4. Function with Multiple Parameters

def add(a,b):
    print(a+b)

add(1,2)


#5. Return Statement

def add1(a,b):
    return a+b

result = add1(1,4)
print(result)

# Difference: print vs return

def show():
    print("Hello")

def give():
    return "Hello"

x = show()   # prints Hello, x = None
y = give()   # y = "Hello"