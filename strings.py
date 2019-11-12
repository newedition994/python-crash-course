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

s = 'helloworld'

# Capitalize string
print(s.capitalize())

# uppercase
print(s.upper())

# lower
print(s.lower())

# swap case
print(s.swapcase())

# length
print(len(s))

# replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

print(s.startswith('hello'))  # starts with

print(s.endswith('d'))  # ends with

print(s.split())  # split into a list

print(s.find('r'))  # find position

print(s.isalnum())  # alphanumeric

print(s.isalpha())  # alphabetic

print(s.isnumeric())  # numeric
