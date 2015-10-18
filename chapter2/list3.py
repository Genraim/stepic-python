__author__ = 'genraim'
"""Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
которые повторяются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным."""
input_list = [int(i) for i in input().split()]
sort_list = sorted(input_list)
symbol = sort_list[0]
flag = False
for s in sort_list[1:]:
    if (s == symbol):
        if not flag:
            print(symbol, end=' ')
        flag = True
    else:
        symbol = s
        flag = False