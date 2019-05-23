# -*- coding: UTF-8 -*-

# import random

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

# import random

# num1 = []
# n = 0
# L = []

# while n < 2500:
#     num1 = 0
#     count = 0
#     while num1 != 3:
#         num1 = random.randint(1,33)
#         count += 1
#     L.append(count)
#     n += 1

# b = len(L)
# a = 0

# for value in L:
#     a = a + value

# c = a / b

# print(c)

# 1出现的几率为 473/2400
# 2出现的几率为 73/2400
# 3出现的几率为 134/2400
# 4出现的几率为 174/2400
# 5出现的几率为 229/2400
# 6出现的几率为 273/2400
# 7出现的几率为 319/2400
# 8出现的几率为 343/2400
#9出现的几率为 313/2400
#10出现的几率为373/2400
#11出现的几率为373
#12出现的几率为389
#13出现的几率为408
#14出现的几率为448
#15出现的几率为390
#16出现的几率为414
#17出现的几率为447
#18出现的几率为454
#19出现的几率为436
#20出现的几率为462
#21出现的几率为422
#22出现的几率为465
#23出现的几率为426
#24出现的几率为394
#25出现的几率为435
#26出现的几率为466
#27出现的几率为439
#28出现的几率为406
#29出现的几率为417
#30出现的几率为437
#31出现的几率为413
#32出现的几率为455
#33出现的几率为373

import random

data = {'1':473/2400,'2':73/2400,'3':134/2400,'4':174/2400,'5':229/2400,
'6':273/2400,'7':319/2400,'8':343/2400,'9':313/2400,'10':373/2400,'11':373/2400,
'12':389/2400,'13':408/2400,'14':448/2400,'15':390/2400,'16':414/2400,'17':447/2400,
'18':454/2400,'19':436/2400,'20':462/2400,'21':422/2400,'22':465/2400,'23':426/2400,
'24':394/2400,'25':435/2400,'26':466/2400,'27':439/2400,'28':406/2400,'29':417/2400,
'30':437/2400,'31':413/2400,'32':455/2400,'33':373/2400}

def random_weight(data):
    total = sum(data.values())
    ra = random.uniform(0,total)
    curr_sum = 0
    ret = None
    keys = data.keys()
    
    for k in keys:
        curr_sum += data[k]
        if ra <= curr_sum:
            ret = k
            break
    return ret

slice = [random_weight(data),random_weight(data),random_weight(data),random_weight(data),random_weight(data),random_weight(data)]
print(random.sample(data,5))
