# 1. Printa en text
print("Hello, world")

# 2. Printa en variabel
x = "Hello, world"
print(x)

# 3.funktion som printar en fast text
def greet_world():
    print("Hello, world")

greet_world()

# 4. funktion som printar en fast text med en flytande variabel
def greet(name):
    return f"Hello, {name}"

print(greet("world"))

# 5. en klass som har ett namn och printar en fast funktion som hälsar på en flytande variabel

class Person:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return f"Hello, {self.name}"

vendela = Person("world")

print(vendela.greeting())