# -*- coding: UTF-8 -*-

import random

# num1 = random.randint(1,33)

# num2 = random.randint(1,33)
# while num2 == num1 :
#     num2 = random.randint(1,33)

# num3 = random.randint(1,33)
# while num3 == num2 or num3 == num1:
#     num3 = random.randint(1,33)

# num4 = random.randint(1,33)
# while num4 == num1 or num4 == num2 or num4 == num3:
#     num4 = random.randint(1,33)

# num5 = random.randint(1,33)
# while num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
#     num5 = random.randint(1,33)

# num6 = random.randint(1,33)
# while num6 == num1 or num6 == num2 or num6 == num3 or num6 == num4 or num6 == num5:
#     num6 = random.randint(1,33)

# num_6 = [num1,num2,num3,num4,num5,num6]
# num_6.sort()

# num7 = random.randint(1,16)

# num_all = num_6 + list([num7])

import random

num1 = []
count = 0
n = 0
L = []

while n < 3:
    T =[]
    while num1 != 1:
        num1 = random.randint(1,33)
        count += 1
        print(count)
    else:
        T.append(count)
    
    n += 1

L.extend(T)
print('count:',count,'\n','num1:',num1,'\n','n:',n,'\n','L:',L)
