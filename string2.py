__author__ = 'genraim'
str = input()
count = 1

for i in range(1, len(str)):
    if (str[i] == str[i - 1]):
        count += 1
    else:
        print(str[i-1], count, sep='', end='')
        count = 1
print(str[-1], count, sep='', end='')
