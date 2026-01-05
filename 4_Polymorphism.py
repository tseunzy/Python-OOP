

print("================Polymorphism================")
# Polymorphism = "Many Forms" (Poly = Many, Morph = Forms)
# Same action, different behavior
print('========METHOD OVERRIDING=======')
# 1. METHOD OVERRIDING
# Different classes doing the same thing differently
class Animal:       # Parent class
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):      # Child class - OVERRIDES speak()
    def speak(self):  # Same method name w different implementation
        return "Woof! Woof!"

class Cat(Animal):   # Child class - OVERRIDES speak()
    def speak(self):  # Same method name different implementation
        return "Meow!"

class Cow(Animal):      # Child class - OVERRIDES speak()
    def speak(self):  # Same method name different implementation
        return "Moo!"

class Duck(Animal):     # Child class - OVERRIDES speak()
    def speak(self):  # Same method name different implementation
        return "Quack!"


animals = [Dog(), Cat(), Cow(), Duck()]

for animal in animals:
    # Same method call, different behavior!
    print(f"{animal.__class__.__name__}: {animal.speak()}")
    
# Output
# Dog: Woof! Woof!
# Cat: Meow!
# Cow: Moo!
# Duck: Quack!

print('===================================================')



class Employee:
    def get_salary(self):
        return 3000

class Manager(Employee):
    def get_salary(self):
        return 8000

class Intern(Employee):
    def get_salary(self):
        return 1500


employees = [Employee(), Manager(), Intern()]

for emp in employees:
    print(f"{emp.__class__.__name__}: {emp.get_salary()}")

# Output
# Employee: 3000
# Manager: 8000
# Intern: 1500


print('====================DUCK TYPING=======================')
# “I don’t care what you are.
# If you can speak(), I’ll call it.”

class Dog:      
    def speak(self):  
        return "Woof! Woof!"

class Cat:  
    def speak(self): 
        return "Meow!"

class Cow:     
    def speak(self): 
        return "Moo!"

class Duck:     
    def speak(self):  
        return "Quack!"

class Sound:
    def make_sound(self, obj):
        print(obj.speak())   # just call speak() # Duck typing


sound1 = Sound()

sound1.make_sound(Cat())        #Meow!
sound1.make_sound(Cow())        #  Moo!
sound1.make_sound(Dog())        # Woof! Woof!
sound1.make_sound(Duck())       # Quack!


print('===================================================')


class Employee:
    def get_salary(self):
        return 3000

class Manager(Employee):
    def get_salary(self):
        return 8000

class Intern(Employee):
    def get_salary(self):
        return 1500

class Contractor:       # Contractor has get_salary()
    def get_salary(self):
        return 5000


employees = [Employee(), Manager(), Intern(), Contractor()]

for emp in employees:
    print(f"{emp.__class__.__name__}: {emp.get_salary()}")  # Duck typing

# Employee: 3000
# Manager: 8000
# Intern: 1500
# Contractor: 5000




print('==============OPERATOR OVERLOADING====================')

# Dunders
# Making +, -, , etc. work with your objects

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def __add__(self, amount):
        return BankAccount(self.balance + amount)
    
    def __sub__(self, amount):
        return BankAccount(self.balance - amount)
    
    def __iadd__(self, amount):
        self.balance += amount
        return self
    
    def __gt__(self, other):
        if self.balance > other.balance:
            return True
        else:
            return False
        
    def __str__(self):
        return f"BankAccount with balance: {self.balance}"

    def __repr__(self):
        return f"BankAccount (balance={self.balance})"

    
account1 = BankAccount(150)
account2 = BankAccount(300)

print(account1)
print(account1 + 200)
print(account1 - 50)

account2 += 250
print(account2)

print(account1 > account2)

# print(str(account))
print(repr(account1))

# print(account.__str__())
# print(account.__repr__())

# print(int.__add__(1, 2))  # 3
# print(str.__add__('Hello, ', 'World!'))  # Hello, World!


print('===================================================')


class student:

    def __init__(self, name, m1, m2):
        self.name = name
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self, other):           # Addition (+)
        name = f"{self.name } {other.name}"
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(name, m1, m2)

        return s3

    def __gt__(self, other):  # Greater than (>)
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):          # readable string
        return f"{self.name}: {self.m1}, {self.m2}"
    
    def __repr__(self):
        return f"name({self.m1}, {self.m2})"
    
    def __len__(self):
        return len(self.name)


s1 = student('Mark', 50, 20)
s2 = student('Ada', 30, 40)

s3 = s1 + s2   # -> student.__add__(s1,s2)
print(s1)
print(s2)
print(s3)
print(repr(s1))

print(len(s2))

# print(student.__add__(s1, s2))

# if s1 > s2:
#     print('s1 wins')
# else:
#     print('s2 wins')

# print(s1)


print('================METHOD OVERLOADING====================')


class Calculator:

#     def sum1(self, a=None, b=None, c=None):  # you set default parameter as None so it can accept what come in and if it doesnt comes in
#         if a!=None and b!=None and c!=None:
#             s = a + b + c
#         elif a!=None and b!=None:
#             s = a + b
#         else:
#             s = a
#         return s

# cal = Calculator()
# print(cal.sum1(4, 3))

    def add(self, *args):
        if len(args) == 1:
            return args[0]
        elif len(args) == 2:
            return args[0] + args[1]
        elif len(args) > 2:
            return sum(args)
        else:
            return 0
    
    def multiply(self, x, y=None): # you set default value as none
        if y is None:
            return x
        else:
            return x * y

calc = Calculator()

# Same method name, different behaviors based on arguments!
print(f"{calc.add(5)}")           # 5
print(f"{calc.add(5, 3)}")     # 8
print(f"{calc.add(1, 2, 3, 4, 8, 5)}")  # 23

print(f"{calc.multiply(4)}")        # 4
print(f"{calc.multiply(4, 5)}")    # 20



print('==============ABSTRACT BASE CLASSES (ABCs)===============')
# the are incomplete
# Can't instantiate abstract classon it own
# Abstraction - hiding the methods from the user (hiding a structure)
# 
from abc import ABC, abstractmethod

class Shape(ABC): # you cant create object of the abstract class 

    @abstractmethod     # Must be implemented by subclasses
    def area(self):
        pass            # you dont define the method in abstract 

    @abstractmethod     # Must be implemented by subclasses
    def perimeter(self):
        pass

    def my_shape(self):         # just a method without abstraction 
        print(f"My shape is {self.__class__.__name__}")

class Circle(Shape):

    def area(self, radius):
        return 3.142 * radius ** 2
    
    def perimeter(self, radius):
        return 2 * 3.142 * radius
    
class Rectangle(Shape):

    def area(self, width, height):
        return width * height
    
    def perimeter(self, width, height):
        return 2 * width * height
    

class Triangle(Shape):

    def __init__(self, base, height, side1, side2, side3):  # I can also initialize first
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

cir = Circle()
print(cir.area(5))          # 78.55
print(cir.perimeter(6))     # 37.704
cir.my_shape()              # My shape is Circle

rect = Rectangle()
print(rect.area(2, 4))          # 8
print(rect.perimeter(4, 3))     # 24
rect.my_shape()             # My shape is Circle      # This was inherited from the Shape class

trig = Triangle(2, 5, 3, 5, 5)
print(trig.area())          # 5.0
print(trig.perimeter())     # 13 
trig.my_shape()             # My shape is Triangle  ## This was inherited from the Shape class


