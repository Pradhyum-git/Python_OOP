'''
                    Inheritance :
Inheritance is an OOP concept where a new class acquires the properties and behaviour of parent class.
It promotes reusability of code.
Key idea : Child inherits features from Parent.

Inheritance  follows Is-A-Relationship
'''
# Parent Class
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year  = year
    
    def start(self):
        print(f"{self.brand} {self.model} is starting")
    
    def stop(self):
        print(f"{self.brand} {self.model} is stopping")

# Child Class
class Car(Vehicle):
    def __init__(self,brand,model,year,number_of_doors,number_of_wheels):
        super().__init__(brand,model,year) # don't need initialise the properties here we can pass parent class
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

class Bike(Vehicle):
    def __init__(self,brand,model,year,number_of_wheels):
       super().__init__(brand,model,year)
       self.number_of_wheels = number_of_wheels

car = Car('suzuki','falcon',2018,6,4)
bike =Bike('Honda','cheetah',2015,2)
car.start()
bike.start()
car.stop()
bike.stop()

'''
From the above example we can see that Car and Bike classes are acquiring properties and behaviour from Vehicle class 
such as attributes(brand,model,year) and methods(start,stop).
'''

'''
            Types of Inheritance :
        1)Single Inheritance 
        2)Multilevel Inheritance
        3)Hierarchical Inheritance
        3)Multiple Inheritance
        4) Hybrid Inheritance
'''

'''
 Single Inheritance : 
        One child inherits from one parent class
 Ex :
        Parent --> Child

'''
# Parent Class
class Animal:
    def sound(self):
        print("Animal Makes Sound")

# Child Class (Inheriting from Animal)
class Dog(Animal):
    def bark(self):
        print('Dog is barking')
    
# Creating object of child class
dog = Dog()
dog.bark() # Child class method
dog.sound() # Inherited from Parent class

'''
MulitLevel Inheritance :
    In multilevel inheritance, a class inherits from another child class, creating a chain of inheritance.
Ex: 
    GrandParent --> Parent --> Child
'''

# Grandparent Class
class Animal:
    def eat(self):
        print("Animal is eating")

# Parent Class
class Dog(Animal):  # Inherits from Animal
    def bark(self):
        print("Dog is barking")

# Child Class
class Puppy(Dog):  # Inherits from Dog (and indirectly from Animal)
    def play(self):
        print("Puppy is playing")

# Creating object of the Child class
puppy = Puppy()
puppy.play()   # Child class method
puppy.bark()   # Parent class method
puppy.eat()    # Grandparent class method

'''
                Animal (GrandParent)
                   |
                   |
                  Dog (Parent)
                   |
                   |
                  Puppy (Child)

'''

'''
            Hierarchical Inheritance
    In hierarchical inheritance, one parent class is inherited by multiple child classes.
    Ex:
                Parent
                /    \
               /      \ 
            Child1   Child2
'''

# Parent Class
class Animal:
    def eat(self):
        print("Animal is eating")

# Child Class 1
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Child Class 2
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

# Creating objects
dog = Dog()
cat = Cat()

dog.eat()   # Inherited from Animal
dog.bark()  # Unique to Dog

cat.eat()   # Inherited from Animal
cat.meow()  # Unique to Cat


'''
            Multiple Inheritance
    A single child class inherits from mulitple Parent classes
    Ex: 
        Parent1 + Parent2 --> Child
    
    Visually :
            Parent1     Parent2
               \           /  
                \         /
                 \       /
                   Child
'''
# Parent Class 1
class Father:
    def skill(self):
        print("Father: Knows Driving")

# Parent Class 2
class Mother:
    def talent(self):
        print("Mother: Good in Singing")

# Child Class inheriting from both Father and Mother
class Child(Father, Mother):
    def play(self):
        print("Child: Enjoys playing games")

# Creating object of Child class
child = Child()
child.play()     # Child's own method
child.skill()    # Inherited from Father
child.talent()   # Inherited from Mother


'''
            Hybrid Inheritance
    Hybrid Inheritance is a combination of two or more types of inheritance (such as single , multilevel , multiple , hierarchical inheritance)
    Ex:
         A
       /   \
      B     C
       \   /
         D

'''
# Parent Class
class Animal:
    def eat(self):
        print("Animal is eating")

# Child Single Inheritance
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Another Child Single Inheritance
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

# Hybrid Inheritance (Multiple Inheritance)
class Pet(Dog, Cat):
    def play(self):
        print("Pet is playing")
        
pet = Pet()
pet.eat()   # Inherited from Animal (via Dog/Cat)
pet.bark()  # From Dog
pet.meow()  # From Cat
pet.play()  # Own method


