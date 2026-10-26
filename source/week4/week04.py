'''
Week 04: Solving problems with variables and expressions
Sister Bingham

'''
import math

#### f-strings (new vs old)
a = 100
b = 45
# new
print(f'This is a string with f-string formatting... {a + 5 * 23 - 12:.2f} {b} {"nice":&>10}')
# old
print('This is a string with .format formatting... {:.2f} {} {:&>10}'.format((a + 5 * 23 - 12), b, "nice"))
print('This is a string with .format formatting... {1:.2f} {0} {2:&>10}'.format((a + 5 * 23 - 12), b, "nice"))
print()

#### take a look at the formatting reference sheet
print(f'here\'s another example: {a:*^10.2f} and {b: ^20}') ###but it can also be spaces - it can only be one item
print()

#### Review input, conversion, output: calculate f = ma  (force = mass * acceleration)
mass = float(input("Mass (kg): "))   # notice the nested functions, input() is inside float(), so input executes first
accel = float(input('Acceleration (m/s^2): '))
force = mass * accel
print(f"{force=}")  # cool trick to print variable=value
print()

#### print result formatted nicely and with 4 decimals
print(f'Force is {force:.4f} Newtons')
print()

#### Review: what do I do if there's a function in the math module 
#### that I need to use? (see top of code)
x = 10 ** .5
print(x)
print()

y = float(input('Enter a number to take the square root of: '))
sqrt_of_y = math.sqrt(y)
print(f'The square root is: {sqrt_of_y:.3f}')
