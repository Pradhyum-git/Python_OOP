'''
Operator Overloading:
        Operator overloading allows the same operator (like +, -, *, /)
        to perform different operations based on the operands.
'''

print(5 + 6)           # performs addition
print('hello' + 'world')  # performs string concatenation

'''
In both statements, we used '+' operator, but it performed different operations.

This happens because Python internally calls methods:

    +  → __add__(a, b)
    -  → __sub__(a, b)
    >  → __gt__(a, b)

For integers: int.__add__(5, 6)
For strings:  str.__add__('hello', 'world')

These special methods are called Magic Methods / Dunder Methods.
'''

print(int.__add__(5, 6))
print(str.__add__('hello', 'world'))

# Operator overloading in a user-defined class

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

s1 = Student(52, 10)
s2 = Student(40, 37)

try:
    print(s1 + s2)
except Exception as e:
    print(e)   # Unsupported operand type error


'''
Let's overload the + operator for Student class
'''

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # Overloading +
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)

    def __gt__(self, other):   # Overloading >
        s1_marks = self.m1 + self.m2   # fixed logic
        s2_marks = other.m1 + other.m2
        return s1_marks > s2_marks


s1 = Student(52, 10)
s2 = Student(40, 37)

s3 = s1 + s2  # calls __add__()
print("Addition of marks: ", s3.m1, s3.m2)

if s1 > s2:   # calls __gt__()
    print("S1 Wins")
else:
    print("S2 Wins")

# __str__ magic method demonstration

a = 10
print(a)                 # internally calls a.__str__()

print(s1)                # prints memory address because __str__ not implemented


'''
Overload __str__ to change object print format
'''

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __str__(self):  # Overloading print()
        return f"({self.m1}, {self.m2})"

s1 = Student(34, 21)
print(s1)  # calls __str__()
