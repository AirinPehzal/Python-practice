import math
word = input("Введите слово (в кириллице)\n")
if len(word)<6:
    for i in range(0, len(word)):
        print(word[i])
else:
    for i in range(0, math.floor(len(word)/2)):
        print(word[i])