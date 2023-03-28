s = input()
l = s.split()
result = l[-1] + ' ' + ' '.join(l[:-1])
print(result)