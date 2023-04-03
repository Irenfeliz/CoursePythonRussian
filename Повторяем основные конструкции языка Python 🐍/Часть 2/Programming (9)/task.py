n = int(input())
words = [input() for _ in range(n)]
def check_word(word):
    if 'a' and 'n' and 't' and 'o' not in word:
        return ''
    index_a = word.find('a')
    letter_a = word[index_a:][0]
    index_n = word[index_a:].find('n')
    letter_n = word[index_a + index_n:][0]
    index_t = word[index_a + index_n:].find('t')
    letter_t = word[index_a + index_n + index_t:][0]
    index_o = word[index_a + index_n + index_t:].find('o')
    letter_o = word[index_a + index_n + index_t + index_o:][0]
    index_n2 = word[index_a + index_n + index_t + index_o:].find('n')
    letter_n2 = word[index_a + index_n + index_t + index_o + index_n2:][0]
    word_result = [letter_a, letter_n, letter_t, letter_o, letter_n2]
    return ''.join(word_result)
result = []

for i in words:
    s = check_word(i)
    if s == 'anton':
        result.append(words.index(i)+1)

print(*result)