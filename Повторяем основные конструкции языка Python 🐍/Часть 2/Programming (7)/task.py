# "камень", "ножницы", "бумага", "ящерица", "Спок"

# 0 -> 1, 3
# 1 -> 2, 3
# 2 -> 0, 4
# 3 -> 2, 4
# 4 -> 0, 1

timur = input()
ruslan = input()

l = ["камень", "ножницы", "бумага", "ящерица", "Спок"]

if timur == ruslan:
    print('ничья')
elif timur == l[0]:
    if ruslan == l[2] or ruslan == l[4]:
        print('Руслан')
    if ruslan == l[1] or ruslan == l[3]:
        print('Тимур')
elif timur == l[1]:
    if ruslan == l[0] or ruslan == l[4]:
        print('Руслан')
    if ruslan == l[2] or ruslan == l[3]:
        print('Тимур')
elif timur == l[2]:
    if ruslan == l[1] or ruslan == l[3]:
        print('Руслан')
    if ruslan == l[0] or ruslan == l[4]:
        print('Тимур')
elif timur == l[3]:
    if ruslan == l[0] or ruslan == l[1]:
        print('Руслан')
    if ruslan == l[2] or ruslan == l[4]:
        print('Тимур')
elif timur == l[4]:
    if ruslan == l[2] or ruslan == l[3]:
        print('Руслан')
    if ruslan == l[0] or ruslan == l[1]:
        print('Тимур')

