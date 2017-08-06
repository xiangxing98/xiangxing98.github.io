# Tibbles

# library(tidyverse)
require(tidyverse)
vignette("tibble")

# coerce a data frame to a tibble. You can do that with as_tibble()
as_tibble(iris)
#> # A tibble: 150 × 5
#>   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
#>          <dbl>       <dbl>        <dbl>       <dbl>  <fctr>
#> 1          5.1         3.5          1.4         0.2  setosa
#> 2          4.9         3.0          1.4         0.2  setosa
#> 3          4.7         3.2          1.3         0.2  setosa
#> 4          4.6         3.1          1.5         0.2  setosa
#> 5          5.0         3.6          1.4         0.2  setosa
#> 6          5.4         3.9          1.7         0.4  setosa
#> # ... with 144 more rows

# You can create a new tibble from individual vectors with tibble(). 
# tibble() will automatically recycle inputs of length 1, and allows you to
# refer to variables that you just created, as shown below.
tibble(
  x = 1:5, 
  y = 1, 
  z = x ^ 2 + y
)
# A tibble: 5 x 3
# x     y     z
# <int> <dbl> <dbl>
#   1     1     1     2
# 2     2     1     5
# 3     3     1    10
# 4     4     1    17
# 5     5     1    26


tb <- tibble(
  `:)` = "smile", 
  ` ` = "space",
  `2000` = "number"
)
tb
# A tibble: 1 x 3
# `:)`   ` ` `2000`
# <chr> <chr>  <chr>
#   1 smile space number

# Another way to create a tibble is with tribble(), short for transposed tibble.
# tribble() is customised for data entry in code: 
#   column headings are defined by formulas (i.e. they start with ~), 
# and entries are separated by commas. 
# This makes it possible to lay out small amounts of data in easy to read form.

tribble(
  ~x, ~y, ~z,
  #--|--|----
  "a", 2, 3.6,
  "b", 1, 8.5
)
#> # A tibble: 2 × 3
#>       x     y     z
#>   <chr> <dbl> <dbl>
#> 1     a     2   3.6
#> 2     b     1   8.5

# I often add a comment (the line starting with #),
# to make it really clear where the header is.

tibble(
  a = lubridate::now() + runif(1e3) * 86400,
  b = lubridate::today() + runif(1e3) * 30,
  c = 1:1e3,
  d = runif(1e3),
  e = sample(letters, 1e3, replace = TRUE)
)
# A tibble: 1,000 x 5
# a          b     c          d     e
# <dttm>     <date> <int>      <dbl> <chr>
#   1 2017-08-03 00:48:23 2017-08-02     1 0.66708433     w
# 2 2017-08-03 16:04:44 2017-08-11     2 0.81551124     a
# 3 2017-08-03 02:36:16 2017-08-30     3 0.92895255     c
# 4 2017-08-03 19:48:45 2017-08-14     4 0.70558643     n
# 5 2017-08-03 10:53:04 2017-08-20     5 0.30914082     b
# 6 2017-08-03 17:54:51 2017-08-08     6 0.07106479     b
# 7 2017-08-03 03:23:54 2017-08-18     7 0.19524233     o
# 8 2017-08-03 16:18:37 2017-08-15     8 0.65981365     v
# 9 2017-08-03 08:21:41 2017-08-02     9 0.42560422     v
# 10 2017-08-03 18:59:18 2017-08-10    10 0.35681998     c
# ... with 990 more rows


nycflights13::flights %>% 
  print(n = 10, width = Inf)


# You can also control the default print behaviour by setting options:
# options(tibble.print_max = n, tibble.print_min = m): 
# if more than m rows, print only n rows. 
# Use options(dplyr.print_min = Inf) to always show all rows.

# Use options(tibble.width = Inf) to always print all columns, 
# regardless of the width of the screen.

nycflights13::flights %>% 
  View()

package?tibble


#SUbsetting

df <- tibble(
  x = runif(5),
  y = rnorm(5)
)

# Extract by name
df$x
#> [1] 0.434 0.395 0.548 0.762 0.254
df[["x"]]
#> [1] 0.434 0.395 0.548 0.762 0.254

# Extract by position
df[[1]]
#> [1] 0.434 0.395 0.548 0.762 0.254


# To use these in a pipe, you’ll need to use the special placeholder .
df %>% .$x
#> [1] 0.434 0.395 0.548 0.762 0.254
df %>% .[["x"]]
#> [1] 0.434 0.395 0.548 0.762 0.254


class(as.data.frame(tb))
#> [1] "data.frame"

# dplyr::filter()
# dplyr::select()

# Exercises 01
# How can you tell if an object is a tibble? 
# (Hint: try printing mtcars, which is a regular data frame).
str(mtcars)
tib_mtcars <- as_tibble(mtcars)
is.tibble(tib_mtcars);is.data.frame(tib_mtcars)
# [1] TRUE
# [1] TRUE

# Exercises 02
# Compare and contrast the following operations on a data.frame and equivalent tibble.
# What is different? Why might the default data frame behaviours cause you frustration?
df <- data.frame(abc = 1, xyz = "a")
tib <- as.tibble(df)

#data.frame
df$x
# [1] a
# Levels: a
df[, "xyz"]
# [1] a
# Levels: a
df[, c("abc", "xyz")]
# abc xyz
# 1   1   a

#tibble
tib$x
# NULL
# Warning message:
#   Unknown or uninitialised column: 'x'.
tib[, "xyz"]
# A tibble: 1 x 1
# xyz
# <fctr>
#   1      a
tib[, c("abc", "xyz")]
# A tibble: 1 x 2
# abc    xyz
# <dbl> <fctr>
#   1     1      a

# Exercises 03
# If you have the name of a variable stored in an object, 

# e.g. var <- "mpg", how can you extract the reference variable from a tibble?

tib_ex <- tibble(
  x = 1:5, 
  y = 1, 
  z = x ^ 2 + y,
  mpg = 1
);tib_ex

var <- "mpg"

tib_ex$var
# NULL
# Warning message:
#   Unknown or uninitialised column: 'var'. 
tib_ex %>% .$mpg

#works
tib_ex[var]
# A tibble: 5 x 1
# mpg
# <dbl>
#   1     1
# 2     1
# 3     1
# 4     1
# 5     1

# Exercises 04
# Practice referring to non-syntactic names in the following data frame by:
# Extracting the variable called 1.
# Plotting a scatterplot of 1 vs 2.
# Creating a new column called 3 which is 2 divided by 1.
# Renaming the columns to one, two and three.
tib_ex2 <- tibble(
  `1` = 1:10,
  `2` = `1` * 2 + rnorm(length(`1`))
)

# To refer to these variables, you need to surround them with backticks, `:
tib_ex2['1'];tib_ex2['2']
#still a tibble

tib_ex2$'1';tib_ex2$'2'
str(tib_ex2$'1') #int [1:10] 1 2 3 4 5 6 7 8 9 10
mode(tib_ex2$'1') #[1] "numeric"
is.vector(tib_ex2$'1')# [1] TRUE
class(tib_ex2$'1')#[1] "integer"

# plot()
plot(tib_ex2$'1'~tib_ex2$'2')

# Creating a new column called 3 which is 2 divided by 1.
dplyr::mutate(tib_ex2, tib_ex2$'3' = tib_ex2$'1'/tib_ex2$'2')
tib_ex2 <- tib_ex2[,'3'='1'/'2']

