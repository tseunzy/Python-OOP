print("================Encapsulation & Private Attributes================")

# Encapsulation is about hiding internal implementation details and exposing only what's necessary

print("\n================Public ================")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner      # Public - anyone can see
        self.balance = balance  # Public - anyone can change (DANGER!)

acct = BankAccount("Ada", 1000)
print(acct.owner)    # "Ada" 
acct.balance = -500  # Can set negative balance!
print(acct.balance)  # the balance can be easily accessible 


print("================Protected (_single_underscore)================")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Protected (convention only)
    
    def get_balance(self):
        return self._balance

acct = BankAccount("Ada", 1000)
acct.balance = -500      # Cannot be accessible easily
print(acct._balance)  # 1000 Can still access (it's just a warning)
print(acct.get_balance())   # 1000 (through method)


print("================Private (__double_underscore)================")
#  simple BankAccount
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # PRIVATE
    
    # Public method to access private data
    def get_balance(self):
        return self.__balance
    
    # Public method to modify private data
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposite ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount"

acct = BankAccount("Ada", 1000)
print(acct.owner)          # "Ada"
print(acct.get_balance())  # 1000 (through method)

# Try to access private attribute directly:
# print(acct.__balance)      # AttributeError: 'BankAccount' object has no attribute '__balance'
# acct.__balance = -500      # Creates NEW public attribute, doesn't touch private one!




print("================Examples================")

class Person:
    def __init__(self, name, age):
        self.name = name        # public  
        self.age = age
        self._mood = "happy"    # protected-by-convention
        self.__ssn = "123-45"   # “privateish” (name-mangled)

p = Person("Ada", 10)
print(p.name)      # OK
print(p._mood)     # Possible, but you're *not supposed to*
# print(p.__ssn)   # AttributeError 
print(p._Person__ssn)  # but can be access using the class name but not advisible cos its secret
# but it exists as _Person__ssn under the hood (don’t rely on this!)




print("================Examples================")
class Secret:
    def __init__(self):
        self.public = "I'm public"
        self._protected = "I'm somewhat private"
        self.__private = "I'm really private!"
    
    def reveal(self):
        return self.__private  # Works inside class

secret_1 = Secret()

print(secret_1.public)           # "I'm public" 
print(secret_1._protected)       # "I'm somewhat private"
# print(secret.__private)      # AttributeError

# But you CAN access it if you know the mangled name:
print(secret_1._Secret__private)  # "I'm really private!" 
# Don't do this! Breaks encapsulation!



print("================Examples================")
# Create a SimpleTV class
class SimpleTV:
    def __init__(self):
        self.brand = "Sony"  # Public
        self.__channel = 1    # Private
        self.__volume = 10    # Private
        self.__is_on = False  # Private
    
    def turn_on(self):
        # Your code here
        if not self.__is_on:
            self.__is_on = True
            print(f"TV is now ON!")        
        else:
            print(f"TV is OFF!")
         
    
    def turn_off(self):
        # Your code here
        if self.__is_on:
            self.__is_on = False
            print("TV is now OFF!")
        else:
            print("TV is already OFF!")

    
    def change_channel(self, new_channel):
        # Your code here (only 1-100 channels)
        
        if new_channel >= 1 and new_channel <= 100:
            self.__channel = new_channel
            print(f"Changed to channel {self.__channel}")
        else:
            print("Channel should be between 1-100!")

    
    def volume_up(self):
        # Your code here (max volume 50)
        if self.__volume < 50:
            self.__volume += 1
            print(f"Volume: {self.__volume}")
        else:
            print("Volume is max 50!")
    
    def volume_down(self):
        # Your code here (min volume 0)
        if self.__volume > 0:
            self.__volume -= 1
            print(f"Volume: {self.__volume}")
        else:
            print(f"Volume is min 0!")
    
    def get_status(self):
        # Return "TV is ON/OFF, Channel: X, Volume: Y"
        status = "ON" if self.__is_on else "OFF"
        return f"{self.brand} TV is {status}, Channel: {self.__channel}, Volume: {self.__volume}"

# Test it
tv = SimpleTV()             
tv.turn_on()                 # TV is now ON!
tv.turn_off()                # TV is now OFF!
tv.change_channel(50)       # Changed to channel 50
tv.volume_up()               # Volume: 11
tv.volume_up()              # Volume: 12
print(tv.get_status())      # Sony TV is OFF, Channel: 50, Volume: 12



print("================USING PRIVATE METHODS ================")


class TVWithWelcome:
    def __init__(self):
        self.__is_on = False
    
    def turn_on(self):
        if not self.__is_on:
            self.__is_on = True
            self.__display_welcome()  # Private method
            return True
        return False
    
    # Private method 1
    def __display_welcome(self):
        print("Welcome to Smart TV!")

tv = TVWithWelcome()
tv.turn_on()            # Welcome to Smart TV!

print(tv._TVWithWelcome__display_welcome()) # wrong way to access the private methods



print("================@property, @getter, @setter================")
# @property
class Employee:

    # Regular method
    def __init__(self, first, last):  # 
        self.first = first              
        self.last = last
        # self.email = first + '.' + last + '@company.com'

    @property       # A method becomes accessible as an attribute whe we use @property above it
    def email(self):
        return self.first + '.' + self.last + '@company.com'
    
    def fullname(self):  # method       # SELF = the employee fullname
        return f"{self.first} {self.last}"
    
    @property 
    def fullnames(self):
        return f"{self.first} {self.last}"
    
    @fullnames.setter       # @fullnames.setter Set a new first and last name. 
    def fullnames(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last 

    @fullnames.deleter     # @fullnames.deleter deleter a new first and last name. 
    def fullnames(self):
        print("Delete name")
        self.first = None
        self.last = None
    
employ = Employee("Ada", "Obi")

employ.fullnames = "Ogundare Oluwaseun"

print(employ.fullnames)

print(employ.email)         # Accessing the email as an attri
# print(employ.fullname())  # A method becomes accessible as an attribute whe we use @property above it

del employ.fullnames

print(employ.fullnames)     # returns None


print("================@property, @getter, @setter================")


class Oldperson:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):           # Getter method
        return self.__age
    
    def set_age(self, new_age):  # Setter method
        if new_age > 0:
            self.__age = new_age

person = Oldperson("Ada", 25)
# print(person.get_age())  # accesing methods
# person.set_age(26)       # accesing methods
# print(person.get_age())


# USing the @property sty;e 
class NewPerson:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    @property           # @property makes a method act like an attribute
    def age(self):              # Getter
        return self.__age
    
    @age.setter
    def age(self, new_age):     # Setter
        if new_age > 0:
            self.__age = new_age

person = NewPerson("Ada", 25)
# print(person.age)      # Like accessing an attribute
# person.age = 26        # Like setting an attribute
# print(person.age) 

print("================@property - getter================")

class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute
    
    # @property makes a method act like an attribute
    @property
    def radius(self):
        """Getter for radius"""
        return self.__radius
    
    @property
    def area(self):
        """Calculated property (no setter = read-only)"""
        return 3.14 * self.__radius * self.__radius
    
    @property
    def circumference(self):
        """Another read-only property"""
        return 2 * 3.14 * self.__radius

circle = Circle(5)

print(circle.radius)        # 5 - calls radius() method like attribute
print(circle.area)          # 78.5 
print(circle.circumference) # 31.4 

# circle.area = 100        # AttributeError: can't set attribute (no setter)

print("================@property - Ssetter================")

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    # Setter for radius
    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
        else:
            print("Radius should be positive")
    
    @property
    def area(self):
        return 3.14 * self.__radius * self.__radius

circle = Circle(5)

print(circle.radius)  # 5
circle.radius = 10    
print(circle.radius)  # 10 
print(circle.area)    # 

circle.radius = -5    # Radius should be positive" 
print(circle.radius)  # Still 10 - not changed due to invalid


print("================@property - Ssetter================")
# You need a getter to set a stter
class Vehicle:
    def __init__(self, speed):
        self.__speed = speed  # Private
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        if value >= 0 and value <= 200:
            self.__speed = value
        else:
            print("Invalid speed")

class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand
    
    # Inherits speed property from Vehicle!
    @property
    def info(self):
        return f"{self.brand} going at {self.speed} km/h"

car = Car(100, "Toyota")
print(car.speed)    # 100  
car.speed = 120      # Setter
# car.speed = 300   # "Invalid speed
print(car.info)     # "Toyota going at 120 km/h - Setter