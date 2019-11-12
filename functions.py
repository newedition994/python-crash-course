# function is a block of code which runs when it is called

# Create function


def sayHello(name='Sam'):
    print(f'Hello {name}')

# Return values


def getSum(num1, num2):
    total = num1 + num2
    return total

# lambda function is a small anonymous function; can take any number of arguments, but can only have one expression


# getSum = lambda num1, num2 : num1 + num2


print(getSum(10, 3))
