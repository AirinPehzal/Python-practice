word = input("Введите слово (в кириллице)\n")
if (word[1] == 'к') or (word[1] == 'и') or (word[1] == 'л'):
    for i in range(1, len(word), 2):
        print(word[i])
else:
    for i in range(0, len(word), 2):
        print(word[i])