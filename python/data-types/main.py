# Immutable data types
# - int
# - float
# - bool
# - str
# - tuple
# - frozenset

# IMMUTABLE EXAMPLE
number = 10
print(number)
print(id(number))  # Memory address of object 10

# Reassignment
number = number + 1
print(number)
print(id(number))  # NEW memory address -> new object 11

# Correct explanation:
# 1. A variable stores a REFERENCE (address) to an object in memory.
# 2. Because ints are immutable, Python CANNOT change 10 in-place.
# 3. So Python creates a NEW object 11 and makes 'number' refer to it.
# 4. The old object 10 may still exist if other variables reference it.
#    If nothing references it, garbage collector may free it later.

# Mutable data types
# - list
# - set
# - dict

# MUTABLE EXAMPLE
numbers = [1, 2, 3]
print(numbers)
print(id(numbers))  # Memory address of LIST object

numbers.append(4)   # Modify SAME object in-place
print(numbers)
print(id(numbers))  # SAME address -> same object modified

# Correct explanation:
# 1. Variable stores reference to list object in memory.
# 2. List is mutable -> contents CAN change without new object.
# 3. append() modifies the existing object in-place.
# 4. The object is still accessible through the same variable.