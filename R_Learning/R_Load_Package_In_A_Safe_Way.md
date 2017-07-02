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