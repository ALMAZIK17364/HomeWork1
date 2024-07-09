# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# HomeWork 0 - Строки и индексация строк

#Создаём переменную с текстом
example = "Undertale"

# Задание:
print(example[0])

print(example[-1])

print(example[4:9])

print(example[::-1])

EvSec = ""
for i in range(len(example)):
    # print(i)
    # print(EvSec)
    # print(i % 2)
    if i%2!=0:
        EvSec += example[i]

# Так как отсчёт символов начинается с 0, для результата нужно использовать символы с нечётным номером.
print(EvSec)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
