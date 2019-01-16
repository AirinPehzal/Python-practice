word = input("Введите слово (в кириллице)\n")
for i in range(0, len(word)):
    if (word[i] != "п")and(word[i] != "о")and(word[i] != "и"):
      if (i % 2 == 1):
          print(word[i])
for i in range(0, len(word)-1):
    if (word[i] != "п")and(word[i] != "о")and(word[i] != "и"):
      if (i % 2 == 0):
          print(word[i])