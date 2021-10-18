class Hello:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello {self.name.title()} you have {self.age}"

name = input("write your name: ")

age = int(input("Write your age: "))

user = Hello(name, age)
print(user)
