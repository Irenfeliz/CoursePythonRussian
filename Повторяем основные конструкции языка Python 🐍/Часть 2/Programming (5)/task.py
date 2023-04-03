l = [int(input()) for _ in range(int(input()))]
result = int(input())

flag = False
for i in l:
    for j in range(len(l)):
        if l.index(i) == j:
            continue
        if i * l[j] == result:
            flag = True
            break

if flag == True:
    print('ДА')
else:
    print('НЕТ')



