s = input()
count = 0
result = []
for i in s:
    if i == 'Р':
        count += 1
    elif i == 'О':
        count = 0
    result.append(count)

print(max(result))
