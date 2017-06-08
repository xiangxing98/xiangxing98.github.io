/**
 * @ Title:		Data Analysis in R, the data.table Way
 * @ Authors:	siqin.hou (xiangxing985529@163.com)
 * @ Date:		2017-06-08 08:09:25
 * @ Version:	v001
 */


# Data Analysis in R, the data.table Way
> [DataCamp：data-table-data-manipulation-r-tutorial](https://www.datacamp.com/courses/data-table-data-manipulation-r-tutorial)

## Course Description

The R data.table package is rapidly making its name as the number one choice for handling large datasets in R. This online data.table tutorial will bring you from data.table novice to expert in no time. Once you are introduced to the general form of a data.table query, you will learn the techniques to subset your data.table, how to update by reference and how you can use data.table’s set()-family in your workflow. The course finishes with more complex concepts such as indexing, keys and fast ordered joins. Upon completion of the course, you will be able to use data.table in R for a more efficient manipulation and analysis process. Enjoy!


```
# Load data.table package
if(!suppressWarnings(require(data.table)))
{
    install.packages('data.table')
    require(data.table)
}

# DT[i, j, by]
# Take DT, subseting rows by using i, then calculate j grouped by by.
# R: i,j,by
# SQL: Where,select,group by
trades[
    filledShares < orderedShares,
    sum( (orderedShares-filledShares) - orderPrice / fx ),
    by = "date,region,algo"
]

DT <- data.table(A = 1:6, B =  c("A","B","C"), C = rnorm(6), D = TRUE)
DT

typeof(1) == "double"
typeof(1L) == "integer"

typeof(NA) == "logical"
typeof(NA_integer_) == "integer"

#
DT;DT[3:5,];DT[3:5]


```

## Create and subset a data.table

Welcome to the interactive exercises for your data.table course. Here you will learn the ins and outs of working with the data.table package.

While most of the material is covered by Matt and Arun in the videos, you will sometimes need to show some street smarts to get to the right answer. Remember that before using the hint you can always have a look at the official documentation by typing ?data.table in the console.

Let's start with some warm-up exercises based on the topics covered in the video. Recall from the video that you can use L after a numeric to specify that it is an integer. You can also give columns with different lengths when creating a data.table, and R will "recycle" the shorter column to match the length of the longer one by re-using the first items. In the example below, column x is recycled to match the length of column y:
```
data.table(x = c("A", "B"), y = 1:4)
   x y
1: A 1
2: B 2
3: A 3
4: B 4
```
You can also review the slides used in the videos by pressing the slides button.

Instructions
Create a data.table my_first_data_table with a column x = c("a", "b", "c", "d", "e") and a column y = c(1, 2, 3, 4, 5). Use the function data.table().
Create a two-column data.table DT that contains the four integers 1, 2, 1 and 2 in the first column a and the letters A, B, C and D in the second column b. Use recycling so that the contents of a will be automatically used twice. Note that LETTERS[1] returns "A", LETTERS[2] returns "B", and so on.
Select the third row of DT and just print the result to the console.
Select the second and third rows without using commas and print the result to the console.

```
# The data.table package is preloaded

# Create my_first_data_table
my_first_data_table <- data.table(x = c("a", "b", "c", "d", "e"), 
                                  y = c(1, 2, 3, 4, 5))  
  
# Create a data.table using recycling
# Make sure to include the L after 1 and 2, 
# so that the class of the first column is integer and not numeric.
DT <- data.table(a = c(1L, 2L), b = LETTERS[1:4])

# Print the third row to the console
DT[3,]

# Print the second and third row to the console without using commas
DT[c(2,3),]
DT[2:3]
```

##Getting to know a data.table

You can pass a data.table to base R functions like head() and tail() that accept a data.frame because data.tables are also data.frames. Also, keep in mind that the special symbol .N, when used inside square brackets, contains the number of rows. For example, DT[.N] and DT[nrow(DT)] will both return the last row in DT.

## Instructions
Select the second to last row of the table using .N.
Return the column names() of the data.table.
Return the number of rows and number of columns of the data.table using the dim() function.
Select row 2 twice and row 3 once, returning a data.table with three rows (two of which are identical).

```
# DT and the data.table package are pre-loaded

# Print the second to last row of DT using .N
DT[.N-1:.N]
#    a b
# 1: 1 C
# 2: 2 B
# 3: 1 A

# Print the column names of DT
names(DT)
# [1] "a" "b"

# Print the number or rows and columns of DT
dim(DT)
# [1] 4 2

# Print a new data.table containing rows 2, 2, and 3 of DT
DT[c(2, 2, 3),]
#    a b
# 1: 2 B
# 2: 2 B
# 3: 1 C
```

# Section 2 - Selecting columns in j

Selecting columns in j
```
# Load data.table package
if(!suppressWarnings(require(data.table)))
{
    install.packages('data.table')
    require(data.table)
}
# The fastest way to learn (by data.table authors): 
# https://www.datacamp.com/courses/data-analysis-the-data-table-way
# Documentation: ?data.table, example(data.table) and browseVignettes("data.table")
# Release notes, videos and slides: http://r-datatable.com


DT <- data.table(
                A = c(1, 2, 3, 4, 5), 
                B = c("a", "b", "c", "d", "e"), 
                C = c(6, 7, 8, 9, 10)) 
DT
#    A B  C
# 1: 1 a  6
# 2: 2 b  7
# 3: 3 c  8
# 4: 4 d  9
# 5: 5 e 10

DT[, .(B, C)]
# .() is an alias to list() in data.tables and they mean the same
#    B  C
# 1: a  6
# 2: b  7
# 3: c  8
# 4: d  9
# 5: e 10

DT[,B]
# [1] "a" "b" "c" "d" "e"

DT[,.(Total = sum(A), Mean = mean(C))]
#    Total Mean
# 1:    15    8

# Recycling in j, column C is recycle
DT[, .(B, C = sum(C))]
#    B  C
# 1: a 40
# 2: b 40
# 3: c 40
# 4: d 40
# 5: e 40

# Throw any thing into j, can draw a plot
DT[, plot(A, C)]

# print A, draw histogram of C and output NULL
DT[, {print(A)
      hist(C)
      NULL}]

```

## Practise: A data.table of a vector?

A data.table DT is preloaded in your workspace on the right. Type DT in the console to have a look at it. As you have learned in the video, you can select a column from that data.table with DT[, .(B)].

What do you think is the output of DT[, B]? vector

```
DT[, .(B)]
#    B
# 1: a
# 2: b
# 3: c
# 4: d
# 5: e

typeof(DT[, .(B)])
# [1] "list"

str(DT[, .(B)])
# Classes ‘data.table’ and 'data.frame':	5 obs. of  1 variable:
#  $ B: chr  "a" "b" "c" "d" ...
#  - attr(*, ".internal.selfref")=<externalptr> 

DT[, B]
# [1] "a" "b" "c" "d" "e"

typeof(DT[, B])
# [1] "character"

str(DT[, B])
# chr [1:5] "a" "b" "c" "d" "e"

is.vector(DT[, B])
# [1] TRUE

# When you use .() in j, the result is always a data.table. 
# For convenience, data.table also provides the option to return a vector 
# while computing on just a single column and not wrapping it with .().

```

## A non-existing column

Have a close look at 1.1 and 1.2 from the data.table package FAQs.

Type D <- 5 in the console. What do you think is the output of DT[, .(D)] and DT[, D]?

```
D <- 5
DT

DT[, .(D)]
# DT[, .(D)] returns 5 as data.table.

DT[, D]
# DT[, D] returns 5 as vector,

# Column D does not exist in DT and is thus not seen as a variable. 
# This causes data.table to look for D in DT's parent frame. 
# Also note that .() in j always returns a data.table.


```

## Subsetting data.tables

As a reminder, DT[i, j, by] is pronounced

> Take DT, subset rows using i, then calculate j grouped by by.

In the video, the second argument j was covered. j can be used to select columns by wrapping the column names in .().

In addition to selecting columns, you can also call functions on them as if the columns were variables. For example, if you had a data.table heights storing people's heights in inches, you could compute their heights in feet as follows:
```
#     name  eye_color   height_inch
# 1:   Tom      Brown            69
# 2: Boris       Blue            71
# 3:   Jim       Blue            68

heights[, .(name, 
              height_ft = height_inch / 12)]
#     name   height_ft
# 1:   Tom    5.750000
# 2: Boris    5.916667
# 3:   Jim    5.666667
```

## Instructions

Create a subset containing the columns B and C for rows 1 and 3 of DT. 
Simply print out this subset to the console.
From DT, create a data.table, ans with two columns: B and val, where val is the product of A and C.
Fill in the blanks in the assignment of ans2, such that it equals the data.table specified in target. Use columns from the previously defined data.tables to produce the val column.

```
# DT and the data.table package are pre-loaded
DT
#    A B  C
# 1: 1 a  6
# 2: 2 b  7
# 3: 3 c  8
# 4: 4 d  9
# 5: 5 e 10

# Subset rows 1 and 3, and columns B and C
DT[c(1,3), .(B, C)]

# Assign to ans the correct value
ans <- DT[, .(B, val = A * C)]
ans
#    B val
# 1: a   6
# 2: b  14
# 3: c  24
# 4: d  36
# 5: e  50

# Fill in the blanks such that ans2 equals target
target <- data.table(B = c("a", "b", "c", "d", "e", 
                           "a", "b", "c", "d", "e"), 
                     val = as.integer(c(6:10, 1:5)))
target
#     B val
#  1: a   6
#  2: b   7
#  3: c   8
#  4: d   9
#  5: e  10
#  6: a   1
#  7: b   2
#  8: c   3
#  9: d   4
# 10: e   5

ans2 <- DT[, .(B, val = c(C, A))]
# B is recycled
ans2
#     B val
#  1: a   6
#  2: b   7
#  3: c   8
#  4: d   9
#  5: e  10
#  6: a   1
#  7: b   2
#  8: c   3
#  9: d   4
# 10: e   5
```

## Section 3 - Doing j by group
doing j by group
```
DT1 <- data.table(A = c("c","b","a"), B =c(1, 2, 3, 4, 5, 6))
DT1
DT1[, .(MySum = sum(B),
    MyMean = mean(B)),
    by = .(A)]

# Groups in 1st Column    
#    A MySum MyMean
# 1: c     5    2.5
# 2: b     7    3.5
# 3: a     9    4.5

# Function calls in by
DT2 <- data.table(A = 1:5, B = 10:14)
DT2
#    A  B
# 1: 1 10
# 2: 2 11
# 3: 3 12
# 4: 4 13
# 5: 5 14

DT2[, .(Mysum = sum(B)), by = .(Grp = A%%2)]
# even and odd number group
#    Grp Mysum
# 1:   1    36
# 2:   0    24

# for short version, no need .()
DT2[, sum(B), by = A%%2]
#    A V1
# 1: 1 36
# 2: 0 24

# Grouping only on a subset, 2:4 rows do group sum
DT2
DT2[2:4, sum(B), by = A%%2]
#    A V1
# 1: 0 24
# 2: 1 12

```

## Let's practise
The by basics
In this section you were introduced to the last of the main parts of the data.table syntax: by. 

If you supply a j expression and a by list of expressions, the j expression is repeated for each by group. Time to master the by argument with some hands-on examples and exercises.

First, just print iris to the console and observe that all rows are printed and that the column names scroll off the top of your screen. This is because iris is a data.frame. Scroll back up to the top to see the column names.

Instructions
Convert the iris dataset to a data.table DT. You're now ready to use data.table magic on it!
Create a new column containing the mean Sepal.Length for each Species. Do not provide a name for this newly created column.
Do exactly the same as in the instruction above, but this time, group by the first letter of the Species name instead. Use substr() for this.

```
iris
head(iris,5)
iris
# iris is already available in your workspace

# Convert iris to a data.table: DT
DT <- data.table(iris)
# or DT <- as.data.table(iris)
# str(DT)

# For each Species, print the mean Sepal.Length
DT[, mean(Sepal.Length), by = Species]

# Print mean Sepal.Length, grouping by first letter of Species
DT[, mean(Sepal.Length), by = substr(Species,1,1)]
#help(substr)
```

## Using .N and by

You saw earlier that .N can be used in i and that it designates the number of rows in DT. There, it is typically used for returning the last row or an offset from it. .N can be used in j too and designates the number of rows in this group. This becomes very powerful when you use it in combination with by.

DT, a data.table version of iris, is already loaded in your workspace, so you can start experimenting right away. In this exercise, you will group by sepal area. Though sepals aren't rectangles, just multiply the length by the width to calculate the area.

Instructions
Group the specimens by Sepal area (Sepal.Length * Sepal.Width) to the nearest 10 cm2cm2. Count how many occur in each group by specifying .N in j. Simply print the resulting data.table. Use the template in the sample code by filling in the blanks.
Copy and adapt the solution to the above question, to name the columns Area and Count, respectively.

```
# data.table version of iris: DT
DT <- as.data.table(iris)

# Group the specimens by Sepal area (to the nearest 10 cm2) and count how many occur in each group. .N can be used in j and designates the number of rows in this group
DT[, .N, by = 10 * round(Sepal.Length * Sepal.Width / 10)]

# Now name the output columns `Area` and `Count`
DT[, .(Count = .N), by = .(Area = 10 * round(Sepal.Length * Sepal.Width / 10))]
```

## Return multiple numbers in j

In the previous exercises, you've returned only single numbers in j. However, this is not necessary. You'll experiment with this via a new data.table DT, which has already been specified in the sample code.

Instructions
Create a new data.table DT2 with 3 columns, A, B and C, where C is the cumulative sum of the C column of DT. Call the cumsum() function in the j argument, and group by .(A, B) (i.e. both columns A and B).
Select from DT2 the last two values of C using the tail() function, and assign that to column C while you group by A alone. Make sure the column names don't change.
```
# Create the data.table DT
DT <- data.table(A = rep(letters[2:1], each = 4L), 
                 B = rep(1:4, each = 2L), 
                 C = sample(8))
DT

# Create the new data.table, DT2
DT2 <- DT[, .(C = cumsum(C)), by = .(A, B)]
DT2

# Select from DT2 the last two values from C while you group by A
DT2[, .(C = tail(C, 2)), by = .(A)]
```

## data.table i,j,by

```
library(hflights)
library(data.table)
DT <- as.data.table(hflights)
DT[Month==10,mean(na.omit(AirTime)), by=UniqueCarrier]
#     UniqueCarrier        V1
#  1:            AA  68.76471
#  2:            AS 255.29032
#  3:            B6 176.93548
#  4:            CO 141.52861
#  5:            DL  92.76824
#  6:            WN  87.14947
#  7:            XE  82.44422
#  8:            OO 114.98865
#  9:            UA 166.18354
# 10:            US 137.46078
# 11:            EV 113.12273
# 12:            F9 126.55357
# 13:            FL  90.85561
# 14:            MQ 100.13054

DT[2:5]
#selects the second to the fifth row of DT

DT[UniqueCarrier == "AA"]
#Returns all those rows where the Carrier is American Airlines

DT[.N-1]
# Returns the penultimate row of DT
# .N You can use it for selecting the last row or an offset from it.

# The j part The ‘j’ part is used to select columns and do stuff with them. 
# And stuff can really mean anything. 
# All kinds of functions can be used, which is a strong point of the data.table package.

DT[, mean(na.omit(ArrDelay))]
[1] 7.094334

# When selecting several columns and doing stuff with them in the 'j' part, 
# you need to use the ‘.()’ notation. 
# This notation is actually just an alias to ‘list()’. 
# It returns a data table, 
# whereas not using ‘.()’ only returns a vector, as shown above.

DT[, .(mean(na.omit(DepDelay)), mean(na.omit(ArrDelay)))]
# V1       V2
# 9.444951 7.094334

# Another useful feature which requires the ‘.()’ notation 
# allows you to rename columns inside the DT[…] command.

DT[, .(Avg_ArrDelay = mean(na.omit(ArrDelay)))]
# Avg_ArrDelay
# 7.094334

DT[, .(Avg_DepDelay = mean(na.omit(DepDelay)),
avg_ArrDelay = mean(na.omit(ArrDelay)))]
# Avg_DepDelay Avg_ArrDelay
# 9.444951     7.094334

# Of course, new column names are not obligatory. 
# Combining the above about ‘i’ and ‘j’ gives:

DT[UniqueCarrier=="AA", 
      .(
      Avg_DepDelay = mean(na.omit(DepDelay)),
      Avg_ArrDelay = mean(na.omit(ArrDelay)),
      plot(DepTime,DepDelay,ylim=c(-15,200)),
      abline(h=0))
      ]

# Avg_DepDelay Avg_ArrDelay V3    V4
# 6.390144     0.8917558    NULL  NULL

# Here we calculated the average delay before departure, 
# but grouped by where the plane is coming from.
DT[,mean(na.omit(DepDelay)),by=Origin]
# Origin  V1
# IAH     8.436951
# HOU    12.837873



DT[,.(Avg_DepDelay_byWeekdays = mean(na.omit(DepDelay))), by=.(Origin,Weekdays = DayOfWeek < 6)]

```





