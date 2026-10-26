'''
Week 6: Decisions (and Booleans and complex conditions)
Sis Bingham
'''

credits = 110
gpa = 2.0

#### Boolean variables can be assigned directly
can_graduate = False  # should be True or False to be a boolean

# write an expression to determine what the value of can_graduate
# should be if you can graduate if you have 120+ credits and a gpa above 2.0
can_graduate = None  # replace None with a condition (or complex condition)
print(can_graduate)

# Note: a good boolean variable name will indicate that it only has two possible values (T/F)

#### Logical operators (and, or, not) and complex conditions
# be careful with complex conditions (ones with and/or)
x = 4
y = x == 5 or 2  # this doesn't work the way you might think it will
# print(f'{y=}')
y = x == 5 or x == 2  # this works!
# print(f'{y=}')


# logical operators (not, and, or ) have an order of operations too 

# order of operations (highest to lowest):
# PEMDAS (math)
# all conditional operators (==, !=, >, <, >=, <=)
# not
# and
# or

# meal = "sandwich"
# money = 0

# if meal == "sandwich" or meal == "pizza slice" and money > 5:
# 	print("Your order will be ready in 5 minutes.")
# else:
#     print("Sorry, can't complete your order.")


















'''
D&C 122:5-7

5 If thou art called to pass through tribulation; if thou art in perils among false brethren; if thou art in perils among robbers; if thou art in perils by land or by sea;

6 If thou art accused with all manner of false accusations; if thine enemies fall upon thee; if they tear thee from the society of thy father and mother and brethren and sisters; and if with a drawn sword thine enemies tear thee from the bosom of thy wife, and of thine offspring, and thine elder son, although but six years of age, shall cling to thy garments, and shall say, My father, my father, why can’t you stay with us? O, my father, what are the men going to do with you? and if then he shall be thrust from thee by the sword, and thou be dragged to prison, and thine enemies prowl around thee like wolves for the blood of the lamb;

7 And if thou shouldst be cast into the pit, or into the hands of murderers, and the sentence of death passed upon thee; if thou be cast into the deep; if the billowing surge conspire against thee; if fierce winds become thine enemy; if the heavens gather blackness, and all the elements combine to hedge up the way; and above all, if the very jaws of hell shall gape open the mouth wide after thee, know thou, my son, that all these things shall give thee experience, and shall be for thy good.
'''













tribulation = True
perils = True
accused = True
enemies = True
family_torn = True
prison = True
pit = True
murderers = True
death_sentence = True
cast_deep = True
surge = True
wind = True
heavens_black = True
hedge = True
hells_jaws = True

if tribulation or perils or accused or enemies or family_torn or prison or pit or murderers or death_sentence or cast_deep or surge or wind or heavens_black or hedge or hells_jaws:
    is_for_experience = True
    is_for_thy_good = True
    God_is_with_you = True 
