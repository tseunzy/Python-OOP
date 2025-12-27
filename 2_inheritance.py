
print("================INHERITANCE AND SUBCLASS=====================")
# Inheritance is like children getting traits from parents. 
# A child class gets everything from a parent class and can add its own unique features
# EVERYTHING get inherited except: Private attributes (starting with __) and Constructor (__init__) must be called explicitly with super()
# PARENT CLASS (Base/Super class)
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# CHILD CLASS (Derived/Sub class)
class Dog(Animal):  # Dog INHERITS from Animal
    # super() is how children talk to their parents:
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent's __init__ using the super class 
        self.breed = breed      # Add new attribute
    
    # Inherits eat() and sleep() from Animal
    
    # Add NEW method
    def bark(self):
        return f"{self.name} says Woof!"

# Another child class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)          # super() is how children talk to their parents:
        self.color = color
    
    def meow(self):
        return f"{self.name} says Meow!"

# Usage
dog_1 = Dog("Buddy", "Golden Retriever")
cat_1 = Cat("Whiskers", "Orange")

print(dog_1.eat())      # "Buddy is eating" - Inherited method from Animal
print(dog_1.sleep())    # "Buddy is sleeping - Inherited
print(dog_1.bark())      # "Buddy says Woof!" - Dog's OWN method

print(cat_1.meow())     # "Whiskers says Meow!" - Cat's OWN method
print(cat_1.name)        # "Whiskers" - Inherited attribute
print(cat_1.sleep())        # Whiskers is sleeping - Inherited instance method



print("================INHERITANCE AND SUBCLASS=====================")
# EVERYTHING get inherited except: Private attributes (starting with __) and Constructor (__init__) must be called explicitly with super()

class Vehicle:
    wheels = 4  # Class variable - inherited
    
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return "Engine started"
    
    def _private_method(self):
        return "Not for public use"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def honk(self):
        return f"{self.brand} {self.model} goes Beep Beep!"

car_1 = Car("Toyota", "Camry")
print(car_1.wheels)    # 4 - Inherited class variable
print(car_1.start())   # "Engine started" - Inherited method
print(car_1.honk())    # "Toyota Camry goes Beep Beep!" - Car's method
print(car_1._private_method())      # "Not for public use - Inherited method



print("================Multiple InheritanceS=====================")

class Mother:
    def eye_color(self):
        return "Brown"

class Father:
    def hair_color(self):
        return "Black"

class Child(Mother, Father):  # Two parents!
    pass

child = Child()
print(child.eye_color())   # "Brown" - From Mother
print(child.hair_color())  # "Black" - From Father



print("================Multilevel Inheritance=====================")
# chain
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# CHILD CLASS (Derived/Sub class)
class Dog(Animal):  
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed      
    
    # Inherits eat() and sleep() from Animal
    
    # Add NEW method
    def bark(self):
        return f"{self.name} says Woof!"

# Multilevel Inheritance
class Cat(Dog):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)          
        self.color = color
    
    def meow(self):
        return f"{self.name} says Meow!"


cat_1 = Cat("Whiskers", "Ekuke", "Orange")

print(cat_1.sleep())        # Whiskers is sleeping - Inherited instance method
print(cat_1.breed)      #  "Ekuke




print("================Method Overriding=====================")
# Children can change what they inherit
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping and sick"

# CHILD CLASS (Derived/Sub class)
class Dog(Animal):  
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is snozing"

# Multilevel Inheritance
class Cat(Animal):
    def __init__(self, name):   
        self.name = name 
    
    def eat(self):
        return f"{self.name} is eating"
    


ani_1 = Animal("Sally")
dog_1 = Dog("Whiskers")
cat_1 = Cat("Jerry")
print(dog_1.sleep())        # "Whiskers is snozing - Inherited instance method
print(dog_1.eat())      #  "Whiskers is eating"

print(cat_1.eat())          # "Jerry is eating
print(cat_1.sleep())        # "Jerry is sleeping and sick" Keep original sleep() from Animal



print("================Example=====================")
class Employee:
    raise_amount = 1.05  # class Variable
    num_of_emp = 0

    # Regular method
    def __init__(self, first, last, pay):  # initailize or constructor # SELF = the employee being created
        self.first = first              # Employee first name
        self.last = last
        self.pay = pay
        self.email = (first + '.' + last + '@company.com').lower()

        Employee.num_of_emp += 1

    def fullname(self):  # method       # SELF = the employee fullname
        return f"{self.first} {self.last}"
    
    def raise_funds(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10     # Changing amount in our subclass do not have any effect on our employee instances

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #OR Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
       
    def add_employee(self, emp):
        if emp not in self.employees:
            return self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            return self.employees.remove(emp)
        
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# creating instances
dev_1 = Developer("Oluwaseun", "Ogundare", 5000, 'java') 
dev_2 = Developer("Sam", "Adeyemi", 6000, 'python')        

mgr_1 = Manager('mike', 'smart', 8000, [])

print(mgr_1.email)          # mike.smart@company.com
print(mgr_1.fullname())     # mike smart

mgr_1.add_employee(dev_2)       # Sam Adeyemi
mgr_1.add_employee(mgr_1)       # mike smart
# mgr_1.remove_emp(mgr_1)

mgr_1.print_emp()

# print(dev_1.email)
# print(dev_1.prog_lang)

# Changing raise_amount(Developer) in our subclass do not have any effect on our Employee instances
# print(dev_1.pay)
# dev_1.raise_funds()
# print(dev_1.pay)



print("================Example 2=====================")
class Payment:
    def __init__(self, amount):
        self.amount = amount
        self.processed = False
    
    def process(self):
        self.processed = True
        return f"Processing ${self.amount} payment"
    
    def refund(self):
        if self.processed:
            return f"Refunding ${self.amount}"
        return "Payment not processed yet"

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number, expiry):
        super().__init__(amount)
        self.card_number = card_number[-4:]  # Store only last 4 digits
        self.expiry = expiry
    
    def process(self):
        result = super().process()  # Call parent's process
        return f"{result} via Credit Card ending in {self.card_number}"

class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    
    def process(self):
        result = super().process()
        return f"{result} via PayPal ({self.email})"
    
    # Add PayPal-specific method
    def send_receipt(self):
        return f"Receipt sent to {self.email}"

# Usage
card_payment = CreditCardPayment(100, "1234567812345678", "12/25")
paypal_payment = PayPalPayment(75, "sam@company.com")

print(card_payment.process())     # "Processing 100 payment via Credit Card ending in 5678
print(paypal_payment.process())  # Processing 75 payment via PayPal (sam@company.com)
print(paypal_payment.send_receipt())  # "Receipt sent to sam@company.com
print(card_payment.refund())    # "refunding 100"  Inherited from Payment



