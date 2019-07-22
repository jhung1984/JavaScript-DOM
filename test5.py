# -*- coding: UTF-8 -*-


import random

data = {'1':260,'2':239,'3':257,'4':221,'5':253,
'6':251,'7':263,'8':229,'9':235,'10':247,'11':250,
'12':236,'13':249,'14':253,'15':225,'16':199,'17':232,
'18':254,'19':262,'20':240,'21':230,'22':283,'23':259,
'24':247,'25':250,'26':229,'27':246,'28':240,'29':342,
'30':310,'31':288,'32':314,'33':336,'34':285,'35':311}

data_1 = {'1':280,'2':298,'3':299,'4':292,'5':317,
'6':284,'7':302,'8':286,'9':296,'10':332,'11':309,
'12':313}
# 更新到19073期

def random_weight(data):
    total = sum(data.values())
    ra = random.randint(1,total)
    curr_sum = 0
    ret = None
    keys = data.keys()
    
    for k in keys:
        curr_sum += data[k]
        if ra <= curr_sum:
            ret = k
            break
    return ret

num1 = random_weight(data)

num2 = random_weight(data)
while num2 == num1 :
    num2 = random_weight(data)

num3 = random_weight(data)
while num3 == num2 or num3 == num1:
    num3 = random_weight(data)

num4 =random_weight(data)
while num4 == num1 or num4 == num2 or num4 == num3:
    num4 = random_weight(data)

num5 = random_weight(data)
while num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
    num5 = random_weight(data)



num_5 = []
num_5.append(int(num1))
num_5.append(int(num2))
num_5.append(int(num3))
num_5.append(int(num4))
num_5.append(int(num5))


num_5.sort()
num6 = random_weight(data_1)
num7 = random_weight(data_1)
while num7 == num6:
    num7 = random_weight(data_1)
num_2 = []
num_2.append(int(num6))
num_2.append(int(num7))
num_2.sort()

num_5.extend(num_2)
num_all = num_5
f = open("out1.py","a")
print(num_all,',',file=f)





