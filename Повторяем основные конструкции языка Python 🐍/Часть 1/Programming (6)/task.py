n = int(input())
l = []

while n > 0:
    s = str(n)
    if len(s) > 2:
        str1 = s[len(s)-3:len(s)]
        l.append(str1)
    else:
        l.append(s)
    n = n // 1000

l.reverse()
print(','.join(l))