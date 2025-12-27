
print("================Object-Oriented Programming================")
# Instance Method: Works with instance data (self)

# Class Method: Works with class data (cls)

# Static Method: Works with NO data (just a function in a class)
print("\n=========Instance(regular one)=======")


# Instance(regular one)
class Student:
    def __init__(self, name, grade):
        self.name = name      # Instance variable
        self.grade = grade    # Instance variable
    
    # INSTANCE METHOD - uses self
    def display(self):
        return f"{self.name}: {self.grade}"
    
    # Another instance method
    def upgrade_grade(self):
        if self.grade == "A":
            self.grade = "A+"
        elif self.grade == "B":
            self.grade = "A"

# Usage
student1 = Student("Ada", "B")
student2 = Student("Efe", "A")

print(student1.display())     # Ada: B
student1.upgrade_grade()
print(student1.display())     # Ada: A  (changed!)

# Can't call without instance!
# Student.display()  # ERROR! Needs self. can only work in lass method


print("================Class methods=====================")
# Class methods are PERFECT for factory patterns - alternative ways to create instances
# A factory method is an alternative constructor that creates instances in different ways, not just through __init__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Normal way: Person("Ada", 25)
    
    # FACTORY METHOD 1: From birth year
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year  # Calculate age
        return cls(name, age)    # Calls __init__
    
    # Class METHOD 2: From dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])
    
    # Class METHOD 3: From CSV string
    @classmethod
    def from_csv(cls, csv_string):
        name, age = csv_string.split(",")
        return cls(name.strip(), int(age.strip()))
    
    # Class METHOD 4: Default adult
    @classmethod
    def create_adult(cls, name):
        return cls(name, 18)  # Default age for adult

# Different ways to create the SAME Person class:
person1 = Person("Ada", 25)                       # Normal
person2 = Person.from_birth_year("Efe", 1995)      # From birth year
person3 = Person.from_dict({"name": "Charlie", "age": 30})  # From dict
person4 = Person.from_csv("David, 35")            # From CSV
person5 = Person.create_adult("Eve")               # Default adult

print(person2.age)  # 29 (2024 - 1995)
print(person4.name) # "David"



print("================Class methods=====================")

class Product:
    def __init__(self, sku, name, price, category):
        self.sku = sku
        self.name = name
        self.price = price
        self.category = category
    
    @classmethod
    def from_api_response(cls, api_data):
        # Extract and transform data
        sku = api_data['product_code']
        name = api_data["product_name"].title()
        price = float(api_data['price']['amount'])
        category = api_data['category']["name"]
        
        # Add tax
        price *= 1.08
        
        return cls(sku, name, price, category)

# API returns complex JSON, but creation is simple:
api_data = {
    "product_code": "P123",
    "product_name": "wireless mouse",
    "price": {"amount": "29.99", "currency": "USD"},
    "category": {"id": 5, "name": "Electronics"}
}

product = Product.from_api_response(api_data)
print(product.name)   # Wireless Mouse
print(product.price)  # 32.3892 (with tax)
print(product.category)  # David



print("==============STATIC METHOD=======================")


class MathUtils:
    # STATIC METHOD - just a function, no self, no cls
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0

# Usage - NO INSTANCE NEEDED
result1 = MathUtils.add(5, 3)        # 8
result2 = MathUtils.multiply(4, 5)   # 20
result3 = MathUtils.is_even(10)       # True

print(result1)
print(result2)
print(result3)

# Can also call on instance (but pointless)
calc = MathUtils()
result4 = calc.add(2, 2)             # 4 -> weird but works
print(result4)


print("==============STATIC METHOD=======================")
class Geometry:
    @staticmethod
    def circle_area(radius):
        return 3.14159 * radius * radius
    
    @staticmethod
    def rectangle_area(width, height):
        return width * height
    
    @staticmethod
    def triangle_area(base, height):
        return 0.5 * base * height
    
    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# All geometry functions in one place
area = Geometry.circle_area(5)
distance = Geometry.distance(0, 0, 3, 4)
triangle = Geometry.triangle_area(7, 9)

print(area)
print(distance)
print(triangle)




print("==============STATIC METHOD=======================")
class Example:
    class_var = "I'm a class variable"
    
    @staticmethod
    def print_class_var():
        pass# print(class_var)  #  ERROR! Need to access via class name
        
    @staticmethod
    def correct_print():
        return (Example.class_var)  #  CORRECT - use class name

correct = Example.correct_print()       # Class.method()
print(correct)

# correct = Example()
# print(correct.correct_print())              # obj.method()



print("===============Static & Class Methods======================")

class Example:
    class_var = "Shared data"
    
    def __init__(self, instance_var):
        self.instance_var = instance_var
    
    @staticmethod
    def static_example(x, y):
        # Can't access self or cls
        # Just a regular function
        return x + y 
    
    @classmethod
    def class_example(cls, x):          #  class method
        # Can access cls (the class)
        # Can modify class variables
        cls.class_var = "Modified"
        return f"{cls.class_var}: {x}"
    
    def instance_example(self, x):  #  Instance method
        # Can access self (the instance)
        # Can modify instance variables
        self.instance_var = x
        return f"{self.instance_var}"

# Usage
print(Example.static_example(5, 3))      # 8 - just math
print(Example.class_example("test"))     # "Modified: test" - uses class
obj = Example("initial")
print(obj.instance_example("new"))       # new - uses instance
print(Example.class_var)                 # Modified - it gets changed all through






print("================Static & Class Methods Example=====================")
#  that we create using our employee class will be instance of that class
class Employee:
    raise_amount = 1.05  # class Variable
    num_of_emp = 0

    # Regular method
    def __init__(self, first, last, pay):  # initailize or constructor # SELF = the employee being created
        self.first = first              # Employee first name
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1

    def fullname(self):  # method       # SELF = the employee fullname
        return f"{self.first} {self.last}"
    
    def raise_funds(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod                # Class method/function  LIKE DECORATOR OF THE MAIN CLASS 
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return Employee(first, last, pay)       # return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # In python, monday == 0, Sunday == 6
            return False
        return True

# creating instances
emp_1 = Employee("Oluwaseun", "Ogundare", 5000) # instances of class Employee
emp_2 = Employee("Sam", "Adeyemi", 6000)        # instances 2

import datetime
my_date = datetime.date(2025, 12, 19)

print(Employee.is_workday(my_date))

#Class method details 
emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Avian-Mike-9000'
# first, last, pay = emp_str_1.split('-')     # now as a class method above 
new_emp_1 = Employee.from_string(emp_str_3)   # to call a class method 

print(new_emp_1.email)
print(new_emp_1.pay)



# Employee.set_raise_amt(1.09)       # it accept the class auto, we pass the amount in. emp_1.set_raise_amt(1.09)
# # Employee.raise_amount = 1.09     # Its same as using the class method
# print(Employee.raise_amount)       # 2 -> just two Employees created 
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)          # EMployee superceed the instance variable  


