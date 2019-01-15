word = input("Введите слово (в кириллице)\n")
if (word[0].lower() == 'а') or (word[0].lower() == 'э') or (word[0].lower() == 'е') or (word[0].lower() == 'я'):
    for i in range(0, len(word), 1):
        print(word[i])
else:
    for i in range(len(word)-1, -1, -1):
        print(word[i])