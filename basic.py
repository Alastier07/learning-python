# Variables
# name = "Aries"; print(name)

name = "Aries"
# print(type(name) == str)
print(isinstance(name, str))

# age = 27
age = int("27") #Casting
print(isinstance(age, int))

# Operators
# = assign
# Arithmetic Operators
1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
5 // 2 #2

print("Panda" + " is a good dog.")

age = 8
age += 8
print(age)

# Comparison Operators
# a = 1; b = 2

# a == b #False
# a != b  #True
# a > b #False
# a < b #True
# a <= b #True
# a >= b #False

# Bolean Operators
# condition1 = True
# condition2 = False

# not condition1 #False
# condition1 and condition2 #False
# condition1 or condition2 #True

# Bitwise Operators
# & performs binary AND
# | performs a binary OR
# << shift left operation
# >> shift right operation

# is 
# in

# Ternary Operators
def is_adult(age):
    return True if age > 18 else False

#String Method
print("ABCDF".lower())
print("abcdf".upper())
print("abcdf".capitalize())

word = 'ABCDF'
print(word[0])
print(word[-1])
print(word[1:3])
print(word[:3])

#Boolean
done = True

if done:
    print("Yes")
else:
    print("No")

#any, all

