'''
Week 8: For loops
Sister Bingham
'''

# 1) loop to print 1 through 5 (using a for loop with range)
for i in range(1,6):
    print(i)
# 2) loop to print "Hello World" a user specified number of times
k = int(input("give me a number: "))
for j in range(k):
    print("Hello World")

# 3) loop to print each letter in a string - two ways: for i in string, for i in range(len(string))
name = 'Spencer'
for l in name:
    print(l)

# 4) loop to print each item in a list
my_list = [1,3,5,7,9]
for m in my_list:
    print(m)

# team activity - looping through strings







#### for day 2
# # variation on a prep material example
# first_name = "Brigham"
# last_name = "Younger"

# # use range and len to loop through the string
# for i in range(len(first_name)):
#     print(f"The letter {first_name[i]} is at position {i} in the first name")
#     print(f"The letter {last_name[i]} is at position {i} in the last name")
#     # we could also use if statements to check if the letters are the same



#### Questions we need to answer in order to do the Wordle Hints
# # How do I compare the letter in one word to the letter in another word at the same position?
# # How do I find out if a letter exists in a different word
