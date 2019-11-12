# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# constructor
# person2 = dict(first_name='Sara', last_name='Willams')
# print(person2, person, type(person2))

# Get Value
print(person['first_name'])
print(person.get('last_name'))

person['phone'] = '555-555-5555'  # add key/value
print(person)

print(person.keys())  # get dict keys

print(person.items())  # get dict items

person2 = person.copy()  # copy dict
person2['city'] = 'Boston'

del(person['age'])  # remove item
person.pop('phone')

person.clear()  # clear

print(len(person2))  # get length

# list of dict
people = [
    {'name': 'Maria', 'age': 54},
    {'name': 'Kenneth', 'age': 63}
]

print(people[1]['name'])
