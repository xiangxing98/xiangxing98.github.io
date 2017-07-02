---
output:
  html_notebook:
    number_sections: yes
    toc: yes
---

# R语言高效数据清理包dplyr学习
> [xueqin.tv](http://www.xueqing.tv/lesson/83)

## Chapter0 dplyr介绍
dplyr是一款用于数据整理的R包，本节内容介绍了dplyr的特性以及雪晴数据网《dplyr高效数据清理》的基本的内容，感兴趣的同学请尽快报名
```{r Load dplyr package}
# Load dplyr package
if(!suppressWarnings(require(dplyr)))
{
    install.packages('dplyr')
    require(dplyr)
}
```


## Chapter1 数据导入
介绍如何将文本格式的数据导入到R的内存，主要介绍read.table和read.csv函数，及常用参数的使用

### read.table

read.table(
    ## file path
    file,
    ## 1st line as header/column name
    header = FALSE,
    ## separator strings
    sep = "",
    ## how manhy rows need read
    nrows = -1,
    ## how manuy rows need skip
    skip = 0,
    ## not available data define as NA
    fill = !blank.lines.skip)

```{r read.table instruction}
#example
read.table(file = "dplyr-data/read.table/file1.txt")
#     V1  V2     V3
# 1 name age height
# 2 John  10    150
# 3 Jack  27    180
# 4 Mary  29    167

read.table(file = "dplyr-data/read.table/file1.txt",
    header = TRUE)
#   name age height
# 1 John  10    150
# 2 Jack  27    180
# 3 Mary  29    167

file1.data <- read.table(file = "dplyr-data/read.table/file1.txt",
    header = TRUE)
file1.data

# sep parameter
read.table(file = "dplyr-data/read.table/file1.txt",
    header = TRUE,
    sep = " ")
#   name.age.height
# 1   John\t10\t150
# 2   Jack\t27\t180
# 3   Mary\t29\t167

# tab and new row
cat("\t\t\t1")
			# 1
cat("\n\n\t1")
#
#
# 	1

read.table(file = "dplyr-data/read.table/file1.txt",
    header = TRUE,
    sep = "\t")
#   name age height
# 1 John  10    150
# 2 Jack  27    180
# 3 Mary  29    167

# sep is a comma
read.table(file = "dplyr-data/read.table/file2.txt",
    header = TRUE,
    sep = ",")
#   name age height
# 1 John  10    150
# 2 Jack  27    180
# 3 Mary  29    167

# skip & fill parameter
read.table(file = "dplyr-data/read.table/file3.txt",
    header = TRUE)
# Error in scan(file = file, what = what, sep = sep, quote = quote, dec = dec,  :
#   line 4 did not have 3 elements

read.table(file = "dplyr-data/read.table/file3.txt",
    header = TRUE,
    nrows = 4)
# Error in scan(file = file, what = what, sep = sep, quote = quote, dec = dec,  :
#   line 4 did not have 3 elements

read.table(file = "dplyr-data/read.table/file3.txt",
    header = TRUE,
    nrows = 3)
#   name age height
# 1 John  10    150
# 2 Jack  27    180
# 3 Mary  29    167
# but we missing 1 row, so skip parameter is used as follow

read.table(file = "dplyr-data/read.table/file3.txt",
    header = FALSE,
    skip = 5)
#       V1 V2  V3
# 1 Steven 45 175
# skip 1st 5 rows and no header

read.table(file = "dplyr-data/read.table/file3.txt",
    header = TRUE,
    fill = T)
# fill missing values as NA
#     name age height
# 1   John  10    150
# 2   Jack  27    180
# 3   Mary  29    167
# 4    DDD  NA     NA
# 5 Steven  45    175

```

### read.csv
```{r import order data by read.csv}
# import data and change to tbl object
order <- read.csv("dplyr-data/order.csv")
head(order,5)
order_tbl <- tbl_df(order)
head(order_tbl, 5)
```

## Chapter2 tbl对象的介绍
本节内容介绍如果用data.frame对象构造成tbl对象
tbl是dplyr定义的数据类型，可以接受data.frame,cube,sql
```{r import data by read.table}
# import data
order <- read.table(file = "dplyr-data/order.csv",
    header = T,
    sep = ",")
class(order)
# [1] "data.frame"
head(order)
tail(order)

# Load dplyr package
if(!suppressWarnings(require(dplyr)))
{
    install.packages('dplyr')
    require(dplyr)
}
# change to tbl use tbl_df function
order_tbl <- tbl_df(order)
class(order_tbl)
# [1] "tbl_df"     "tbl"        "data.frame"
order_tbl

# for a data.frame, is not nessary to change to tbl object
# for sql object, can useful to use dplyr to manupulate data

# another way to read data
library(readr)
order <- read_csv("E:/03-Download/dplyr/dplyr-data/order.csv")
View(order)
```

## Chapter3 数据筛选--filter函数
filter(tbl/data.fram, condition) and output a data.frame, filter rows/observation
```{r filter in dplyr}
# Load dplyr package in a safer way
if(!suppressWarnings(require(dplyr)))
{
    install.packages('dplyr')
    require(dplyr)
}

df <- data.frame(
  color = c("blue", "black", "blue", "blue", "black"),
  value = 1:5
)
tbl <- tbl_df(df)
tbl
# # A tibble: 5 × 2
#    color value
#   <fctr> <int>
# 1   blue     1
# 2  black     2
# 3   blue     3
# 4   blue     4
# 5  black     5

# filter a value that match some condition
filter(tbl, color == "blue")
# # A tibble: 3 × 2
#    color value
#   <fctr> <int>
# 1   blue     1
# 2   blue     3
# 3   blue     4

# filter value in 1 or 4
filter(tbl, value %in% c(1,4))
# A tibble: 2 × 2
#    color value
#   <fctr> <int>
# 1   blue     1
# 2   blue     4

# import data and change to tbl object
order <- read.csv("dplyr-data/order.csv")
head(order,5)
order_tbl <- tbl_df(order)
head(order_tbl, 5)

# filter order data is 2009-10-13 rows
filter(order_tbl, orderdate == "2009-10-13")

# filter order data is 2009-10-13 rows and total price greater than 100 rows, 1 row match and assign to filterData
filterData <- filter(order_tbl, orderdate == "2009-10-13" & totalprice > 100)
View(filterData)
```

## Chapter4 子集选取函数--select
select columns/variable by name/match rules
```{r select function in dplyr}
# Load dplyr package in a safer way
if(!suppressWarnings(require(dplyr)))
{
    install.packages('dplyr')
    require(dplyr)
}

df <- data.frame(
  color = c("blue", "black", "blue", "blue", "black"),
  value = 1:5
)
tbl <- tbl_df(df)
tbl

# just select color column
select(tbl, color)
# A tibble: 5 × 1
#    color
#   <fctr>
# 1   blue
# 2  black
# 3   blue
# 4   blue
# 5  black

# select all other columns except color column equals select value column
select(tbl, -color)
# A tibble: 5 × 1
#   value
#   <int>
# 1     1
# 2     2
# 3     3
# 4     4
# 5     5
```

Useful function to select
```{r Useful function to select}
starts_with(x, ignore.case = TRUE) # column/variable start with chart x
ends_with(x, ignore.case = TRUE) # column/variable end with chart x
contains(x, ignore.case = TRUE) # column/variable contains chart x
matches(x, ignore.case = TRUE)  # column/variable matches regular expression x
num_range("x", 1:5, width = 2)  # column/variable from x01 to x05
one_of("x", "y", "z") # column/variable contains in x, y, z
everything() # all column/variable

# e.g. order_tbl, check column
names(order_tbl)
 # [1] "X"             "orderid"       "customerid"    "campaignid"
 # [5] "orderdate"     "city"          "state"         "zipcode"
 # [9] "paymenttype"   "totalprice"    "numorderlines" "numunits"

# select order data and total price
date_price <- select(order_tbl,orderdate, totalprice)
date_price

# rename column name at the same time
date_price2 <- select(order_tbl,date = orderdate, price = totalprice)
date_price2

# select starts with order column name
Start_With_Order <- select(order_tbl,starts_with("order",ignore.case = TRUE))
Start_With_Order
# A tibble: 100,000 × 2
#    orderid  orderdate
#      <int>     <fctr>
# 1  1002854 2009-10-13
# 2  1002855 2009-10-13
# 3  1002856 2011-06-02
# 4  1002857 2009-10-14
# 5  1002886 2010-11-19
# 6  1002887 2009-10-15
# 7  1002888 2009-10-15
# 8  1002889 2009-10-15
# 9  1002890 2009-10-15
# 10 1003004 2009-10-15
# ... with 99,990 more rows

# select contains id column name
Contains_ID <- select(order_tbl, contains("id",ignore.case = TRUE))
head(Contains_ID,5)
# A tibble: 5 × 3
#   orderid customerid campaignid
#     <int>      <int>      <int>
# 1 1002854      45978       2141
# 2 1002855     125381       2173
# 3 1002856     103122       2141
# 4 1002857     130980       2173
# 5 1002886      48553       2141

# rename function
as.data.frame(Contains_ID)
# rename the new name must at the left
after_rename <- rename(Contains_ID, ooID = orderid, ooID = customerid, ooCAID =  campaignid)
head(Contains_ID,5)
# A tibble: 5 × 3
#   orderid customerid campaignid
#     <int>      <int>      <int>
# 1 1002854      45978       2141
# 2 1002855     125381       2173
# 3 1002856     103122       2141
# 4 1002857     130980       2173
# 5 1002886      48553       2141

# after rename returns a new tbl, the origin Contains_ID will not be changed
head(after_rename,5)
# A tibble: 5 × 3
#      ooID   ooID ooCAID
#     <int>  <int>  <int>
# 1 1002854  45978   2141
# 2 1002855 125381   2173
# 3 1002856 103122   2141
# 4 1002857 130980   2173
# 5 1002886  48553   2141
# this works in the code below
head(rename(iris, pt = Petal.Length),5)

# e.g. with select from ? rename
iris <- tbl_df(iris) # so it prints a little nicer
select(iris, starts_with("Petal"))
select(iris, ends_with("Width"))
select(iris, contains("etal"))
select(iris, matches(".t."))
select(iris, Petal.Length, Petal.Width)
vars <- c("Petal.Length", "Petal.Width")
select(iris, one_of(vars))

df <- as.data.frame(matrix(runif(100), nrow = 10))
df <- tbl_df(df[c(3, 4, 7, 1, 9, 8, 5, 2, 6, 10)])
select(df, V4:V6)
select(df, num_range("V", 4:6))

# Drop variables
select(iris, -starts_with("Petal"))
select(iris, -ends_with("Width"))
select(iris, -contains("etal"))
select(iris, -matches(".t."))
select(iris, -Petal.Length, -Petal.Width)

# Rename variables:
# * select() keeps only the variables you specify
select(iris, petal_length = Petal.Length)
# Renaming multiple variables uses a prefix:
select(iris, petal = starts_with("Petal"))

# Reorder variables: keep the variable "Species" in the front
select(iris, Species, everything())

# * rename() keeps all variables
rename(iris, petal_length = Petal.Length)

# Programming with select ---------------------------------------------------
select_(iris, ~Petal.Length)
select_(iris, "Petal.Length")
select_(iris, lazyeval::interp(~matches(x), x = ".t."))
select_(iris, quote(-Petal.Length), quote(-Petal.Width))
select_(iris, .dots = list(quote(-Petal.Length), quote(-Petal.Width)))
```

## Chapter5 数据的排序--arrange函数
traditional method: order function
```{r use order to order}
# Load dplyr package in a safer way
if(!suppressWarnings(require(dplyr)))
{
    install.packages('dplyr')
    require(dplyr)
}

df1 <- data.frame(
  color = c("blue", "black", "blue", "blue", "black"),
  value = 1:5
)
tbl <- tbl_df(df1)
tbl
# A tibble: 5 × 2
#    color value
#   <fctr> <int>
# 1   blue     1
# 2  black     2
# 3   blue     3
# 4   blue     4
# 5  black     5

# order use index
df_order <- order(df1$color)
df_order
# [1] 2 5 1 3 4
df1[df_order,]
#   color value
# 2 black     2
# 5 black     5
# 1  blue     1
# 3  blue     3
# 4  blue     4

# use arrange to order a data frame/tbl, default is aesc, 1 to 3
arrange(df1, color)
# use desc to order by 3 to 1
arrange(df1, desc(color))

# import data and change to tbl object
order <- read.csv("dplyr-data/order.csv")
head(order,5)
order_tbl <- tbl_df(order)
head(order_tbl, 5)

# order by date
tbl <- select(order_tbl, odate = orderdate, oprice = totalprice)
arrange(tbl, odate)
# A tibble: 100,000 × 2
#         odate oprice
#        <fctr>  <dbl>
# 1  2009-10-04    200
# 2  2009-10-04    120
# 3  2009-10-04    100
# 4  2009-10-04    100
# 5  2009-10-04     70
# 6  2009-10-04     50
# 7  2009-10-04     50
# 8  2009-10-04     40
# 9  2009-10-04     40
# 10 2009-10-04     40
# ... with 99,990 more rows

# order by date & by price desc 3 to 1
arrange(tbl, odate, desc(oprice))
# A tibble: 100,000 × 2
#         odate oprice
#        <fctr>  <dbl>
# 1  2009-10-04    200
# 2  2009-10-04    120
# 3  2009-10-04    100
# 4  2009-10-04    100
# 5  2009-10-04     70
# 6  2009-10-04     50
# 7  2009-10-04     50
# 8  2009-10-04     40
# 9  2009-10-04     40
# 10 2009-10-04     40
# ... with 99,990 more rows
```

## Chapter6 数据扩展--mutate函数
数据扩展，保留原来的变量、列的基础上增加变量或者列
```{r mutate function}
# Load dplyr package in a safer way
if(!suppressWarnings(require(dplyr)))
{
    install.packages('dplyr')
    require(dplyr)
}

df1 <- data.frame(
  color = c("blue", "black", "blue", "blue", "black"),
  value = 1:5
)
tbl <- tbl_df(df1)
tbl
# A tibble: 5 × 2
#    color value
#   <fctr> <int>
# 1   blue     1
# 2  black     2
# 3   blue     3
# 4   blue     4
# 5  black     5

# add double column
mutate(tbl, double = 2 * value)
# A tibble: 5 × 3
#    color value double
#   <fctr> <int>  <dbl>
# 1   blue     1      2
# 2  black     2      4
# 3   blue     3      6
# 4   blue     4      8
# 5  black     5     10

# add double column and quadruple column
mutate(tbl, double = 2 * value, quadruple = 4 * value)
# A tibble: 5 × 4
#    color value double quadruple
#   <fctr> <int>  <dbl>     <dbl>
# 1   blue     1      2         4
# 2  black     2      4         8
# 3   blue     3      6        12
# 4   blue     4      8        16
# 5  black     5     10        20

# use order data set to mutate year, month and date
# import data and change to tbl object
order <- read.csv("dplyr-data/order.csv")
head(order,5)
order_tbl <- tbl_df(order)
head(order_tbl, 5)
tbl <- select(order_tbl, odate = orderdate, oprice = totalprice)
tbl <- arrange(tbl, odate, desc(oprice))
head(tbl, 5)
# # A tibble: 5 × 2
#        odate oprice
#       <fctr>  <dbl>
# 1 2009-10-04    200
# 2 2009-10-04    120
# 3 2009-10-04    100
# 4 2009-10-04    100
# 5 2009-10-04     70

# mutate
tbl_New <- mutate(tbl, oYear = substr(odate, 1, 4), oMonth = substr(odate, 6, 7),oDate = substr(odate, 9, 10))
head(tbl_New,5)
# A tibble: 5 × 5
#        odate oprice oYear oMonth oDate
#       <fctr>  <dbl> <chr>  <chr> <chr>
# 1 2009-10-04    200  2009     10    04
# 2 2009-10-04    120  2009     10    04
# 3 2009-10-04    100  2009     10    04
# 4 2009-10-04    100  2009     10    04
# 5 2009-10-04     70  2009     10    04

# transmute
# Mutate adds new variables and preserves existing;
# transmute drops existing variables.
df1 <- data.frame(
  color = c("blue", "black", "blue", "blue", "black"),
  value = 1:5
)
tbl_transmute <- tbl_df(df1)
tbl_transmute
# A tibble: 5 × 2
#    color value
#   <fctr> <int>
# 1   blue     1
# 2  black     2
# 3   blue     3
# 4   blue     4
# 5  black     5

transmute(tbl_transmute, double = 2 * value, quadruple = 4 * value)
# A tibble: 5 × 2
#   double quadruple
#    <dbl>     <dbl>
# 1      2         4
# 2      4         8
# 3      6        12
# 4      8        16
# 5     10        20
```

## Chapter7 数据汇总--summarise函数
数据汇总-将多个值汇总为一个数据值
```{r summarise}
df1 <- data.frame(
  color = c("blue", "black", "blue", "blue", "black"),
  value = 1:5
)
tbl_summarise <- tbl_df(df1)

summarise(tbl_summarise, total = sum(value))
# A tibble: 1 × 1
#   total
#   <int>
# 1    15

# multi parameter
summarise(tbl_summarise, total_value = sum(value), mean_value = mean(value), sd_value = sd(value))
# A tibble: 1 × 3
#   total_value mean_value sd_value
#         <int>      <dbl>    <dbl>
# 1          15          3 1.581139

# use order data set to summarise
# import data and change to tbl object
order <- read.csv("dplyr-data/order.csv")
head(order,5)
order_tbl <- tbl_df(order)
head(order_tbl, 5)
tbl <- select(order_tbl, odate = orderdate, oprice = totalprice)
# tbl <- arrange(tbl, odate, desc(oprice))
summarise(tbl, max = max(oprice),
              min = min(oprice),
              mean = mean(oprice))
# A tibble: 1 × 3
#     max   min     mean
#   <dbl> <dbl>    <dbl>
# 1  6780     0 60.77773

```
summarise()中的汇总函数将一列值转换为一个单独的值输出
R自带的统计函数都是可以使用的
min(), max(), mean(), sum(), sd(), median(), IQR()

此外，dplyr还提供了一些其他会用到的函数
n():观测值的个数
n_distinct(x):不相同的观测值的个数
first(x),last(x)和nth(x, n)获取第一个，最后一个，和第n个数据

```{r first and last value}
summarise(tbl, first = first(odate), last = last(odate))
# A tibble: 1 × 2
#        first       last
#       <fctr>     <fctr>
# 1 2009-10-13 2014-04-28
```

## Chapter8 数据连接--join函数
dplyr advanced function:
- data set join/connection, like excel vlookup function
- group_by
- pipe function: %>%
- other function: do, plyr::colwise
- mysql database connection

```{r join}
x <- data.frame(name = c("John", "Paul", "George", "Ringo", "Stuart", "Siqin"),
                instrument = c("guitar", "bass", "guitar", "drums", "bass", "drums"))
x
#     name instrument
# 1   John     guitar
# 2   Paul       bass
# 3 George     guitar
# 4  Ringo      drums
# 5 Stuart       bass
# 6  Siqin      drums
y <- data.frame(name = c("John", "Paul", "George", "Ringo", "Brian"),
                band = c(T, T, T, T, T))
y
#     name band
# 1   John TRUE
# 2   Paul TRUE
# 3 George TRUE
# 4  Ringo TRUE
# 5  Brian TRUE

# left_join like excel vlookup, all value in left table will remain, but not match value in right table will be set NA
left_join(x, y, by = "name")
#     name instrument band
# 1   John     guitar TRUE
# 2   Paul       bass TRUE
# 3 George     guitar TRUE
# 4  Ringo      drums TRUE
# 5 Stuart       bass   NA
# 6  Siqin      drums   NA

# inner_join, just remain left and right table match value,
# and add column(right table data) in left table
# and not match value in left table will be discarded
inner_join(x, y, by = "name")
#     name instrument band
# 1   John     guitar TRUE
# 2   Paul       bass TRUE
# 3 George     guitar TRUE
# 4  Ringo      drums TRUE

# semi_join, just remain left table that matches the value in right table, and right table value will not used
semi_join(x, y, by = "name")
#     name instrument
# 1   John     guitar
# 2   Paul       bass
# 3 George     guitar
# 4  Ringo      drums

# anti_join, just convert with semi_join, just keep match values in right table
anti_join(x, y, by = "name")
#     name instrument
# 1  Siqin      drums
# 2 Stuart       bass

# use order and custimer data set to join
# import data and change to tbl object
df_order <- read.csv("dplyr-data/order.csv")
df_customer <- read.csv("dplyr-data/customer.csv")
head(df_order,5)
head(df_customer,5)

tbl_order <- tbl_df(df_order)
tbl_customer <- tbl_df(df_customer)

s_order <- select(tbl_order, odate = orderdate, ocust_id = customerid)
s_customer <- select(tbl_customer, ocust_id = customerid, gender, firstname,lastname =Lastname)

arrange(left_join(s_order, s_customer, by = "ocust_id"), firstname)
```

## Chapter9 分类汇总 -- group_by
分类汇总 -- group_by
```{r group_by function}
#summary by year--Group-wise summary
# group_by()转变成一 个分好组的数据框

df1 <- data.frame(
  color = c("blue", "black", "blue", "blue", "black"),
  value = 1:5
)
summarise(df1, total =sum(value))
# just get one sumarised data total
#   total
# 1    15

# group by color
by_color <- group_by(df1, color)
# then summarise by group
summarise(by_color, total = sum(value))
# A tibble: 2 × 2
#    color total
#   <fctr> <int>
# 1  black     7
# 2   blue     8


# use order data set
# import data and change to tbl object
df_order <- read.csv("dplyr-data/order.csv")
head(df_order,5)

tbl_order <- tbl_df(df_order)
# tbl_customer <- tbl_df(df_customer)

s_order <- select(tbl_order, odate = orderdate, oprice = totalprice)

# mutate year and month column
m_order <- mutate(s_order,
                  oyear = substr(odate, 1, 4),
                  omonth = substr(odate, 6, 7))
head(m_order, 5)

# group by year
m_order_year <- group_by(m_order, oyear)
head(m_order_year)
# Source: local data frame [6 x 4]
# Groups: oyear [3]
#
#        odate oprice oyear omonth
#       <fctr>  <dbl> <chr>  <chr>
# 1 2009-10-13 190.00  2009     10
# 2 2009-10-13  10.00  2009     10
# 3 2011-06-02  35.22  2011     06
# 4 2009-10-14  10.00  2009     10
# 5 2010-11-19  10.00  2010     11
# 6 2009-10-15  10.00  2009     10

# summary yearly price and average price, and max month for check data period(year 2014 just have 5 month)
# summarise support multi parameter
summarise(m_order_year,
          yearly_price = sum(oprice),
          average_price = mean(oprice),
          Max_Month = max(omonth))
# A tibble: 6 × 4
#   oyear yearly_price average_price `max(omonth)`
#   <chr>        <dbl>         <dbl>         <chr>
# 1  2009     262627.5      34.13850            12
# 2  2010     967429.2      52.23982            12
# 3  2011    1380636.6      51.35342            12
# 4  2012    1404113.1      68.40990            12
# 5  2013    1633004.8      76.71011            12
# 6  2014     429962.0      84.47190            05
```

## Chapter10 管道函数
%>% or %.% use the previous function(left)'s out put as the next function(right)'s input.
```{r pipe function}
1:5 %>% mean()
# [1] 3
1:5 %>% mean(.) %>% sqrt()
# [1] 1.732051

# use order data set
# 01. import data and change to tbl object
df_order <- read.csv("dplyr-data/order.csv")
head(df_order,5)
# 02. change to tbl object
tbl_order <- tbl_df(df_order)
head(tbl_order, 5)

# 03. mutate year and month column
m_order <- mutate(tbl_order,
                  oyear = substr(orderdate, 1, 4),
                  omonth = substr(orderdate, 6, 7))
head(m_order, 5)

# 04. group by month
m_order_month <- group_by(m_order,omonth)

# 05. summarise order count by month
summarise(m_order_month, monthly_order_count = n())


# use pipe function rewrite above flow 03,04,05
tbl_order %>%
  mutate(oyear = substr(orderdate, 1, 4),
         omonth = substr(orderdate, 6, 7)) %>%
  group_by(omonth) %>%
  summarise(monthly_order_count = n())
# A tibble: 12 × 2
#    omonth monthly_order_count
#     <chr>               <int>
# 1      01               13601
# 2      02                6609
# 3      03                6235
# 4      04                6042
# 5      05                5037
# 6      06                4691
# 7      07                4354
# 8      08                4763
# 9      09                5676
# 10     10                7106
# 11     11               17268
# 12     12               18618

```

## Chapter11 colwise和do函数
筛选销售额每年最大的记录
```{r colwise and do function}
# Load dplyr package
if(!suppressWarnings(require(dplyr)))
{
    install.packages('dplyr')
    require(dplyr)
}

# import data
order <- read.csv("dplyr-data/order.csv")

# Get Yearly Order data and split by year
Yearly_Order <- order %>% select(orderdate, totalprice) %>%
                  mutate(oyear = substr(orderdate, 1, 4))

# Group by Year, Get Yealy Maximun Order
Yealy_Maximun <- Yearly_Order %>% group_by(oyear) %>%
                  summarise(max(totalprice))

```

筛选每年销售额最大的两条记录
```{r do(data, fun(.))}
# Load dplyr package
if(!suppressWarnings(require(dplyr)))
{
    install.packages('dplyr')
    require(dplyr)
}

# import data
order <- read.csv("dplyr-data/order.csv")

# Get Yearly Order data and split by year
Yearly_Order <- order %>% select(orderdate, totalprice) %>%
                  mutate(oyear = substr(orderdate, 1, 4))

# Group by Year, Get Yealy Max 2 Orders
Yearly_Order %>% group_by(oyear) %>%
        arrange(desc(totalprice)) %>%
        do(., head(., 2))
# Source: local data frame [12 x 3]
# Groups: oyear [6]
#
#     orderdate totalprice oyear
#        <fctr>      <dbl> <chr>
# 1  2009-12-17    2244.00  2009
# 2  2009-10-26    1154.65  2009
# 3  2010-09-05    2250.00  2010
# 4  2010-10-06    2250.00  2010
# 5  2011-05-09    2250.00  2011
# 6  2011-05-17    2000.00  2011
# 7  2012-12-12    6780.00  2012
# 8  2012-11-12    6606.00  2012
# 9  2013-01-18    4050.00  2013
# 10 2013-06-26    3592.00  2013
# 11 2014-03-29    4735.00  2014
# 12 2014-03-30    4378.50  2014

```

### plyr package colwise function
```{r colwise function}
# Load plyr package
if(!suppressWarnings(require(plyr)))
{
    install.packages('plyr')
    require(plyr)
}

# load and check iris data set
head(iris, 5)

# to round every column use colwise function
# call function to each column
# colwise(function)(data.frame)
colwise(round)(iris[, 1:4]) %>% head(., 5)
#   Sepal.Length Sepal.Width Petal.Length Petal.Width
# 1            5           4            1           0
# 2            5           3            1           0
# 3            5           3            1           0
# 4            5           3            2           0
# 5            5           4            1           0

```

## Chapter12 连接MySQL数据库
连接MySQL数据库
```{r connect mysql}
# mysql data base
src_database <- src_mysql(dbname = "sqlbook", host = "127.0.0.1", port = "3063",user = "root",password = "root")

# mysql table
src_table <- tbl(src_database, from = "orders")

# execute sql command
sqlQueryResults <- select(src_table, orderid, orderdate)
# or use pipe function
sqlQueryResults <- src_table %>% select(orderid, orderdate)

# check sql query command
sqlQueryResults$query

# save results as csv file
write.csv(sqlQueryResults, "dplyr-data/order_record.csv")

# show sqlQueryResults
sqlQueryResults

# mysql data base
# mysql -u root -p
# enter password

# show databases
# show databases

#use which database, change to your database
# use mydatabase

# show tables in your database
# show tables

```

## Chapter13 Example dplyr and pipeline operator

> [dplyr Examples with pipeline](https://renkun.me/pipeR-tutorial/Examples/dplyr.html)

> [rlist Examples with pipeline](https://renkun.me/pipeR-tutorial/Examples/rlist.html)


`hflights` is a dataset contains information about flights that departed Houston in 2011. In the description the author writes:

> This dataset contains all flights departing from Houston airports IAH (George Bush Intercontinental) and HOU (Houston Hobby). The data comes from the Research and Innovation Technology Administration at the Bureau of Transporation statistics: [http://www.transtats.bts.gov/DatabaseInfo.asp?DB_ID=120&Link=0](http://www.transtats.bts.gov/DatabaseInfo.asp?DB_ID=120&Link=0)

Having known what the data is all about, then we load the libraries and take a look at the structure of the data.

```{r}
install.packages(c("dplyr","hflights"))
library(dplyr)
library(pipeR)
# or use
library(magrittr)
library(hflights) # install.packages("hflights")
data(hflights)

str(hflights)
# 'data.frame':	227496 obs. of  21 variables:
#  $ Year             : int  2011 2011 2011 2011 2011 2011 2011 2011 2011 2011 ...
#  $ Month            : int  1 1 1 1 1 1 1 1 1 1 ...
#  $ DayofMonth       : int  1 2 3 4 5 6 7 8 9 10 ...
#  $ DayOfWeek        : int  6 7 1 2 3 4 5 6 7 1 ...
#  $ DepTime          : int  1400 1401 1352 1403 1405 1359 1359 1355 1443 1443 ...
#  $ ArrTime          : int  1500 1501 1502 1513 1507 1503 1509 1454 1554 1553 ...
#  $ UniqueCarrier    : chr  "AA" "AA" "AA" "AA" ...
#  $ FlightNum        : int  428 428 428 428 428 428 428 428 428 428 ...
#  $ TailNum          : chr  "N576AA" "N557AA" "N541AA" "N403AA" ...
#  $ ActualElapsedTime: int  60 60 70 70 62 64 70 59 71 70 ...
#  $ AirTime          : int  40 45 48 39 44 45 43 40 41 45 ...
#  $ ArrDelay         : int  -10 -9 -8 3 -3 -7 -1 -16 44 43 ...
#  $ DepDelay         : int  0 1 -8 3 5 -1 -1 -5 43 43 ...
#  $ Origin           : chr  "IAH" "IAH" "IAH" "IAH" ...
#  $ Dest             : chr  "DFW" "DFW" "DFW" "DFW" ...
#  $ Distance         : int  224 224 224 224 224 224 224 224 224 224 ...
#  $ TaxiIn           : int  7 6 5 9 9 6 12 7 8 6 ...
#  $ TaxiOut          : int  13 9 17 22 9 13 15 12 22 19 ...
#  $ Cancelled        : int  0 0 0 0 0 0 0 0 0 0 ...
#  $ CancellationCode : chr  "" "" "" "" ...
#  $ Diverted         : int  0 0 0 0 0 0 0 0 0 0 ...
```

The data is tabular and very well fit in a data frame. Remarkably it has 227496 rows which is much larger than small datasets like mtcars.

Two columns in the data frame attracts our attention: `Distance` and `ActualElapsedTime`. If we divide Distance by ActualElapsedTime we can get the actual flight speed. Therefore, in this example, we use dplyr functions to transform the data in pipeline and see which carrier has faster flights.

```{r}
hflights %>% 
  # 1. filter out no canceld flight
  filter(Cancelled == 0) %>%
  # 2. mutate new column speed
  mutate(speed = Distance / ActualElapsedTime) %>%
  # 3. save to hflights2
  (~ hflights2) %>% 
  # 4. group_by UniqueCarrier
    group_by(UniqueCarrier) %>%
    #group_by(.data = .,UniqueCarrier)  %>%
  # 5. summarize
  summarize(mean_speed = mean(speed,na.rm = TRUE)) %>%
  # 6. arrange, by speed desc
  arrange(desc(mean_speed)) %>%
  # 7. barplot, why with?
  with(barplot(mean_speed,names.arg = UniqueCarrier,
    main = "Average flight speed"))
```




## End 2017-06-10 By Stone.Hou

Updated in 20170702, add example
