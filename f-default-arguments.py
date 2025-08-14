#default arguments = a default value for certain parameters in a function 
# default is used if no value is passed for that parameter

def net_price(list_price, discount=0, tax=0.05): # kan ha arhumenter uten verdi, men dersom man fyller inn 
    # verdier for disse, så vil de bli brukt i stedet for default verdiene
    return list * (1 - discount) * (1 + tax)

print(net_price(100))  # bruker default verdier for discount og tax
print(net_price(100, 0.1))  # bruker default verdi for tax
print(net_price(100, 0.1, 0.07))  # bruker ingen default verdier

import time
def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)  # venter i 1 sekund mellom hvert tall
    print("Counting complete!")

count(1, 10)  # teller fra 1 til 5 med 1 sekund mellom hvert tall