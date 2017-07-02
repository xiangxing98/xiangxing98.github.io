require(jsonlite)
profile <- fromJSON("HighPerformance//test_json_data.json")
str(profile)
# List of 5
# $ name   : chr "test1"
# $ n      : int 20
# $ random : chr [1:3] "rnorm" "runif" "rnorm"
# $ range  : num [1:2] 0.2 0.8
# $ columns: chr [1:3] "a" "b" "c"

data <- lapply(profile$random,function(fun) {
  rnd <- get(fun)
  val <- rnd(n=profile$n)
  val[val < profile$range[1]] <- profile$range[1]
  val[val > profile$range[2]] <- profile$range[2]
  return(val)
})
str(data)
# List of 3
# $ : num [1:20] 0.561 0.386 0.2 0.2 0.2 ...
# $ : num [1:20] 0.654 0.726 0.745 0.8 0.44 ...
# $ : num [1:20] 0.753 0.2 0.664 0.454 0.2 ...

df <- data.frame(do.call(cbind,data))
colnames(df) <- profile$columns
str(df)
# 'data.frame':	20 obs. of  3 variables:
#   $ a: num  0.561 0.386 0.2 0.2 0.2 ...
# $ b: num  0.654 0.726 0.745 0.8 0.44 ...
# $ c: num  0.753 0.2 0.664 0.454 0.2 ...

# Here we call `fromJSON` function to load the settings, 
# and call lapply to generate random numbers according to the specification 
# in a robust way. 
# The code above does not involve any piece of settings and data 
# so that we are allowed to rerun the machine by different settings 
# without having to change any bit of code.


# In some situations, our program has more than one profiles. 
# These profiles can be duplicates to each other except for a subset of settings. 
# But if we want to change a field in each profile, 
# it can be time-consuming. A decent way is to adopt profile overriding. 
# To proceed,
# we first create a default profile (default.json) that defines the template.

# {
#   "name": "default",
#   "n": 20,
#   "random": ["rnorm", "runif", "rnorm"],
#   "range": [0.2, 0.8],
#   "columns": ["a","b","c"]
# }

# Then we create another overriding profile (test2.json) 
# that only contains updates to the default one. 
# For example:
#   
# {
#   "name": "test2",
#   "n": 50,
#   "range": [0.4, 0.6]
# }

# To make it work, we use modifyList function to update the list created from 
# default.json by that from test2.json.
require(jsonlite)
profile <- modifyList(fromJSON("HighPerformance//test_json_default_default.json"),
                      fromJSON("HighPerformance//test_json_test2_data.json"))
data <- lapply(profile$random,function(fun) {
  rnd <- get(fun)
  val <- rnd(n=profile$n)
  val[val < profile$range[1]] <- profile$range[1]
  val[val > profile$range[2]] <- profile$range[2]
  return(val)
})
df <- data.frame(do.call(cbind,data))
colnames(df) <- profile$columns

# modifyList is a built-in function in R. 
# It updates a list by merging updated fields and 
# introducing new fields in the list and sublists recursively.
# 
# Now we may create several differnt set of settings 
# and operate the machine in a very flexible way.
