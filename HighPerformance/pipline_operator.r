#pipline operator

# Pipe operator %>% is the single operator the package provides. 
# The operator basically pipes the left-hand side value forward to 
# the right-hand side expression which is evaluated according to its syntax.


# In summary, %>% supports to pipe left-hand side value
# 
# To first argument of a function
# To . in an expression
# By formula to avoid ambiguity in symbol names.
# To an expression only for its side effect.
# To an expression and save the intermediate results.
# To a symbol in order to extract that element



# You may notice that all these functions take the data as the first argument. 
# Therefore, pipeR provides a Pipe operator %>% that inserts the left-hand side value 
# to the first argument of the right-hand side function.
# 
# Basically, x %>% f(...) will be evaluated as f(x,...). 
# This allows us to rewrite the above example in a much fluent style. 
# We are enabled to build pipelines to manipulate data.

# 1. Resample from mtcars$mpg
# 2. Perform a kernel estimation of its distribution
# 3. Plot the estimated density function
mtcars$mpg %>%
  sample(size = 10000, replace = TRUE) %>% #1
  density(kernel = "gaussian") %>% #2
  plot(col = "red", main = "density of mpg (bootstrap)") #3

# Even if we realize that the data needs some filtering, 
# it is easy to add a step in the pipeline.

# 1. subset from mtcars
# 2. sample
# 3. Perform a kernel estimation of its distribution
# 4. Plot the estimated density function
mtcars %>%
  subset(mpg >= quantile(mpg, 0.05) & mpg <= quantile(mpg, 0.95)) %>%
  (mpg) %>%
  sample(size = 10000, replace = TRUE) %>%
  density(kernel = "gaussian") %>%
  plot(col = "red", main = "density of mpg (bootstrap)")

# pipe design and future development follow the following principles:
# 1. Define a set of syntax rather than symbols
# 2. Syntax should be simple, clear and intuitive
# 3. Give users full control of the piping behavior

# More specifically, pipeR
# 
# 1. Defines intuitive syntax rather than a collection of symbols to improve code readability.
# 2. Uses different syntax for each feature to reduce ambiguity.

# example

summary(sample(diff(log(rnorm(100,mean = 10))),
               size = 10000,replace = TRUE))

# rewrite with pipeline
set.seed(123)
rnorm(100, mean = 10) %>%
  log %>%
  diff %>%
  sample(size = 10000, replace = TRUE) %>%
  summary

# Note
# Note that, at each line, whenever we want to 
# continue building the pipeline with the previous result, 
# we end that line with %>>%. 
# If one line does not end up with %>>%, the pipeline ends.
mtcars$mpg %>%
  plot

mtcars$mpg %>%
  plot(col = "red")

# Sometimes the value on the left is needed at multiple places. 
# In this case you can use . to represent it anywhere in the function call.
# 
# Plot mtcars$mpg with a title indicating the number of points.

mtcars$mpg %>%
  plot(col="red", main=sprintf("number of points: %d",length(.)))

# Take a sample from the lower letters of half the population.
letters %>%
  sample(size = length(.)/2)
# [1] "p" "j" "o" "x" "q" "e" "z" "u" "i" "l" "f" "a" "m

# here are situations where one calls a function in a namespace with ::. 
# In this case, the call must end up with parentheses with or without parameters.

mtcars$mpg %>%
  stats::median()

require("graphics")
mtcars$mpg %>%
  graphics::plot(col = "red")

# The same rule also applies when piping a value to a function in a list.
functions <- list(average = function(x) mean(x))
mtcars$mpg %>% functions$average()
mtcars$mpg %>% functions[["average"]]()

mtcars %>%
  lm(mpg ~ cyl + wt)
# Error in as.data.frame.default(data) : 
#   cannot coerce class ""formula"" to a data.frame

# 指定参数名
mtcars %>%
  lm(formula = mpg ~ cyl + wt)
# use {} and .
mtcars %>%
{ lm(mpg ~ cyl + wt, data = .) }
# or use () and .
mtcars %>%
  ( lm(mpg ~ cyl + wt, data = .) )

#The difference between {} and () used above is
# 1. {} accepts more than one expressions within the braces and 
# its value is determined by the last one; 
# but () accepts only one expression.
# 2. {} has only one feature: pipe to . 
# in the enclosed expression while () has more features 
# (we will cover them soon).
mtcars %>% {
  model <- lm(mpg ~ wt + cyl, data = .)
  summ <- summary(model)
  summ[c("r.squared","adj.r.squared")]
}


mtcars %>% 
  lm(formula = mpg ~ wt + cyl) %>%
  summary %>% {
    if(.$r.squared >= 0.8) {
      return("Model A")
    }
    cat("Model B should be considered.\n")
    "Model B"
  }


# One thing to notice is that {} is more flexible than previously demonstrated.
# It also allows using %>>% within the braces as well as causing side effect 
# such as plotting graphics.
mtcars %>% {
  par(mfrow=c(1,2))
  .$mpg %>% plot(col = "red", main="mtcars (mpg)")
  .$mpg %>% hist(main = "distribution")
}

mtcars %>% {
  par(mfrow=c(1,2))
  .$mpg %>% plot(col = "red", main=sprintf("mtcars (mpg: %d)",length(.)))
  .$mpg %>% hist(main = "distribution")
}
# It should be obvious that . 
# below par() belong to the first %>>% that works with mtcars 
# while . in length() belong to the operator that works with .$mpg so that 
# it can correctly show the length of mpg (32) rather than that of mtcars (11).

length(mtcars)
# [1] 11

length(mtcars$mpg)
# [1] 32

density_plot <- mtcars$mpg %>%
  sample(size = 10000, replace = TRUE) %>%
  (function(kernel) {
    . %>%
      density(kernel = kernel) %>%
      plot(main = sprintf("%s kernel", kernel))
  })

par(mfrow=c(1,3))
density_plot("gaussian")
density_plot("rectangular")
density_plot("triangular")

1:10 %>% (function(x,pow) x^pow)(2)
# [1]   1   4   9  16  25  36  49  64  81 100

mtcars %>%
  lm(formula = mpg ~ wt + cyl) %>%
  (function(model, warn_level) {
    if(summary(model)$r.squared < warn_level)
      warning("r.squared is too low", call. = FALSE)
    model
  })(0.9) %>%
  coef
# (Intercept)          wt         cyl 
# 39.686261   -3.190972   -1.507795 
# Warning message:
#   r.squared is too low 




# Extract element
list(a=1,b=2) %>% (a) # list(a=1,b=2)[["a"]]










