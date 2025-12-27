
print("================Object-Oriented Programming================")

# Data (attributes): color, brand, speed, fuel level -> WHAT THEY HAVE 
# Functions (methods): start(), stop(), accelerate(), refuel() -> WHAT THEY CAN DO

#  Create a simple employee class
#  A class is a blueprint for creating instances and each unique employee
# Class Variable: Shared by ALL instances (like family surname)
# Instance Variable: Unique to EACH instance (like personal name)

print("\n=========Creating Instances=======")

class Dog:
    def __init__(self, name):  # self = the dog being created
        self.name = name       # THIS dog's name
    
    def bark(self):            # self = the dog barking
        return f"{self.name} says Woof!"  # THIS dog's name

# When we create instances:
buddy = Dog("Buddy")   # self = buddy
max = Dog("Max")       # self = max

print(buddy.bark())  # Buddy says Woof! (self was buddy)
print(max.bark())    # Max says Woof!  (self was max)

print("================================")

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100 # It remains for each instance
    
    def attack(self, other_player):
        other_player.health -= 10
        return f"{self.name} attacked {other_player.name}!"

player1 = Player("Ada")
player2 = Player("Efe")

print(player2.health)           # 100
print(player1.attack(player2))  # Ada attacked Efe!
print(player2.health)           # 90


print("===============Class Variable======================")

class Family:
    # CLASS VARIABLE - Shared by all
    last_name = "Ogundare"  # Shared family name
    
    def __init__(self, first_name):
        # INSTANCE VARIABLE - Unique to each
        self.first_name = first_name  # Personal name

# Create family members
dad = Family("Seun")
mom = Family("Mary")
son = Family("Tom")

print(dad.first_name, Family.last_name)    # Seun Ogundare
print(mom.first_name, mom.last_name)    # Mary Ogundare  
print(son.first_name, son.last_name)    # Tom Ogundare


print("=====================================")

class MenuItem:
    # CLASS VARIABLES (same for all items)
    restaurant = "Tasty Bites"
    tax_rate = 0.08
    
    def __init__(self, name, price):
        # INSTANCE VARIABLES (unique to each item)
        self.name = name
        self.price = price
    
    def total_price(self):
        return self.price * (1 + MenuItem.tax_rate)

burger = MenuItem("Burger", 10)
pizza = MenuItem("Pizza", 15)


print(burger.restaurant)  # Tasty Bites (shared) # print(MenuItem.restaurant)
print(pizza.restaurant)   # Tasty Bites (shared) #object.attribute or self.attribute or ClassName.attribute
print(burger.name)        # Burger (unique)
print(pizza.name)         # Pizza (unique)
print(burger.total_price()) # 10.8


print("=====================================")
class Classroom:
    # CLASS VARIABLE with list
    all_students = []  # Shared list
    
    def __init__(self, student_name):
        self.name = student_name
        Classroom.all_students.append(self.name)

class1 = Classroom("Ada")
class2 = Classroom("Efe")

print(Classroom.all_students)  # ['Ada', 'Efe'] 
# Both instances share the SAME list!

class3 = Classroom("Charlie")
print(Classroom.all_students)  # ['Ada', 'Efe', 'Charlie']
# All classes see Charlie added!


print("=====================================")
class Classroom:
    def __init__(self, student_name):
        self.name = student_name
        self.students = []  # INSTANCE variable - unique list
        self.students.append(student_name)

class1 = Classroom("Ada")
class2 = Classroom("Efe")

print(class1.students)  # ['Ada']
print(class2.students)  # ['Efe']  Different lists!



print("=====================================")
class Car:
    wheels = 4          #  Class variable (all cars have 4 wheels)
    
    def __init__(self, brand, color):
        self.brand = brand  # Instance variable
        self.color = color  # Instance variable
        self.mileage = 0    # Instance variable
        
        Car.total_cars += 1  # 

Car.total_cars = 0      # Class variable (added later)


my_car = Car("Toyota", "red")
your_car = Car("Honda", "blue")

print(Car.total_cars)        # 2 -> just two cars created 

my_car.mileage = 10000  # Changing instance variable
Car.wheels = 5          # Changing class variable (now all have 5 wheels!)
print(my_car.wheels)    # 5
my_car.wheels = 3       # Changing instance variable
print(my_car.wheels)      # 3
print(Car.wheels)       # 5 -> Changing the instance doesnt affect the class variable



print("==============USING INSTANCES METHOD=====================")
# USED INSTANCES METHOD ALL THROUGH
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited NGN{amount}. New balance: NGN{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry, not enough funds!")
        else:
            self.balance -= amount
            print(f"Withdrew NGN{amount}. New balance: NGN{self.balance}")

account1 = BankAccount("Seun", 1000)
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)






















# Use Class Variables When:
# Data is shared by all instances

# Tracking totals/counts across all objects

# Constants (like tax rates, company name)

# Default values for all instances

# Use Instance Variables When:
# Data is unique to each object

# State that changes independently

# Properties specific to one object

