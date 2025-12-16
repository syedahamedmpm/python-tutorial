# . What is a String?

# A string is text data.

text = "Python"

print("text",text)
print("text[0]",text[0])
print("text[-1]",text[-1])
print("text[0:2]",text[0:2])
print("text[:3]",text[:3])
print("text[3:]",text[3:])


# 8. Important String Methods

msg = "hello python"

print('UPPER',msg.upper())
print('Lower',msg.lower())
print('STRIP',msg.strip())
print('REPLACE',msg.replace("python", "world"))
print('Split',msg.split())

print('STR LENGTH',len(msg))


# 10. Check String Content
text = "Python123"

print('isalpha',text.isalpha())   # False
print('isdigit',text.isdigit())   # False
print('isalnum',text.isalnum())   # True


name = "Syed"
age = 25

print(f"My name is {name} and I am {age} years old")