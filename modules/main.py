# variable scope = where a variable is accessible
# scope resolution = LEGB - Local -> Enclosing -> Global -> Built-in

def func1():
    a = 1
    print(a) # local to func1
func1()

def func2():
    x = 1
    def func3():
        x = 2
        print(x)
    func3() # prints 2, local to func3 - regel å bruke lokal variabe før global variabel

# GLOBAL:
def func4():
    print(y)  # prints 1, local to func4
def func5():
    print(y)

y = 3  # hvis det ikker eksisterer en lokal variabel eller enclosing variabel bruker den global variabel

#BUILT IN:
from math import e
def func6():
    print(e)  # prints the value of e from the math module, built-in variable
e = 3  # if this line is executed, it will override the built-in value of e
func6()  # prints 3, the overridden value of e