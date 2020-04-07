# Python打印矩形-直角三角形-等腰三角形-菱形

> https://www.cnblogs.com/qiuxirufeng/p/9650437.html

## **思路如下：**

### （1）先打印一个星号并换行

　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915102337152-2040073164.png)

```python
print("*")
```

### （2）打印一行6列星号

　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915102524479-878808777.png)

```python
for i in range(6):
    print("*", end=" ")
```

### （3）打印6行一列星号

　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915102647597-708978260.png)

```python
for i in range(6):
    print("*")
```

###（4）打印6行6列矩形

　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915102814025-1526777000.png)

```python
for i in range(6):
    for j in range(6):
        print("*",end=" ")　　# 每打印一行就换行
    print()
```

### （5）打印直角三角形

金字塔型是由下面直角三角形转成的，先打印此图形

　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915103040615-1529829536.png)

控制内层循环的打印。观察上图，发现如下规律：

　　　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915103249001-1105272085.png)

则让内层循环 j<=i，就可以实现。i 控制行数，j 控制列数。比如：当 i=0 时，内层循环1次，j=0，j<=i，当 j++ 时，就跳出内层循环；当 i=1 时，内存循环2次，j=0 和 j=1 的情况，当 j=1，j++，则 j=2，j<=i 则不成立，跳出内存循环。以此类推。

```python
for i in range(6):
    for j in range(i+1):
        print("*",end=" ")
    print()
```

### （6）当 j<i，那么每行少一个星号，则第一行会被抹掉，如下图所示：

　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915103730271-709401219.png)

```python
for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()
```

### （7）空格和星号相结合的情况，完整金字塔就是被空格顶过去的。

　　打印6个空格，后跟星号

　　　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915104036299-1074620632.png)

```python
for i in range(6):
    print(" ", end=" ")
print("*")
```

　　每行5个空格，后跟一个星号

　　　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915104323279-1997210245.png)

```python
for i in range(6):
    for k in range(5):
        print(" ", end=" ")
    print("*")
```

有了以上的基础，下面分析打印完整金字塔型：

### （8）打印金字塔型-准备

根据下图所示，我们已经可以打印出左边的图形，然后通过控制空格，把它转成右边的图形。

　　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915105128272-1070089212.png)   ![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915105347509-1619432342.png)

　　观察后发现如下规律，右边图形相对于左边的图形。行数仍然是6行，即 i=6，先不考虑空格的问题，每一行星星的个数，如下所示：

　　　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915105549473-321234347.png)

　　可以得出：j<=(2*i)。当i=0时，j=0，打印一个星号，必须j<=，参考上面的讲解；当i=1时，j=2，因为是j<=i，j取值0，1，2，循环三次，打印3个星号。以此类推。

　　　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915112108900-2081541136.png)

```python
for i in range(6):
    for j in range(2*i+1):
        print("*",end=" ")
    print()
```

### （9）打印金字塔型-空格插入

在（8）的基础上，插入空格。对比发现，如下规律：

　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915112620145-1742374751.png)

　　再加一层内循环，在星号内循环的前面，先打印空格，然后再打印相应的星号。

　　可以得出：k<6-i-1；当 i=0 时，k<5，k取值0，1，2，3，4，循环5次，打印5个空格。依次类推。

　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915112823956-1229509285.png)

```python
for i in range(6):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()
```

### （10）菱形的下半部分

菱形的上半部分已经打印出，下面考虑如何打印下半部分，最上面的11个星号，已经在上半部分给出，只考虑打印11个星号以下的图形。如图：

　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915114132805-1290047688.png)

　　观察发现，下半部分共5行，即 i=5 。有如下的规律，如下图所示：

　　　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915113424726-1907052784.png)

　　空格内存循环，k<i+1，星号内层循环，m<(9-3*i)+i。

　　(9-3*i)+i，是如何得出？通过数学归纳法，发现：

　　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915115552285-1738125764.png)

```python
for i in range(5):
    for k in range(i+1):
        print(" ", end=" ")
    for m in range((9-3*i)+i):
        print("*",end=" ")
    print()
```

### （11）打印出完整的菱形

通过（10）和（11），我们已经可以打印出完整的菱形。

　　![img](https://img2018.cnblogs.com/blog/1330952/201809/1330952-20180915114315625-426725492.png)

```python
for i in range(6):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()
for i in range(5):
    for k in range(i+1):
        print(" ", end=" ")
    for m in range((9-3*i)+i):
        print("*",end=" ")
    print()
```



作者：[ 湫兮](http://blog.esofar.cn/)

出处：https://www.cnblogs.com/qiuxirufeng/p/9650437.html

本站使用「[CC BY 4.0](https://creativecommons.org/licenses/by/4.0)」创作共享协议，转载请在文章明显位置注明作者及出处。