# Вводится строка, вывести True если строка является палиндромом и False если строка не является палиндромом,
# без учета регистра и пробелов

string = input()
string = string.replace(' ','').lower()
# удаление пробелов и перевод букв в нижний регистр
symbol = string[::-1]
print(string == symbol)