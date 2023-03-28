s = input()
l = s.split()
result = []

for i in range(0,len(l),2):
    l1 = l[i:i+2]
    l1.reverse()
    result += l1
print(*result)

