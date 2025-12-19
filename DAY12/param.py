# 1. Default Parameters

# If no value is passed, Python uses a default.



from re import sub


def greet(name="guest"):
    print(f"Hello Mr.{name}")
greet()
greet('Hameed')


# 2. Keyword Arguments

# You can pass arguments by name.
# Order doesn’t matter here.


def info(age,name):
    print(f"Name is {name} Age is {age}")


info(name="Hameed",age=25)

# 3. *args (Multiple Positional Arguments)
def add_number(*numbers):
    total=0
    for i in numbers:
        total+=i
    print(f"Current Total is {total}")
    


add_number(1,2,3,4)

# 4. **kwargs (Multiple Keyword Arguments)

# Accepts unlimited key–value pairs.
def student_info(**info):
    print(info)


student_info(name="Hameed",age=11,class_name="6th")



# 5. Using *args and **kwargs Together

def demo(*nums,**data):
    print(nums)
    print(data )


demo(1,2,3,name="Hameed",age=11 ,class_name="6th")




# 6. Returning Multiple Values

# Python returns them as a tuple.


def calculate(a,b):
    return a+b,a-b,a*b,a/b


result = calculate(3,2)
print(result)
addition,subtraction,multiplication,division=result
print(addition)
print(subtraction)
print(multiplication)
print(division)


# 7. Variable Scope (Simple)
# Local Variable

def test():
    x = 10  # Local variable
    print(x)

test()


# globalscope
y=400
def demo():
    print(x)
    print(y)

demo()