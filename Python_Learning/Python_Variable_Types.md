# Python 变量类型

> <https://www.runoob.com/python/python-variable-types.html>

变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。

基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。

因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。

## 变量赋值

Python 中的变量赋值不需要类型声明。变量赋值简单粗暴不需要声明类型, 灵活多变,非常好用。

每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。

每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：

### 变量赋值实例(Python 2.0+)

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print counter
print miles
print name

# 执行以上程序会输出如下结果：
# 100
# 1000.0
# John

# 变量赋值
a = 1
b = "god"

# 字符串赋值
str = 'this is string 1'

# 列表串赋值
list = ['this', 'is', 'list', 2]

# 元组赋值
tuple = ('this', 'is', 'tuple', 3)

# 字典赋值
dict = {1:'this', 2:'is', 3:'dictionary', 4:4}
```

[运行实例 »](https://www.runoob.com/try/runcode.php?filename=demo_variable&type=python)

以上实例中，100，1000.0和"John"分别赋值给counter，miles，name变量。

## 多个变量赋值

Python允许你同时为多个变量赋值。例如：

```python
a = b = c = 1
```

以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
您也可以为多个对象指定多个变量。例如：

```python
a, b, c = 1, 2, "john"
```

以上实例，两个整型对象 1 和 2 分别分配给变量 a 和 b，字符串对象 "john" 分配给变量 c。

## 标准数据类型

在内存中存储的数据可以有多种类型。数据类型 分为数字型和非数字型。

- 数字型包括整型，长整型，浮点型，复数型；

- 非数字型包括字符串，列表，元组和字典 ；

例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。

Python 定义了一些标准类型，用于存储各种类型的数据。Python有五个标准的数据类型：

- Numbers（数字） 数字数据类是不可改变的数据类型，改变数字数据类型会分配一个新的对象。
- String（字符串） 字符串的操作有基本的功能不需要再自己进行拼接遍历的操作。字符串表示方式：str="hello,world"
- List（列表） 列表用 "[ ]" 标识类似 C 语言中的数组。列表表示方式：list=['hello',2,3,4,'world']
- Tuple（元组） 元组用 "( )" 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。tuple=('hello',2,3,4,'world')
- Dictionary（字典）字典用 "{ }" 标识。字典由索引 key 和它对应的值 value 组成。

非数字型的共同点：都可以使用切片、链接（+）、重复（*）、取值（a[]）等相关运算;

非数字型的不同点：列表 可以直接赋值，元组不可以赋值，字典按照 **dict[k]=v** 的方式赋值。

1. 截取方式相同：名称[头下标:尾下标]
2. 下标是从0开始算起，可以是正数或者负数，下标为空则表示取到头或者尾
3. 开始截取时，包含了下边界，而截取到最大范围不包括上边界。
4. 元组不能二次赋值，列表可以

## Python数字-数值

数字数据类型用于存储数值。

他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。

当你指定一个值时，Number对象就会被创建：

```python
var1 = 1
var2 = 10
```

您也可以使用del语句删除一些对象的引用。

del语句的语法是：

del var1[,var2[,var3[....,varN]]]]

您可以通过使用del语句删除单个或多个对象的引用。例如：

```python
del var
del var_a, var_b
```

Python支持四种不同的数字类型：

- int（有符号整型）
- long（长整型[也可以代表八进制和十六进制]）
- float（浮点型）
- complex（复数）

### **数值类型实例**

一些数值类型的实例：

| int    | long                  | float      | complex    |
| :----- | :-------------------- | :--------- | :--------- |
| 10     | 51924361L             | 0.0        | 3.14j      |
| 100    | -0x19323L             | 15.20      | 45.j       |
| -786   | 0122L                 | -21.9      | 9.322e-36j |
| 080    | 0xDEFABCECBDAECBFBAEl | 32.3e+18   | .876j      |
| -0490  | 535633629843L         | -90.       | -.6545+0J  |
| -0x260 | -052318172735L        | -32.54e100 | 3e+26J     |
| 0x69   | -4721885298529L       | 70.2E-12   | 4.53e-7j   |

- 长整型也可以使用小写 l，但是还是建议您使用大写 L，避免与数字 1 混淆。Python使用 L 来显示长整型。
- Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。

> **注意：**long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。

## Python字符串

字符串或串(String)是由数字、字母、下划线组成的一串字符。

一般记为 :

```python
s = "a1a2···an"
# (n>=0)
```

它是编程语言中表示文本的数据类型。

python的字串列表有2种取值顺序:

- 从左到右索引默认0开始的，最大范围是字符串长度少1
- 从右到左索引默认-1开始的，最大范围是字符串开头

![python-string-slice](F:\Github\xiangxing98.github.io\Python_Learning\python-string-slice.png)

如果你要实现从字符串中获取一段子字符串的话，可以使用 **[头下标:尾下标]** 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。

**[头下标:尾下标]** 获取的子字符串包含头下标的字符，但不包含尾下标的字符。

比如:

```python
s = 'abcdef'
s[1:5]
# 'bcde'
```

当使用以冒号分隔的字符串，python 返回一个新的对象，结果包含了以这对偏移标识的连续的内容，左边的开始是包含了下边界。

上面的结果包含了 **s[1]** 的值 b，而取到的最大范围不包括**尾下标**，就是 **s[5]** 的值 f。

![python-string-index](F:\Github\xiangxing98.github.io\Python_Learning\python-string-index.png)

加号（+）是字符串连接运算符，星号（*）是重复操作。如下实例：

### 字符串实例(Python 2.0+)

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

str = 'Hello World!'

print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第六个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

# 以上实例输出结果：
# Hello World!
# H
# llo
# llo World!
# Hello World!Hello World!
# Hello World!TEST

```

Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：

![python_list_slice_2](F:\Github\xiangxing98.github.io\Python_Learning\python_list_slice_2.png)

## Python列表

List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。

列表用 **[ ]** 标识，是 python 最通用的复合数据类型。

列表中值的切割也可以用到变量 **[头下标:尾下标]** ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

![img](F:\Github\xiangxing98.github.io\Python_Learning\list_slicing1.png)

加号 **+** 是列表连接运算符，星号 ***** 是重复操作。如下实例：

### Python列表实例(Python 2.0+)

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

# 以上实例输出结果：
# ['runoob', 786, 2.23, 'john', 70.2]
# runoob
# [786, 2.23]
# [2.23, 'john', 70.2]
# [123, 'john', 123, 'john']
# ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']

```

## Python 元组

元组是另一个数据类型，类似于 List（列表）。

元组用 **()** 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

### Python 元组实例(Python 2.0+)

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第四个（不包含）的元素
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组

# 以上实例输出结果：
# ('runoob', 786, 2.23, 'john', 70.2)
# runoob
# (786, 2.23)
# (2.23, 'john', 70.2)
# (123, 'john', 123, 'john')
# ('runoob', 786, 2.23, 'john', 70.2, 123, 'john')

```

以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的：

### 无效元组实例(Python 2.0+)

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用
```

## Python 字典

字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。

两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

### Python 字典实例(Python 2.0+)

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

# 输出结果为：
# This is one
# This is two
# {'dept': 'sales', 'code': 6734, 'name': 'john'}
# ['dept', 'code', 'name']
# ['sales', 6734, 'john']

```

## type() 、isinstance()查看该变量的数据类型

python 的所有数据类型都是类,可以通过 type() 查看该变量的数据类型:

```python
n=1
type(n)
# <type 'int'>

n="runoob"
type(n)
# <type 'str'>

# 此外还可以用 isinstance 来判断：
a = 111
isinstance(a, int)
# True
```

isinstance 和 type 的区别在于：

```python
class A:
 pass

class B(A):
 pass

isinstance(A(), A)
# True

type(A()) == A
# False

isinstance(B(), A)
# True

type(B()) == A
# False
```

区别就是:

- type()不会认为子类是一种父类类型。
- isinstance()会认为子类是一种父类类型。

## Python数据类型转换

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

| 函数                                                         | 描述                                                |
| :----------------------------------------------------------- | :-------------------------------------------------- |
| [int\(x [,base])](https://www.runoob.com/python/python-func-int.html) | 将x转换为一个整数                                   |
| [long(x [,base] )](https://www.runoob.com/python/python-func-long.html) | 将x转换为一个长整数                                 |
| [float(x)](https://www.runoob.com/python/python-func-float.html) | 将x转换到一个浮点数                                 |
| [complex(real [,imag])](https://www.runoob.com/python/python-func-complex.html) | 创建一个复数                                        |
| [str(x)](https://www.runoob.com/python/python-func-str.html) | 将对象 x 转换为字符串                               |
| [repr(x)](https://www.runoob.com/python/python-func-repr.html) | 将对象 x 转换为表达式字符串                         |
| [eval(str)](https://www.runoob.com/python/python-func-eval.html) | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| [tuple(s)](https://www.runoob.com/python/att-tuple-tuple.html) | 将序列 s 转换为一个元组                             |
| [list(s)](https://www.runoob.com/python/att-list-list.html)  | 将序列 s 转换为一个列表                             |
| [set(s)](https://www.runoob.com/python/python-func-set.html) | 转换为可变集合                                      |
| [dict(d)](https://www.runoob.com/python/python-func-dict.html) | 创建一个字典。d 必须是一个序列 (key,value)元组。    |
| [frozenset(s)](https://www.runoob.com/python/python-func-frozenset.html) | 转换为不可变集合                                    |
| [chr(x)](https://www.runoob.com/python/python-func-chr.html) | 将一个整数转换为一个字符                            |
| [unichr(x)](https://www.runoob.com/python/python-func-unichr.html) | 将一个整数转换为Unicode字符                         |
| [ord(x)](https://www.runoob.com/python/python-func-ord.html) | 将一个字符转换为它的整数值                          |
| [hex(x)](https://www.runoob.com/python/python-func-hex.html) | 将一个整数转换为一个十六进制字符串                  |
| [oct(x)](https://www.runoob.com/python/python-func-oct.html) | 将一个整数转换为一个八进制字符串                    |
