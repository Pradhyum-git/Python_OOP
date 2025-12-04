'''

Polymorphism : Polymorphism allows the same method or operator behave differently based on the object or context

Simple Idea : same action --> different behaviours

Poly : many
morphs : forms
'''

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

# Same function call on different objects
def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()

make_sound(d)   # Dog barks
make_sound(c)   # Cat meows

'''
Explanation :
Both classes have same method named sound().
We call same method make_sound() for different objects.
It behaves differently based on the object.
'''