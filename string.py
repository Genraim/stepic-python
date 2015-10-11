__author__ = 'genraim'
str = input()
len = len(str)
str = str.lower()
count = str.count('g') + str.count('c')
print((count/len)*100)