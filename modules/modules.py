# module = a file that contains Python code - use import to use it in another file

# print(help('modules'))

import math
import math as m
# from math import pi, sqrt, ceil, floor - kan skrive print(pi) istedenfor print(math.pi), men kan skape konflikt med andre variabler
print(math.pi)  # Returns the value of pi
print(m.pi)  # Returns the value of pi using the alias 'm'

# Example of importing a custom module
import modexample
result = modexample.pi
result = modexample.square(9)

print(result)  

