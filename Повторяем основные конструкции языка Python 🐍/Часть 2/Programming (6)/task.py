# "камень", "ножницы" или "бумага"

timur = input()
ruslan = input()

if ruslan == timur == 'камень' or ruslan == timur == 'ножницы'or ruslan == timur == 'бумага':
    print('ничья')
elif (ruslan == 'ножницы' and timur == 'бумага') or (ruslan == 'бумага' and timur == 'камень') or (ruslan == 'камень' and timur == 'ножницы'):
    print('Руслан')
else:
    print('Тимур')