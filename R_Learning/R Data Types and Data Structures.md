# R语言数据类型与数据结构-R Data Types and Data Structures

> [yiibai.com/R语言教程](http://www.yiibai.com/r/r_data_types.html#article-start)

通常，在使用任何编程语言进行编程时，需要使用各种变量来存储各种信息。变量只不过是保存存储值的内存位置。 这意味着，当您创建变量时，可以在内存中保留一些空间用来存储某些值。

可能希望存储各种数据类型的信息，如字符，宽字符，整数，浮点，双浮点，布尔等。根据变量的数据类型，操作系统会分配内存并决定在保留这些内存。

*R*语言与其他编程语言(如[C语言](http://www.yiibai.com/cprogramming/)和[Java](http://www.yiibai.com/java/))相反，变量不会被声明为某些数据类型。 变量被分配给*R*对象，并且*R*对象的数据类型转变为变量的数据类型。 有很多类型的*R*对象。 常用*R*对象是 -

- 向量
- 列表
- 矩阵
- 数组
- 因子
- 数据帧

这些对象中最简单的是向量对象，并且向量对象有六种数据类型的原子向量，也称为六类向量。 其他*R*对象是建立在原子向量之上的。六类向量类型如下表所示 -

| 数据类型 | 示例                              | 验证代码                                     | 输出结果              |
| ---- | ------------------------------- | ---------------------------------------- | ----------------- |
| 逻辑   | TRUE, FALSE                     | `v <- TRUE ; print(class(v));`           | `[1] "logical"`   |
| 数字值  | 12.3, 5, 999                    | `v <- 23.5 ; print(class(v));`           | `[1] "numeric"`   |
| 整数   | 2L, 34L, 0L                     | `v <- 2L ; print(class(v));`             | `[1] "integer"`   |
| 复数   | 3 + 2i                          | `v <- 2+5i ; print(class(v));`           | `[1] "complex"`   |
| 字符   | ‘a’ , ‘“good”, “TRUE”, ‘23.4’   | `v <- "TRUE" ; print(class(v));`         | `[1] "character"` |
| 原生   | `"Hello"`存储值为： `48 65 6c 6c 6f` | `v <- charToRaw("Hello"); print(class(v));` | `[1] "raw"`       |

在*R*编程中，非常基本的数据类型是叫作向量的*R*对象，它们保存不同类的元素，如上所示。 请注意在*R*语言中，类型的数量不仅限于上述六种类型。 例如，我们可以使用许多原子向量并创建一个数组，其类型将成为数组。

## 向量

当要创建具有多个元素的向量时，应该使用`c()`函数，表示将元素组合成一个向量。

```R
# Create a vector.
apple <- c('red','green',"yellow");
print(apple);

# Get the class of the vector.
print(class(apple));
```

上面示例代码，执行结果如下 -

```shell
> apple <- c('red','green',"yellow");
> print(apple);
[1] "red"    "green"  "yellow"
> print(class(apple));
[1] "character"
>
```

## 列表

列表是一个*R*对象，它可以包含许多不同类型的元素，如向量，函数，甚至其中的另一个列表。

```R
# Create a list.
list1 <- list(c(2,5,3),21.3,sin);

# Print the list.
print(list1);
```

上面示例代码，执行结果如下 -

```shell
[[1]]
[1] 2 5 3

[[2]]
[1] 21.3

[[3]]
function (x)  .Primitive("sin")
```

## 矩阵

矩阵是二维矩形数据集。 它可以使用向量输入到矩阵函数来创建。

```R
# Create a matrix.
M = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = TRUE)
print(M)
```

当执行上述代码时，会产生以下结果 -

```shell
     [,1] [,2] [,3]
[1,] "a"  "a"  "b"
[2,] "c"  "b"  "a"
```

## 数组

矩阵只能有两个维度，数组可以是任意数量的维数。数组函数采用一个`dim`属性，创建所需的维数。 在下面的例子中，我们创建一个有两个元素的数组，每个元素都是`3x3`个矩阵。

```R
# Create an array.
a <- array(c('green','yellow'),dim = c(3,3,2))
print(a)
```

当执行上述代码时，会产生以下结果 -

```shell
, , 1

     [,1]     [,2]     [,3]
[1,] "green"  "yellow" "green"
[2,] "yellow" "green"  "yellow"
[3,] "green"  "yellow" "green"

, , 2

     [,1]     [,2]     [,3]
[1,] "yellow" "green"  "yellow"
[2,] "green"  "yellow" "green"
[3,] "yellow" "green"  "yellow"

```

## 因子

因子是使用向量创建的*R*对象。 它将向量存储在向量中的元素的不同值作为标签。标签始终是字符，无论它是输入向量中是数字，还是字符或布尔等。它们在统计建模中很有用。

因子使用`factor()`函数创建。`nlevels`函数给出了级别的计数。

```R
# Create a vector.
apple_colors <- c('green','green','yellow','red','red','red','green')

# Create a factor object.
factor_apple <- factor(apple_colors)

# Print the factor.
print(factor_apple)
print(nlevels(factor_apple))
```

当执行上述代码时，会产生以下结果 -

```shell
[1] green  green  yellow red    red    red   green 
Levels: green red yellow
# applying the nlevels function we can know the number of distinct values
[1] 3
```

## 数据帧

数据帧是表格数据对象。与数据帧中的矩阵不同，每列可以包含不同的数据模式。 第一列是数字，而第二列可以是字符，第三列可以是逻辑类型。它是一个长度相等的向量列表。

数据帧使用`data.frame()`函数创建。

```R
# Create the data frame.
BMI <-     data.frame(
   gender = c("Male", "Male","Female"), 
   height = c(152, 171.5, 165), 
   weight = c(81,93, 78),
   Age = c(42,38,26)
)
print(BMI)
```

当执行上述代码时，会产生以下结果 -

```R
  gender height weight Age
1   Male  152.0     81  42
2   Male  171.5     93  38
3 Female  165.0     78  26
```