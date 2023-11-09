
1.input_string = input("Введите строку: ")

words = input_string.split()

words.reverse()

print(words)
Введите строку: Death there mirth way the noisy merit
['merit', 'noisy', 'the', 'way', 'mirth', 'there', 'Death']  

3.# Ввод списка чисел

numbers = input("Введите список чисел через пробел: ")



# Разделение строки на отдельные числа

number_list = numbers.split()



# Приведение чисел к целочисленному типу

number_list = [int(x) for x in number_list]



# Ввод степени

n = int(input("Введите степень: "))



# Возведение чисел в степень n

result = [x ** n for x in number_list]



# Вывод результата

print(result)
Введите список чисел через пробел: 3 5 -7 -13 43
Введите степень: 2
[9, 25, 49, 169, 1849]

4.text = input("Введите текст: ")

symbol = input("Введите символ: ")



doubled_text = text.replace(symbol, symbol*2)

print("Удвоенный текст:", doubled_text)
Введите текст: "Hello, world!"
Введите символ: o
Удвоенный текст: "Helloo, woorld!"

5.string = "Hello, x and y are characters."



# Подсчёт количества символов 'x' и 'y'

count_x = string.count('x')

count_y = string.count('y')



# Вывод результата

print(f'x: {count_x}, y: {count_y}')
x: 1, y: 1

6.text = input("Введите текст со скобками: ")  # Вводим строку с текстом

result = ""  # Пустая строка для хранения содержимого скобок



start = text.find("(")  # Ищем позицию открывающей скобки

while start != -1:  # Пока есть открывающая скобка

    end = text.find(")", start)  # Ищем позицию закрывающей скобки

    if end != -1:  # Если закрывающая скобка найдена

        result += text[start + 1: end] + "n"  # Добавляем содержимое скобок в результат

    else:  # Если закрывающая скобка не найдена

        break  # Завершаем цикл

    start = text.find("(", end)  # Ищем позицию следующей открывающей скобки, начиная с позиции закрывающей скобки



print(result)  # Выводим результат
Введите текст со скобками: Hello


