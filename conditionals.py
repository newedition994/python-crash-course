# if/ else conditions are used to decide to do something based on something being true or false

x = 21
y = 20

# comparison operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    print(f'{x} is greater than {y}')  # simple if

if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')  # if/else

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')  # elif => else if

if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')  # Nested if

# logical  operators (and or, not) - Used to combine conditional statements

if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')  # and

if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')  # or

if not(x == y):
    print(f'{x} is not equal to {y}')  # not

# Membershipt Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4, 5]

if x in numbers:
    print(x in numbers)  # in

if x not in numbers:
    print(x not in numbers)  # not in

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

if x is y:
    print(x is y)  # is

if x is not y:
    print(x is not y)
