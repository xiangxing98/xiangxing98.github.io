# Load package in a safe way

## Load data.table package

```
# Load data.table package
if(!suppressWarnings(require(data.table)))
{
    install.packages('data.table')
    require(data.table)
}
```

## Set Local Repositories

```{r}
#windows Rconsole
file.path(R.home('etc'), 'Rconsole')
# [1] "D:/PROGRA~1/R/R-33~1.3/etc/Rconsole"

#set repos
options(repos = c(CRAN = "http://mirrors.tuna.tsinghua.edu.cn/CRAN/",
                  CRANextra = "http://mirrors.xmu.edu.cn/CRAN/"))
# https://cloud.r-project.org/

# on windows, for R-2.14.0.  In this file you will even find an example of setting the CRAN mirror.  
# You can edit here is you have root or administrative privileges, but more likely you will copy it and place it in the personal .Rprofile file in your home directory.
# Inside the command is simple, this is copied straight from the Rprofile.site file.

local({
  r <- getOption("repos")
  r["CRAN"] <- "http://cran.cnr.berkeley.edu/"
  options(repos = r)
})
```

## 用搜索路径来查看所有已加载的包
```{r}
search()
View(installed.packages())

# R出厂的包 在CRAN包库中，要访问其他存储库
setRepositories() 

# 下载 github上的包
install.packages("devtools")
install.packages("devtools")
install_github("knitr","yihui")  

```

## 10 usefull packages in R

The yhat blog lists 10 R packages they wish they'd known about earlier. 

Drew Conway calls them "10 reasons to always start your analysis in R". 

They're all very useful R packages that every data scientist should be aware of. 

They are:

1. sqldf (for selecting from data frames using SQL) 
2. forecast (for easy forecasting of time series) 
3. plyr (data aggregation) or dplyr 
4. stringr (string manipulation) 
5. Database connection packages RPostgreSQL, RMYSQL, RMongo, RODBC, RSQLite 
6. lubridate (time and date manipulation) 
7. ggplot2 (data visulization) 
8. qcc (statistical quality control and QC charts) 
9. reshape2 (data restructuring) 
10. randomForest (random forest predictive models) 
