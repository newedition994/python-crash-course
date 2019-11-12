# create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# use a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
# print(fruits, fruits2, type(fruits2))

fruits2 = ('Apples',)  # single value needs trailing comma

print(fruits[1])  # get value

# fruits[0] = 'Pears'  # can't change value

del fruits2  # delete tuple

print(len(fruits))  # get length

# create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

print('Apples' in fruits_set)  # check if in set

fruits_set.add('Grape')  # add to set

fruits_set.remove('Grape')  # remove from set

fruits_set.add('Apples')  # add duplicate

fruits_set.clear()  # clear set

# del fruits_set  # delete

print(fruits_set)
