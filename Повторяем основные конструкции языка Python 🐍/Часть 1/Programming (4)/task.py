year = int(input())

horoscope = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух',
             'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']

while year > 2011:
    year -= 12
while year < 2000:
    year += 12

print(horoscope[year % 100])
