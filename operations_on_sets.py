import array as arr
set_1 = {'apple', 'bannana', 'orange', 'blueberry', 'mango'}
set_2 = {'mango', 'passionfruit', 'dragon fruit', 'kiwi'}
print(set_1)
print(set_2)

set_1.add('watermelon')
print(set_1)

set_2.add('pomegranate')
print(set_2)

print(set_1.intersection(set_2))

numbers = arr.array ('i',[1, 2, 3, 4, 5])
fruits = ['apple', 'bannana', 'orange', 'blueberry', 'mango']
numbers.insert(1,5)
print(numbers)
numbers.append(6)
print(numbers)
print(numbers.count(4))