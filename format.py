# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3.21043

print(f'price 1 is {price1:.2f}') # gir to desimaler (f = floating)
print(f'price 1 is {price1:10}') # setter av 10 spaces når outputet vises
print(f'price 1 is {price1:010}')
print(f'price 1 is {price1:<10}') # left justified
print(f'price 1 is {price1:>10}') # right justified
print(f'price 1 is {price1:^10}') # centered
print(f'price 1 is {price1:+10}') #displays pluss and minus signed
print(f'price 1 is {price1: }') # diplys just minus
print(f'price 1 is {price1:,}') #thousand place seperated with a ,
# kan kombinere alle over og
print(f'price 1 is {price1:+,.2f}')