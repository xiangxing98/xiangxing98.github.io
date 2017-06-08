---
title: "Getting and Cleaning Data"
output: html_notebook
---

## 1. Download Data
```{r}
if(!file.exists("data")) {
  dir.create("data")}
fileUrl<-"https://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD"
download.file(fileUrl,destfile="./data/cameras.csv",method="curl")
list.files("./data")
```

## 2. Reading Local File （.csv）
```{r}
cameraData<-read.table("./data/cameras.csv",sep=",",header=TRUE)
head(cameraData)
```

## 3. Reading Excel File （.xlsx）
```{r}
library(xlsx)
cameraData<-read.xlsx("./data/cameras.xlsx",sheetIndex=1,header=TRUE)
head(cameraData)

## Reading specific rows and columns
colIndex<-2:3
rowIndex<-1:4
cameraDataSubset<-read.xlsx("./data/cameras.xlsx",sheetIndex=1,colIndex=colIndex,rowIndex=rowIndex)
cameraDataSubset
```

## 4. Reading XML and HTML
```{r}
library(XML)
fileUrl<-"http://www.w3schools.com/xml/simple.xml"
doc<-xmlTreeParse(fileUrl,useInternal=TRUE)
rootNode<-xmlRoot(doc)
xmlName(rootNode)   #查看文件标题
names(rootNode)#查看所有子主题
rootNode[[1]]  #查看子主题第一级
rootNode[[1]][[1]]  #查看子主题第一级的第一个Element
xmlSApply(rootNode,xmlValue)  #查看所有Element的Value
```

### XPath：
```{r}
# /nodeTop level node
# //nodeNode at any level
# node[@attr-name]Node with an attribute name
# node[@attr-name='bob']Node with attribute name attr-name='bob'
# Information from:http://www.stat.berkeley.edu/~statcur/Workshop2/Presentations/XML.pdf

xpathSApply(rootNode,"//name",xmlValue)
xpathSApply(rootNode,"//price",xmlValue)
fileUrl <- "http://espn.go.com/nfl/team/_/name/bal/baltimore-ravens"
doc <- htmlTreeParse(fileUrl,useInternal=TRUE)
scores <- xpathSApply(doc,"//li[@class='score']",xmlValue)
teams <- xpathSApply(doc,"//li[@class='team-name']",xmlValue)
scores
```

## 5. Reading JSON
```{r}
library(jsonlite)
jsonData<fromJSON("https://api.github.com/users/jtleek/repos")
names(jsonData)
jsonData$name
names(jsonData$owner)
jsonData$owner$login

#Writing data frames to JSON
myjson<-toJSON(iris,pretty=TRUE)
cat(myjson)

#Convert back to JSON
iris2<-fromJSON(myjson)
head(iris2)
```

## 6. Data Table
```{r}
library(data.table)

DF=data.frame(x=rnorm(9),y=rep(c("a","b","c"),each=3),z=rnorm(9))
head(DF,3)
DT=data.table(x=rnorm(9),y=rep(c("a","b","c"),each=3),z=rnorm(9))head(DT,3)

# See all data tables in Memory
tables()

# Subsetting rows
DT[2,]
DT[DT$y=="a",]   #选出y＝a的
DT[c(2,3)]  #选出行12，列123

# Calculating values for variables with expressions
DT[,list(mean(x),sum(z))]  #返回x的mean，z的sum两个值

# Adding new columns
DT[,w:=z^2]

# 多重操作，tmp意指中间变量
DT[,m:={tmp<-(x+z); log2(tmp+5)}]

# plyr like operations
DT[,a:=x>0]  #增加一个变量 true false
DT[,b:=mean(x+w),by=a]  #by语句

# Special Variable
# .N  An integer, length 1, containing the number of elements of a factor level

set.seed(123);
DT<-data.table(x=sample(letters[1:3],1E5,TRUE))
DT[, .N,by=x]

# Keys （重要）
DT<-data.table(x=rep(c("a","b","c"),each=100),y=rnorm(300))
setkey(DT,x)
DT['a'] 

# Fread指令 Fast reading
big_df<-data.frame(x=rnorm(1E6),y=rnorm(1E6))
file<-tempfile()write.table(big_df,file=file,row.names=FALSE,col.names=TRUE,sep="\t",quote=FALSE)
system.time(fread(file))

```





This is an [R Markdown](http://rmarkdown.rstudio.com) Notebook. When you execute code within the notebook, the results appear beneath the code. 

Try executing this chunk by clicking the *Run* button within the chunk or by placing your cursor inside it and pressing *Ctrl+Shift+Enter*. 

```{r}
plot(cars)
```

Add a new chunk by clicking the *Insert Chunk* button on the toolbar or by pressing *Ctrl+Alt+I*.

When you save the notebook, an HTML file containing the code and output will be saved alongside it (click the *Preview* button or press *Ctrl+Shift+K* to preview the HTML file).


