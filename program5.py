n = input("Введите число\n")
for i in range(1, 10, 1):
    s = str(n) + " * " + str(i) + " = " + str(int(n)*i)
    print(s)