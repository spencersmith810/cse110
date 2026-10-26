#########################################################################
''' Python Basics'''
#########################################################################

# This is a line comment. The # tells my program to ignore 
# things after the # until the end of the line

''' These triple quotes tell the program to ignore everything
until there's another set of triple quotes.'''

""" I can use double or single quotes in python as long as 
I'm consistent (if I start with double I have to end with double) """

# notice the different colors VS Code uses for different things

x = 5   # this creates a variable named x and stores the int 5 in it
print(x)  # this tells the computer to display the value of x (see below)

x = 10.0  # x is now reassigned the float value 10
print(x)

x = 'bill'  # x is now assigned the string 'bill'
print(x)

name = input("enter name: ")    # name will be assigned a string
                                # input is a built-in function
                                # that always returns a string
print(name)





favNumber = int(input("What's your favorite number: "))

