# create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# constructor
# numbers2 = list((1, 2, 3, 4, 5))
# print(numbers, numbers2)

print(fruits[1])  # get a value

print(len(fruits))  # length

fruits.append('Mangos')  # append the list

fruits.insert(2, 'Strawberries')  # insert into position

fruits[0] = 'Blueberries'  # change value

fruits.pop(2)  # remove the pop

fruits.reverse()  # reverse list

fruits.sort()  # sort list

fruits.sort(reverse=True)  # reverse sort

print(fruits)
