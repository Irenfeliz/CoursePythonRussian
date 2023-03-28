s = input()
l = s.split()
count = 0

for i in range(len(l)-1):
    if int(l[i]) < int(l[i+1]):
        count += 1
print(count)