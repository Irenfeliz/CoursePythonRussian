count = int(input())
answer = []
def quadrant(x, y):

    if x > 0 and y > 0:
        return 'q1'
    elif x < 0 and y > 0:
        return 'q2'
    elif x < 0 and y < 0:
        return 'q3'
    elif x > 0 and y < 0:
        return 'q4'


for i in range(count):
    punto = input()
    l = punto.split()
    x = int(l[0])
    y = int(l[1])
    answer += [quadrant(x,y)]

print('Первая четверть:', answer.count('q1'))
print('Вторая четверть:', answer.count('q2'))
print('Третья четверть:', answer.count('q3'))
print('Четвертая четверть:', answer.count('q4'))









