# args = gjør sånn at vi kan sende inn et vilkårlig antall argumenter til en funksjon - tuple
# kwargs = gjør sånn at vi kan sende inn et vilkårlig antall nøkkelordargumenter til en funksjon - dictonary

def add(*args):
    # return type(args)
    total = 0   
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))  # pakker alt inn i en tuple

def display_names(*args):
    for arg in args:
        print(arg, end='')

display_names("Alice", "Bob", "Charlie")
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Main St", city="Anytown", state="CA", zip="12345")
print('----------------')

# Kombinere args og kwargs:
def shipping_label(*args, **kwargs):
    print("Shipping Label:")
    for arg in args:
        print(arg, end=' ')
    print()  # for å få en ny linje etter navnene
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f'{kwargs.get("street")}')
        print(f'{kwargs.get("pobox")}')
    else:
        print(f'{kwargs.get("street")}')
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "SquarePants", # Blanding av argumenter - husk å ha args først og deretter kwargs
               street = "123 fake street. ",
               pobox = "1234",
               apt = "1A",
               city = "Detroit",
               state = "Michigan",
               zip = "12345")