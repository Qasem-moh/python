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


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def myfunc(self):
        return "Hello my name is " + self.name

    def ReturnName(self):
        if self.gender == "Male":
            return f"Hello Mr {self.name}"
        elif self.gender == "Female":
            return f"Helo Miss {self.name}"
        else:
            return f"Hello {self.name}"


p1 = Person("John", 36, "Male")
p2 = Person("Sara", 25, "Female")
p3 = Person("Qasem", 29, "")
print(p1.name, p1.age)
print(p1.myfunc())
print(p1.ReturnName())
print(p1.ReturnName())
print(p2.ReturnName())
print(p3.ReturnName())
