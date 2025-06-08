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
for i in range(len(li) -1):
     li[i], li[i+1] = li[i+1], li[i]
print(li)
print()

print('10.WAP to merge two list.')
l1 = [1, 3, 7, 9]
l2 = [2, 4, 6, 8]
print(*l1,*l2)
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
#o/p --> ''iH woH rea uoy')
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
l1 = [1,2,3,4]
l2 = [2,4,6,8]
print([l1, l2])  #[[1,2,3,4], [2,4,6,8]]
print((l1, l2))  #([1,2,3,4], [2,4,6,8])

print()
print('27.WAP to remove duplicates from a list without using inbuilt function.')
l = [1,3,5,7,2,4,6,7,3,1]
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
d = {'a': 'apple', 'one': 1, 'b': 'ball', 'three': 3, 'four':4, 'n': 45.7}
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




