korean_snack_box_1 = {'Tteokbokki', 'Bungeoppang', 'Jajangmyeon', 'Sundubu Jjigae', 'Bungeoppang'}
korean_snack_box_2 = {'Sujeonggwa', 'Bibimbap', 'Samgyetang', 'Japchae', 'Bibimbap', 'Tteokbokki'}
print(korean_snack_box_1)
print(korean_snack_box_2)
korean_snack_box_1.add('Gimbap')
print( korean_snack_box_1)
common_food = korean_snack_box_1.intersection(korean_snack_box_2)
print(common_food)
import array as arr
count = arr.array ('i',[ 4, 6, 3, 5])
print(count)
count.insert(0, 2)
count.append(1)
print(count)
five = count.count(5)
print(five)
count.reverse()