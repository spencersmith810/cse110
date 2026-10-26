'''
Week 2: More variables, input, and output
Sister Hansen
What kind of comment is this? - multi-line-comment
'''

#### variables (and good names) - What kind of comment is this? - line-comments
# create a string variable
dog_name = 'churro'
# create an integer variable
num_int = 10
# create a float variable
num_float = 5.0
#### input
# get input from the user and store it in a variable
dog_name = input('What is your dogs name: ') # input always returns a string

# get a number from the user (decide if you want to convert now or later)
fav_num = input("what is your favorite number: ")
print(fav_num)
print(fav_num * 3)
fav_num_float = float(fav_num) # converting the string to a float
print(fav_num * 3)

#### output and f-strings
# output all the variables with a single print statement
print(dog_name, fav_num, num_int, num_float, 3, "hi")
# now use an f-string to output all the variables
cool_string = f"Hi {dog_name}, I hear your favorite number is {fav_num_float}"
print(cool_string)

# output all the variables again, but use a string method on one 
# so that it prints in upper case, lower case, or title case
print(f"Hi {dog_name.capitalize()}, I hear your favorite number is {fav_num_float}.")