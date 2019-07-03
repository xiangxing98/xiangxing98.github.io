# Select Element in Matrix

> 2017/05/06 updated by Stone.Hou [Back to My Github Home Page](https://xiangxing98.github.io/)

## all_wars_matrix is available in your workspace
```
all_wars_matrix
```

## Select the non-US revenue for all movies
```
non_us_all <- all_wars_matrix[,2]
```

## Average non-US revenue
```
mean(non_us_all)
```

## Select the non-US revenue for first two movies
```
non_us_some <- non_us_all[1:2]
```

## Average non-US revenue for first two movies
```
mean(non_us_some)
```