n = int(input())

l = [i for i in str(n)]

if len(l) == 6:
    print(int(l[0]+''.join(l[5:0:-1])))
if len(l) == 5:
    l.reverse()
    print(int(''.join(l)))