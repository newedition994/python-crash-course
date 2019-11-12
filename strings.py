# String in python are surround by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-strings
print(f'Hello, my name is {name} and I am {age}')

# String Methods
