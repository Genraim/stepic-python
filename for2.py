__author__ = 'genraim'
a = int(input())
b = int(input())
s = 0
j = 0
while (a % 3 != 0):
    a += 1
for i in range (a, b+1, 3):
    s += i
    j +=1
print(s/j)