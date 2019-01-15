word = input("Введите слово (в кириллице)\n")
if (word[0] == 'а') or (word[0] == 'э') or (word[0] == 'е') or (word[0] == 'я'):
    for i in range(0, len(word), 1):
        print(word[i])
else:
    for i in range(len(word)-1, -1, -1):
        print(word[i])