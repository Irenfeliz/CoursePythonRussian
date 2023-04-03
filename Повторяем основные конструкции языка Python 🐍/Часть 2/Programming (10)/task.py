word = input() + ' запретил букву'
# chr(1072): chr(1103)
alphabet = [chr(i) for i in range(1072, 1104)]
# print(alphabet)

for i in alphabet:
    if i in word:
        print(word.strip() + ' ' + i)
        word = word.replace(i, '')
        if '  ' in word:
            word = word.replace('  ', ' ')

