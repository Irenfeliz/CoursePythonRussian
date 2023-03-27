weight, height = float(input()), float(input())

imt = weight / (height ** 2)

if imt > 25:
    print('Избыточная масса')
if 18.5 <= imt <= 25:
    print('Оптимальная масса')
if imt < 18.5:
    print('Недостаточная масса')
