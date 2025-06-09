import re

print("1.WAP to find the length of the string without using inbuilt funct.")
st = "python world"
count = 0
for _ in st:
    count += 1
print(count)

print(len(st))
print()
print("2.WAP to reverse a string without using inbuilt function")
st = "reverse a string"
rev = ""
for char in st:
    rev = char + rev
print(rev)

rev = st[::-1]
print(rev)
print()
print("3.WAP to replace one string with another")
st = "Hello world!!"
out = st.replace("world", "universe")
print(out)

print()
print("4.WAP to convert string into list and vice versa")
st = "convert string into list and vice versa"
li = st.split()
print(li)
string1 = " ".join(li)
print(string1)
print()

print("5.WAP to convert 'hello welcome to python' to comma separated string.")
st = 'hello welcome to python'
li = st.split()
new_value = ",".join(li)
print(new_value)

for char in st:
    print(char, end=",")

print()

print(".WAP to print alternate characters from a given string")
st = 'PROGRAMMING'
for char in range(0, len(st), 2):
    print(st[char], end=" ")
print()
print(" ".join(([st[char] for char in range(0, len(st), 2)])))
print()

print('7.WAP to print ascii values of string')
st = "pythonPYTHON"
for char in st:
    print(f"ascii value of {char} is {ord(char)}")
print()

print('8.WAF to convert upper case into lower case and vice versa.')
st = "python JAVA"
upper = ''
lower = ''
for char in st:
    if 'a' <= char <= 'z':
        upper += chr(ord(char) - 32)
    else:
        lower += chr(ord(char) + 32)
print(upper)
print(lower)
print()

print('9.WAP to swap 2 numbers without using third variable')
a = 10
b = 20
a, b = b, a
print(a, b)
print()
li = [10, 20]
for i in range(len(li) - 1):
    li[i], li[i + 1] = li[i + 1], li[i]
print(li)
print()

print('10.WAP to merge two list.')
l1 = [1, 3, 7, 9]
l2 = [2, 4, 6, 8]
print(*l1, *l2)
print(l1 + l2)

print(out)
l3 = []
for i in zip(l1, l2):
    l3.append(i)
print(l3)

print()
print('14.WAP to check given string is Palindrome.')
st = 'malayalam'
if st[::-1]:
    print(f'{st} is pallindrome')
else:
    print(f'{st} is not pallindrome')

print()
print('15.WAP to search for the character in a string and return the corresponding index')
st = "hello world"
char = 'w'
for index, ele in enumerate(st):
    if ele == char:
        print(f'the corresponding index of given character {char} is {index}')

print()

print('16.WAP to get below o/p')
sentence = 'hello world welcome to python programming hi there'
'''{'h':['hello', 'hai'], 'w':['world', 'welcome']......}'''
di = {}
for word in sentence.split():
    if word[0] not in di:
        di[word[0]] = [word]
    else:
        di[word[0]] += [word]
print(di)

print()
print('17 WAP to replace all the characters with "-" if the characters occurs more than once in a string.')
s = 'hellohai'
for char in s:
    if s.count(char) > 1:
        s = s.replace(char, '_')
print(s)

print()

print('18. WADF that returns only +ve values of subtraction')


def outer(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return abs(res)

    return inner


@outer
def sub_(a, b):
    return a - b


print(sub_(10, 15))

print()
print('20. WAF which takes list of strings and int , float, if it is of string print it as it is else reverse it.')
li = [34, 'hello', 'apple', 56.7, 4546, 67.8, 'google', 45]


def define_functionality(lst, res=[]):
    for item in lst:
        if isinstance(item, str):
            res.append(item)
        elif isinstance(item, int):
            res += [int(str(item)[::-1])]
        elif isinstance(item, float):
            res += [float(str(item)[::-1])]
    return res


out = define_functionality(li)
print(out)

print()
print('21. WA class called simple and it should have iteration capability')


class simple:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, dx, dy):
        return self.a + dx, self.b + dy

    def sub(self, dx, dy):
        return self.a - dx, self.b - dy


s = simple(10, 20)
print(s.add(5, 5))
print(s.sub(6, 6))

print('22. Write a custom class which can access values of dict using d[a] and d.a')


class access_dict:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, key):
        return self.__dict__[key]


d = access_dict('Akshaye', 32)
print(d.name)
print(d['age'])

print()
print('23. WAP to get below o/p# s = "Hi How are you"')
# #o/p --> 'uoy era woH iH')
s = 'Hi How are you'
rev = ''
for char in s:
    rev = char + rev
print(rev)

print(" ".join(s.split().__reversed__()))

print()
print('24. WAP to get below o/p# s = "Hi How are you"')
# o/p --> ''iH woH rea uoy')
st = "Hi How are you"
rev = ''
for char in st.split():
    rev += char[::-1] + ' '
print(rev)

print()
print('25. WALE to add 2 numbers.(a,b)')
add = lambda a, b: a + b
print(add(2, 5))

print()
print('26.What is o/p of the following')
l1 = [1, 2, 3, 4]
l2 = [2, 4, 6, 8]
print([l1, l2])  # [[1,2,3,4], [2,4,6,8]]
print((l1, l2))  # ([1,2,3,4], [2,4,6,8])

print()
print('27.WAP to remove duplicates from a list without using inbuilt function.')
l = [1, 3, 5, 7, 2, 4, 6, 7, 3, 1]
non_duplicate = []
duplicate = []
for item in l:
    if item not in non_duplicate:
        non_duplicate.append(item)
    else:
        duplicate.append(item)
print(non_duplicate)
print(duplicate)

print()
print('28. WAP to find longest word in sentence.')
s = 'Life is full of surprises and miracles'
longest_word = ''
max_length = 0
for word in s.split():
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word
print(longest_word)

print()
print('29.WAP to reverse the values in the dictionary  if value is of string type.')
d = {'a': 'apple', 'one': 1, 'b': 'ball', 'three': 3, 'four': 4, 'n': 45.7}
di = {}
for key, value in d.items():
    if isinstance(value, str):
        di[key] = value[::-1]
    else:
        di[key] = value
print(di)

print()
print('30.WAP to get 1234')
t = ('1', '2', '3', '4')
res = ''
for item in t:
    res += item
print(res, end="")

print()
print('31.How to get elements that are present in list b but not in list a.')
a = ['hello', 'hai', 'world']
b = ['hello', 'hai', 'world', 'python']

for item in b:
    if item not in a:
        print(item)

print()
print(
    '32.A function takes variable number of positional arguments as input.how to check if the arguments are more the 5.')


def func(*args, **kwargs):
    if len(args) > 5:
        print("the length of an argument is more than 5")
    else:
        print("length of argument is less than 5")


func(1, 2, 3, 4, 5, 6)

print()
print('34.WAF to reverse any iterable without using reverse function.')


def reverse_(iterable):
    rev = ''
    for char in iterable:
        rev = char + rev
    return rev


out = reverse_("python")
print(out)
print()


def reverse_iterable(*args):
    for item in args:
        if isinstance(item, (str, list, tuple)):
            return item[::-1]


print(reverse_iterable("hello"))
print(reverse_iterable([10, 20, "hi", "hello"]))
print(reverse_iterable(('python', 'java', 100, 200)))

print()
print('35.WAF to get the below o/p')


# #func('TRACXN', 0) ---> RCN
# #func('TRACXN', 1) ---> TAX')
def func(string, i):
    if i == 0:
        print(string[1::2])
    else:
        print(string[0::2])

func('TRACXN', 1)
func('TRACXN', 0)

print()
print('36. WAP to sum all the numbers in below string.')
s = 'Sony12India567pvt21ltd'
su = 0
for item in s:
    if item.isdigit():
        su += int(item)
print(su)
print()
print()

print('37. Sum of numbers')
s = 'Sony12India567pvt21ltd'
# #12+21+567 = 600
from re import findall
res = findall('[0-9]+', s)
sum = 0
for item in res:
    if item.isdigit():
        sum += int(item)
print(sum)
print()

print('#38.WAP to print all the numbers in below list.')
l = ['hello', '123', 'hai', 'python', '345']
li = []
for item in l:
    if item.isdigit():
        li.append(int(item))

print(li)
print()
out = "".join(l)
res = findall('[0-9]+', out)
print(res)

print()

print('39.WAP to print number of occurance of a char in a given string without using inbuilt func')
s = 'hiihellowordhellowar'

di = {}
for char in s:
    if char not in di:
        di[char] = 1
    else:
        di[char] += 1

print(di)

print()

print('40.WAP to print repeated char and count the same')
s = 'helloworld'
di = {}
for char in s:
    if s.count(char) > 1:
        di[char] = s.count(char)
print(di)

print()

print('41.WAP to get alternate char of a string in list.')
st = 'helloworld'
li = []
for char in st[::2]:
    li.append(char)
print(li)

print()
print('42.WAP to get squares of number using lambda')
l = [1,3,5,7]
res = lambda l: l ** 2
print(list(map(res, l)))

print()
print('43.WAF that accepts two strings and returns True if strings are anagrams of each other.')
def anagram(string1, string2):
    s1, s2 = sorted(string1), sorted(string2)
    return s1 == s2

print(anagram('tea', 'ate'))
print(anagram('fare', 'fear'))

print()
print('44.WAP to iterate through list and build a new list that contains only even length elements')
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'amazon']
li = []
for name in names:
    if len(name) % 2 == 0:
        li.append(name)
print(li)

print()
print('45.WAP to create a dictionary of even length words.')
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'amazon']
di = {}
for name in names:
    if len(name) % 2 == 0:
        di[name] = len(name)
print(di)

print()

print('46.WAP to square the numbers in a list')
l = [1,3,5,7]
square = lambda l: l**2
print(list(map(square, l)))

print()

print('49. WAP to print sum of internal and external list')
l = [[1,2,3], [4,5,6], [7,8,9]]
external_sum = 0
for i in l:
    sum_internal = 0
    for j in i:
        sum_internal += j
    external_sum += sum_internal
print(external_sum)

print()

print('50.WAP to reverse list as below')
s = ['hello', 'hai', 'python']
rev = []
for word in s:
    rev = [word] + rev
print(rev)

print()
print('51.WAP to update the tuple')
t1 = (1,3,5,7)
t2 = (2,4,6,8)
print((*t1, *t2))
print(t1 + t2)

