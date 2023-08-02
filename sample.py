#
# class Employee:
#     eid = int()
#     name = str()
#     age = int()
#     office_address = str()
#     office_name = str()
#
#     def __init__(self, eid, name, age, office_address, office_name):
#         self.eid = eid
#         self.name = name
#         self.age = age
#         self.office_address = office_address
#         self.office_name = office_name
#
#     def displayemployee(self):
#         print("employee id:", self.eid)
#         print("employee name : ", self.name)
#         print("employee age :", self.age)
#         print("employee office address :", self.office_address)
#         print("employee office name :", self.office_name)
#
#     @classmethod
#     def changeoffice_address(cls, office_address):
#         cls.office_address = office_address
#
#     @staticmethod
#     def pattern():
#         print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#
#
# Employee.office_address = 'Hebbal'
# Employee1 = Employee(12, 'akki', 28, 'bangalore', 'oracle')
# Employee1.displayemployee()
#
# Employee2 = Employee(13, 'abhi', 30, 'mumbai', 'TCS')
# Employee2.displayemployee()
#
# Employee.changeoffice_address('kolkata')
# Employee1.displayemployee()
# Employee2.displayemployee()


#SINGLE LEVEL
# class A:
#     a = 10
#     def displayA(self):
#         print("parent")
#
# class B(A):
#     b = 45
#     def displayB(self):
#         self.displayA()
#         print("child")
#
# b = B()
# b.displayB()
# parent
# child

#b.displayA()
#parent



#MULTI LEVEL
# class A:
#     a = 10
#     def displayA(self):
#         print("A class")
#
# class B(A):
#     b = 20
#     def displayB(self):
#         self.displayA()
#         print("B class")
#
# class C(B):
#     c = 30
#     def displayC(self):
#         self.displayB()
#         print("C class")
#
# c = C()
# c.displayC()

# A class
# B class
# C class


#MULTIPLE (MULTI PARENT TO SINGLE CHILD)
# class A:
#     a = 10
#     def displayA(self):
#         print("A class")
#
# class B(A):
#     b = 20
#     def displayB(self):
#         print("B class")
#
# class C(B, A):
#     c = 30
#     def displayC(self):
#         self.displayA()
#         self.displayB()
#         print("C class")
#
# c = C()
# c.displayC()

# A class
# B class
# C class


#HIERARICHAL(SINGLE PARENT TO MULTI CHILD)
# class A:
#     a = 10
#     def displayA(self):
#         print("A class")
#
# class B(A):
#     b = 20
#     def displayB(self):
#         self.displayA()
#         print("B class")
#
# class C(A):
#     c = 30
#     def displayC(self):
#         self.displayA()
#         print("C class")
#
# class D(A):
#     d = 40
#     def displayD(self):
#         self.displayA()
#         print("D class")
#
# b = B()
# b.displayB()
#
# c = C()
# c.displayC()
#
# d = D()
# d.displayD()
#
# # A class
# # B class
# # A class
# # C class
# # A class
# # D class


#POLYMORPHISM
# class IDLE:
#     def execute(self):
#         print("idle editor")
#
#
# class PYCHARM:
#     def execute(self):
#         print("pycharm editor")
#
# class VSCODE:
#     def execute(self):
#         print("vscode editor")
#
# def run(software):
#     software.execute()
#
#
# idle = IDLE()
# pycharm = PYCHARM()
# vscode = VSCODE()
#
# run(idle)       #idle editor


# a = 45
# b = 0
#
# try :
#     c = a/b
#     print(c)
#
# except ZeroDivisionError:
#     print("do not divisible by 0")
#
# print("thank you")
# print("take care")


# a = 70
# b = "akki"
#
# try:
#
#     c = a / b
#     print(c)
# except TypeError:
#     print("give integer")
#
# print("thank you")


# num1 = 10
# num2 = 0
# try:
#
#     if num2 == 0:
#         raise ZeroDivisionError("denominator should not be zero")
# except ZeroDivisionError as akki:
#     print("error code : ", akki)
# else:
#     res = num1 / num2
#     print(res)
# finally:
#     print("the end")


# try:
#     age = 25
#     if age < 0:
#         raise ValueError("age should br more than zero")
#     print("your age is :", age)
# except ValueError :
#     print("enter valid age")
#
# print("rest of code")


#CUSTOM EXCEPTION

# class Zero_error(Exception):
#     message = str()
#
#     def __init__(self, message):
#         self.message = message
#
#
#     def __repr__(self):
#         return self.message
#
# num1 = int(input())
# num2 = int(input())
#
# try:
#     if num2 == 0:
#         raise Zero_error("denominator should not be zero")
# except Zero_error as akki:
#     print("code error :", akki)
# else:
#     res = num1 / num2
#     print(res)
# finally :
#     print("the end")





class Checkage(Exception):
    message = str()


    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return self.message

age = int(input("Enter your age :"))

try:

    if age < 18:
        raise Checkage("not eligible to vote")

    else:
        print("eligible to vote")



