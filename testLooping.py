fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

charUser = input("Enter a character: ")
newList = [ch for ch in fruits if ch[0] == charUser]
print(newList)
