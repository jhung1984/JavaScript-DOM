# 1.python基础

## 1.1 数据类型和变量

数据类型
* 整数
* 浮点数
* 字符串
* 布尔值
* 空值
变量

## 1.2 字符串和编码

字符编码
* ASCII 127个字符，即大小写英文字母、数字和一些符号。
* GB2312 中文简体编码
* Unicode 把所有语言都统一到一套编码里。
* UTF-8 把Unicode编码转化为“可变长编码”的UTF-8编码。

格式化
+ 占位符           替换内容
+ %d                整数
+ %f                浮点数
+ %s                字符串
+ %x                十六进制整数

例子：'Age:%s. Gender:%s' %(25,True)
     'Age:25. Gender:True'

format（）方法，它会用传入的参数依次替换字符串内的占位符。
例子：
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'

## 1.3 list和tuple

### list 
    Python内置的一种有序的集合的数据类型。
    classmates = ['Michael','Bob',Tracy']
* len（）函数可以获得list元素的个数。
* insert classmates.insert(1,'Jack')即把元素插入到指定的位置。
* append classmates.append("Adam")往list中追加元素到末尾.
* pop（） classmates.pop() 删除list末尾的元素.pop（i）删除指定位置的元素，i为索引位置。

### tuple
    另一种有序列表叫元祖。与list不同，tuple一旦初始化就不能修改。
    t = (1,2)
    注意:list是以方括号建立的列表,而tuple是以小括号建立的列表.

## 1.4 dict和set

### dict
    Python内置了字典:dict的支持,dictionary,在其他语言中也称为map,使用键-值(kye-value)存储,具有极快的查找速度.
    map = {'Michael':95,'Bob':75,'Tracy':85}
    map['Michael]
### set
    set和dict类似,也是一组key的集合,但不存储value且key不能重复.
### 1.5 函数

### 定义函数
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号，然后在缩进块中编写函数体，函数的返回值用return语句返回。
    def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
函数体内部的语句在执行时,一旦执行到return时,函数就执行完毕,并返回结果.因此,函数内部通过条件判断和循环可以实现复杂的逻辑.
如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名.
    from abstest import my_abs
    my_abs(-33)

### 空函数
* pass
pass语句定义空函数
    def nop():
        pass
pass可用来作为占位符.

* 参数检查
    def my_abs(x):
        if not isinstance(x,(int,float)):
            raise TypeError('bad operand type')
        if x >= 0:
            return x
        else:
            return -x

* 返回多个值
    import math

    def move(x,y,step,angle=0):
        nx = x + step * math.cos(angle)
        ny = y + step * math.sin(angle)
        return nx,ny

返回值是一个tuple.python的函数返回多个值就是返回一个tuple.

### 小结

定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。

### 函数的参数

#### 位置参数
    def power(x):
        return x*x

    def power(x,n):
        s = 1
        while n > 0:
            n = n -1
            s = s * x
        return s

#### 默认参数
    def power(x,n=2):
        s = 1
        while n > 0:
            n = n - 1
            s = s * x
        return s
默认参数可以简化函数的调用.默认参数必须指向不变对象！