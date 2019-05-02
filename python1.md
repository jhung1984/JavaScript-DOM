# python

## 数字

### 数字类型

python数字类型的完整工具包括:

* 整数和浮点数
* 复述
* 固定精度的十进制数
* 有理分数
* 集合
* 布尔类型
* 无穷的整数精度
* 各种数字内置函数和模块
  
### 内置数学工具和扩展

表达式操作符及程序

* yield x                     生成器函数发送协议
* lambda args: expression     生成匿名函数
* x if y else z               三元选择表达式
* x or y                      逻辑或(只有x为假,才会计算y)
* x and y                     逻辑与(只有x为真,才会计算y)
* not x                       逻辑非
* x in y,x not in y           成员关系(可迭代对象,集合)
* x is y,x is not y           对象实体测试
* x<y,x<=y,x>y,x>=y           大小比较,集合子集和超集值和相等性操作符
* x == y,x != y
* x | y                       位或,集合并集
* x ^ y                       位异或,集合对称差
* x & y                       位与,集合交集
* x<<y,x>>y                   左移或右移y位
* x+y,x-y                     加法/合并,减法,集合差集
* x*y,x%y,x/y,x//y            乘法/重复,余数/格式化,除法,真除法或floor除法
* -x,+x                       一元减法,识别
* ~x                          按位求补(取反)
* x**y                        幂运算
* x[i]                        索引(序列,映射及其他)点号取属性运算,函数调用
* x[i:j:k]                    分片
* x(...)                      调用(函数,方法,类及其他可调用的)
* x.attr                      属性引用
* (...)                       元组,表达式,生成器表达式
* [...]                       列表,列表解析
* {...}                       字典,集合,集合和字典解析

### 变量和基本的表达式

* 变量在它第一次赋值时创建.
* 变凉在表达式中试用将被替换为它们的值.
* 变量在表达式中试用以前必须已赋值.
* 变量像对象一样不需要再一开始运行声明.

### 十六进制,八进制和二进制

* oct函数会将十进制转换为八进制.
* hex函数会将十进制转换为十六进制.
* bin函数会将十进制转换为二进制.
* int('64'),int('100',8),int('40',16),int('1000000',2)打印后将变成(64,64,64,64)
* int('0x40',16),int('0b1000000',2)打印后将变成(64,64)
* eval函数将字符串转换为十进制:eval('64'),eval('0o100'),eval('0x40'),eval('0b1000000')
* 利用字符串格式化方法调用和表达式:'{0:o},{1:x},{2:b}'.format(64,64,64)}打印后变成'100,40,1000000'另一个例子:'%0,%x' %(64,255)

### 位操作

### 其他的内置数学工具

三种方法计算平方根:

    import math
    math.sqrt(144)
    144 ** .5
    pow(144, .5)

### 其他数字类型

#### 小数位

    from decimal import Decimal
    Decimal（'0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30')
    Decimal('0.00')

小数位的全局精度

    import decimal
    decimal.getcontext().prec = 4

小数位的临时精度

    import decimal
    with decimal.localcontext() as ctx:
        ctx.prec = 2

#### 分数类型

    from fractions import Fraction
    x = Fraction(1,3)
    Fraction('.25')
    Fraction(1,4)

## 字符串

### 常见字符串常量和表达式

* 操作                                    解释
* s = ''                                空字符串
* s = "spanm's"                         双引号和单引号相同
* s = 's\np\ta\x00m'                    转义序列
* s = """..."""                         三重引号字符串块
* s = r'\temp\spam'                     Raw字符串
* s = b'spam'                           python3.0中的字节字符串
* s = u'spam'                           仅在python2.6中使用的Unicode字符串
* s1 + s2                               合并
* print('-' * 80)                       重复
* s[i]                                  索引
* s[i:j:k]                              分片:索引x对象中的元素,从偏移位i直到偏移为j-1,每隔k元素索引一次
* len(s)                                求长度
* "a %s parrot" % kind                  字符串格式化表达式
* "a {0} parrot".format(kind)           python2.6和python3.0中的字符串格式化方法
* s.find('pa')                          字符串方法调用:搜索
* s.rstrip()                            移除空格
* s.replace('pa','xx')                  替换
* s.split(',')                          用展位符分隔
* s.isdigit()                           内容测试
* s.lower()                             短信息转换
* s.endswith('spam')                    结束测试
* 'spam'.join(strlist)                  嵌入分隔符
* s.encode('latin-1')                   Unicode编码等
* for x in s: print(x)                  迭代
* 'spam' in s                           成员关系
* [c * 2 for c in s]                    列表解析

### 字符串反斜杠字符

* \newline                              忽视(连续)
* \\                                    反斜杠(保留\)
* \'                                    单引号(保留')
* \"                                    双引号(保留")
* \a                                    响铃
* \b                                    倒退
* \f                                    换页
* \n                                    换行
* \r                                    返回
* \t                                    水平制表符
* \v                                    垂直制表符
* \N{id}                                Unicode数据库ID
* \uhhhh                                Unicode16位的十六进制值
* \uhhhhhhh                             Unicode32位的十六进制值
* \xhh                                  十六进制值
* \ooo                                  八进制值
* \0                                    Null(不是字符串结尾)
* \other                                不转义(保留)

### 字符串转换工具

    str(32)
    ord('s')    转换为ASCII码
    chr（115）  转换为字符串

### 字符串方法

1. 大小写转换
    * s.lower() 返回s字符串的小写格式
    * s.upper() 返回s字符串的大写格式
    * s.title() 返回s字符串中所有单词首字母大写且其他字母小写的格式
    * s.capitalize() 返回s字符串首字母大写,其他字幕小写的心字符串.
    * s.swapcase() 对s中的所有字符串做大小写转换

2. isXXX判断
    * s.isdecimal() 测试字符串s是否为分数.
    * s.isdigit() 测试字符串s是否为字母.
    * s.isnumeric() 测试字符串s是否只为数字组成.
    * s.sialpha() 测试字符串s是否只为字母组成.
    * s.isalnum() 测试字符串s是否由字母和数字组成.
    * s.islower() 判断是否是小写
    * s.isupper() 判断是否为大写
    * s.istitle() 判断是否为首字母大写
    * s.isspace() 判断是否是空白(空格,制表符,换行符)
    * s.isprintable() 判断是否为打印字符(制表符,换行符不是打印字符)
    * s.isdentifier() 判断是否满足标识符定义规则

3. 填充
    * s.center(width[,fillchar]) 将字符串居中,左右两边使用fillchar进行填充,使得整个字符串的长度为width.fillchar默认为空格.