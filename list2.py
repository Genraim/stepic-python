__author__ = 'genraim'
a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
else:
    for n in range(len(a)):
        print((a[n-1] + a[(n+1) % len(a)]), end=' ')