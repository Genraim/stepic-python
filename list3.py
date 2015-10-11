__author__ = 'genraim'
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