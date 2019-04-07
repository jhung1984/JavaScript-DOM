print('''line1
line2
line3''')

a = 'ABC'
b = a
a = 'XYZ'
print(b)

'Age:%s. Gender:%s' %(25,True)

age = 3
if age >= 18:
    print('adult')
elif age >=6:
    print('teenager')
else:
    print('kid')

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n +1
    if n % 2 == 0:
        continue
    print(n)

a = 'abc'
b = a.replace('a','A')
print(b)

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

import math
def quadratic(a,b,c):
    a * math.sqrt(x) + b * x + c = 0
    return x

def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(4,3))

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end([66]))