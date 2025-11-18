student = {
    "name": "Syed",
    "age": 25,
    "course": "Python"
}
print(student["name"])
print(student.get("age"))

# 3. Adding & Updating Items
student["city"] = "Chennai"   # Add
student["age"] = 26           # Update



# 4. Removing Items
student.pop("course")   # removes specific key
student.popitem()       # removes last added item
del student["age"]      # delete key
student.clear()         # empty dictionary


print(student)

# 5. Dictionary Methods (Very Important)
#=======================================#
#  Method     # Description             #
#  -----------#-------------------------#
# .keys()     # returns all keys        #
# .values()   # returns all values      #
# .items()    # returns key–value pairs #
# .update()   # updates multiple keys   #
# .get()      # safe value access       #
# ======================================#


student = {
    "name": "Syed",
    "age": 25,
    "course": "Python"
}

print(student.keys())
print(student.values())
print(student.items())


# 6. SETS (set)
nums = {1, 2, 3, 3, 4}
print(nums)   # {1, 2, 3, 4}


# 7. Adding & Removing in Sets

s = {1, 2, 3}
s.add(4)
print(s)
s.remove(2)
print(s)
s.discard(10)  # safe remove (no error)
print(s)


# 8. Set Operations (SUPER IMPORTANT)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a|b)  # Union
print(a&b)  # Intersection (Common items   )
print(a-b)  # Difference (items in a not in b)
print(a^b)  # Symmetric Difference (items in a or b but not both)