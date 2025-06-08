print("filter the even numbers using filter function")
li = [23, 24, 26, 29, 32, 39, 44]

def even_(num):
    if num % 2 == 0:
        return True
    else:
        return False
filtered_obj = filter(even_, li)
for ele in filtered_obj:
    print(ele)
print("###################################################################")
def even_(num):
    return num % 2 == 0
filtered_obj = filter(even_, li)
print(list(filtered_obj))
print("###################################################################")
filtered_obj = lambda num : num % 2 == 0
print(list(filter(filtered_obj, li)))
print("###################################################################")
print(list(filter(lambda num : num % 2 == 0, li)))
print("###################################################################")
print()

print("number greater than 60")

li = [67, 86, 46, 35, 25, 78, 97]
print(list(filter(lambda num : num >= 60, li)))
print("###################################################################")
print()
print("filter vowel characters")

st = "shantanu"
print(list(filter(lambda ch: ch in 'aeiou', st)))
print("###################################################################")
print("Filter students having marks greater than or equal to 90")
print()
data = {'Nitesh' : 78, 'Rahul' : 98, 'Raj' : 91, 'Amar' : 90, 'Abhi' : 81}
def topper_(student):
    return data[student] >= 90
print(list(filter(topper_, data)))

print("###################################################################")
print()
print(list(filter(lambda student : data[student] >= 90, data)))
print("###################################################################")
print()
print("MAP FUNCTION")
print()
print("print the length of names using map function")

names = ['raj', 'yash', 'yashraj']

def len_name(name):
    return len(name)

mapped_obj = map(len_name, names)
for name in  mapped_obj:
    print(name)
print("###################################################################")
print()
print(list(map(len_name, names)))
print("###################################################################")
print()
print(list(map(lambda name : len(name), names)))
print("###################################################################")
print()
print("print square of numbers using map function")
nums = [5, 3, 8, 11, 6]
print(list(map(lambda num: num ** 2, nums)))

print("###################################################################")
print()
print("add two list of equal index using map function")
num1 = [10, 20, 30]
num2 = [1, 2, 3]

def add_(a, b):
    return a + b

print(list(map(add_, num1, num2)))
print()
print("add two list of unequal index using map function")
print()
num1 = [10, 20, 30, 40]
num2 = [1, 2, 3]

print(list(map(lambda a, b: a + b, num1, num2)))
print()
print("###################################################################")
print()
print("print sum of numbers in a list using reduce function")
import functools
li = [5, 8, 2, 10, 9]
def sum_(a, b):
    return a + b

print(functools.reduce(sum_, li))
print()
print(functools.reduce(lambda a, b: a + b, li))
print()
print("###################################################################")

print("print maximum numbers in a list using reduce function")
print(),
nums = [5, 8, 2, 10, 9]
def greater_(a, b):
    if a > b:
        return a
    else:
        return b
print(functools.reduce(greater_, nums))
print()
print("###################################################################")

print()
