# R_Statistic_Test.md

Two Sample t-test and  Exact Two-Sample Fisher-Pitman Permutation Test

> http://www.jianshu.com/p/4b0e6fa098a5

```
# 载入包，并生成数据
library(coin)
score <- c(40, 57, 45, 55, 58, 57, 64, 55, 62, 65)
treatment <- factor(c(rep("A", 5), rep("B", 5)))
mydata <- data.frame(treatment, score)

# 查看数据look the data
mydata

# 对独立样本进行T检验
t.test(score ~ treatment, data = mydata, var.equal = TRUE)

#  Two Sample t-test
# 
# data:  score by treatment
# t = -2.345, df = 8, p-value = 0.04705
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#  -19.0405455  -0.1594545
# sample estimates:
# mean in group A mean in group B 
#            51.0            60.6

```

对独立样本进行置换检验，结果表明，T检验显著，
但是置换检验不显著，置换结果更准确，需要增加样本数。

```
oneway_test(score ~ treatment, data = mydata, distribution = "exact")
#     Exact Two-Sample Fisher-Pitman Permutation Test
# 
# data:  score by treatment (A, B)
# Z = -1.9147, p-value = 0.07143
# alternative hypothesis: true mu is not equal to 0
```

## 构建数据框
### 构建数据框第一种方法
```
商品名称<-c("鼠标","键盘","mp3","4gu盘")
平均月销量<-c(124,90,88,120)
sale<-data.frame(商品名称,平均月销量)
 sale

#   商品名称 平均月销量
# 1     鼠标        124
# 2     键盘         90
# 3      mp3         88
# 4    4gu盘        120
```

### 构建数据框第二种方法
```
mylist<-list(商品名称=商品名称,平均月销量=平均月销量)#先创建列表
mylist
$商品名称
[1] "鼠标" "键盘" "mp3" "4gu盘"
$平均月销量
[1] 124 90 88 120

sale<-data.frame(mylist)#在创建数据框
sale
# 商品名称 平均月销量
# 1 鼠标 124
# 2 键盘 90
# 3 mp3 88
# 4 4gu盘 120

str(sale)#以简洁的方式对任意的R对象进行总结
# 'data.frame': 4 obs. of 2 variables:
# $ 商品名称 : Factor w/ 4 levels "4gu盘","mp3",..: 4 3 2 1
# $ 平均月销量: num 124 90 88 120
```


