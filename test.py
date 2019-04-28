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


numbers = [12,37,5,42,8,3]
even = []
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

count = 0
while(count < 9):
    print('The count is :',count)
    count += 1
print("Goodbye")

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)

i = 1
while i:
    print(i)
    i += 1
    if i > 10:
        break
n = 33
sum = 0
count = 1
while (count <= n):
    sum += count
    count += 1
print("1到 %d 之和为:%d" % (n,sum))

#!/usr/bin/python
# -*- coding:UTF-8 -*-

class Employee:
    empCount = 0

    def __init__(self, name,salary):
        self.name = name
        self.salary =salary
        Employee.empCount += 1
    
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)

emp1 = Employee("ZARA",2000)
emp2 = Employee("Manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"销毁")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1),id(pt2),id(pt3))
del pt1
del pt2
del pt3

