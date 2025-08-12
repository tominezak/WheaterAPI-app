# keyword arguments = arguments passed to a function by explicitly specifying the parameter name

def hello(greeting, title, first_name, last_name):
    print(f"{greeting}, {title} {first_name} {last_name}!")

hello(title="Mr.", last_name="Doe", first_name="John", greeting="Hello") # posisjonene for argumentene er ikke viktige når vi bruker nøkkelordargumenter

for x in range (1, 11):
    print(x, end='') # end er et keyword argument som spesifiserer hva som skal skrives ut etter hvert tall

print("1", "2", "3", "4", "5", sep='-', end='!') # sep er et keyword argument som spesifiserer hva som skal skrives ut mellom hvert tall

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
print()

phone_num = get_phone(country="47", area="123", first="456", last="7890")
print(phone_num)