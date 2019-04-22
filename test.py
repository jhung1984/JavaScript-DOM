import random

num1 = random.randint(1,33)
print(num1)

num2 = random.randint(1,33)
while num2 == num1 :
    num2 = random.randint(1,33)
else:
    print(num2)

num3 = random.randint(1,33)
while num3 == num2 or num3 == num1:
    num3 = random.randint(1,33)
else:
    print(num3)


num4 = random.randint(1,33)
while num4 == num1 or num4 == num2 or num4 == num3:
    num4 = random.randint(1,33)
else:
    print(num4)

num5 = random.randint(1,33)
while num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
    num5 = random.randint(1,33)
else:
    print(num5)

num6 = random.randint(1,33)
while num6 == num1 or num6 == num2 or num6 == num3 or num6 == num4 or num6 == num5:
    num6 = random.randint(1,33)
else:
    print(num6)

num7 = random.randint(1,16)
print(num7)

num_all = [num1,num2,num3,num4,num5,num6,num7]
print(num_all)
num_all.sort()
print(num_all)


