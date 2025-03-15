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

#complex numbers
num1 = 2+3j
num2 = complex(2, 3)

print(num2.real, num2.imag)

print(abs(-5.5)) #5.5
print(round(5.6)) #6
print(round(5.59, 1)) #5.6

#Enums

from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)
print(State.INACTIVE.value)
# print(list(State))
# print(len(State))

#Input
# age = input("What is your age? ")
# print(f"Your age is {age}")

#Control Statements
condition = True

if condition:
    print("The condition")
    print("was true")
# elif <condition>:
else:
    print("The condition was false")

# List
dogs = [] #Empty List
dogs = ["Roger", 1, "Syd", True]

# print("Roger" in dogs) #True
# print(dogs[2]) "Syd"
dogs[2] = "Beau"

# print(dogs[-1]) #True
# print(dogs[2:4]) #Beau, True
# print(dogs[:3]) #Roger, 1, Beau
# print(dogs[2:]) #Beau, True
# print(len(dogs)) #4
# dogs.append("Lucky") #add Lucky on list
# dogs.extend(["Lucky", 7]) #add list on dogs
# dogs += "[Panda, 8]" #same as extend
# dogs.remove("Beau")
# print(dogs.pop()) #get the last item of the list and remove
# dogs.insert(2, "Pogi")
# dogs[1:1] = ["Test1", "Test2"]
print(dogs)

items = ["Roger", "Panda", "Lylia", "Lucky", "pogi"]
# itemscopy = items[:]

#Sorting
# items.sort(key=str.lower)
print(sorted(items, key=str.lower))
print(items)
# print(itemscopy)

#Tuples
