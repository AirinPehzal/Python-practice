line = "abcdefghijklmnopqrstuvwxyz"
Bline = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
stroka = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
Bstroka = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
word = input('Введите слово\n')
novword = ""
for i in range(0, len(word)):
    if line.find(word[i].lower()) != -1:
        if line.find(word[i]) != -1:
            if word[i] == "z":
                novword = novword + 'a'
            else:
                novword = novword + line[line.find(word[i])+1]
        else:
            if word[i] == "Z":
                novword = novword + 'A'
            else:
                novword = novword + Bline[Bline.find(word[i])+1]
    else:
        if stroka.find(word[i]) != -1:
            if word[i] == "я":
                novword = novword + 'а'
            else:
                novword = novword + stroka[stroka.find(word[i])+1]
        else:
            if word[i] == "Я":
                novword = novword + 'А'
            else:
                novword = novword + Bstroka[Bstroka.find(word[i])+1]
print(novword)