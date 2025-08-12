# functions = a block of reusable code - place () after the name to run it

def happy_birthday():
    print('Happy Birthday to you!')
    print('Happy Birthday to you!')
    print('Happy Birthday dear friend!')
    print('Happy Birthday to you!')
    print()

happy_birthday()
happy_birthday()

def greet(name):
    print(f'Hello {name}!')

greet('Bro')

def greet2(name, age): # parameteres in parentheses
    print(f'Hello {name}, you are {age} years old!')

greet2('Bro', 30) # arguments in parentheses
print()

def displa_invoice(username, amount, duedate):
    print(f'hello {username},')
    print(f'your bill of ${amount} is due on {duedate}.')

displa_invoice('Bro', 100, '2023-10-31')

# return = statement used to end a function and send a result back to the caller
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Cannot divide by zero!'
    return x / y

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

def create_name(first, last):
    first = first.capitalize() 
    last = last.capitalize()
    return first + ' ' + last

full_name = create_name('bro', 'code')
print(full_name)