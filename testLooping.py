# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


# charUser = input("Enter a character: ")
# newList = [ch for ch in fruits if ch[0] == charUser]
# print(newList)
# *****************************************************************************
# class MyClass:
#     x = 5
#
#
# print(MyClass)
# print(MyClass.x)
# //////////////////////////////////////////////////////////////////////////////
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Student:
    pass


class Memebers:
    def __init__(self):
        print("Add member ")


Memebers()
