'''
Week 5: Decisions (if)
Sis Bingham
'''

'''
SYNTAX of an if statement...

if condition1:
    # code block to execute if condition1 is True
elif condition2:
    # code block to execute if condition2 is True (condition1 must be False)
else:
    # code block to execute if none of the conditions were True


condition - an expression that results in True or False (anything not 0 is True)
	a condition that results in 0 will be interpreted as False
	a condition that results in anything other than 0 will be interpreted as True

a variable can also have a value of True or False, this is called a Boolean variable (more in next week's material)

Operators used to create conditions
Math	English	                    Python	    Example
=	    Equals	                    ==	        state == "Idaho"
≠	    Not Equals	                !=	        choice != "yes"
<	    Less than	                <	        price < 1
≤	    Less than or equal to	    <=	        cost <= money_left
>	    Greater than	            >	        age > 65
≥	    Greater than or equal to	>=	        grade >= 90
'''


# decisions, decisions, decisions
a = 2
b = 3
is_valid = True  # boolean


if a == b:
    print('a == b') 
# elif a != b:    # elif isn't required, use if needed
#     print('a != b')
# elif a < b:     # conditions are checked in order, top down
#     print('a < b') # but the if is exited once a true condition is found
# elif a <= b:
#     print('a <= b')
# elif a > b:
#     print('a > b')
# elif a >= b:
#     print('a >= b')
# else:     # else isn't required, use if needed
#     print('none of the conditions were true')

print("\n  outside of the if now")

# new if statement with complex conditions (and, or)
# if a > b and a == b:
#     print('and is true')

# you can check the result of conditions with a print
# print(a > b and a == b)

# can we compare strings like this
# print('cat' > 'bob')

# if a > b and a == b:
#     print('and is true')
# else:
#     print('and isn\'t true')
