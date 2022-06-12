print("hello world!")

myVariable = "Amar Shivangol"
print(myVariable)
# This is comment
"""
This is a comment
Multiple comments
"""

x = 1
y = 2.8
z = 1j
t = "hello"
print(type(x))
print(type(y))
print(type(z))
print(type(t))

a = """It is the simplest method
 to let a long string split into different lines.
  You will need to enclose it with a pair of Triple quotes, one at the start and second in the end. Anything inside the enclosing Triple quotes will become part of one multiline string
"""
print(a)

b = "Hello, World"
print(b[2:5])
"""
TypeError: can only concatenate str (not "int") to str
age = 36
txt = "My name is John, I am " + age
print(txt)
"""
age = 36
txt = "My name is John, I am {}"
print(txt.format(age))
print("My name is John, I am", 36)

age = 36
test = 34
txt = "My name is John and age {1} and height is {0}"
print(txt.format(age,test))