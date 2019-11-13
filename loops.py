people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
    print(f'Current Person: {person}')

# Break
for person in people:
    if person == 'Sara':
        break
    print(f'Current Person: {person}')

# continue
for person in people:
    if person == 'Sara':
        continue
    print(f'Current Person: {person}')

for i in range(len(people)):
    print(people[i])  # range

for i in range(0, 11):
    print(f'Number: {i}')  # range

# while loops execute a set of statements as long as a condition is true
count = 0
while count < 10:
    print(f'Count: {count}')
    count += 1
