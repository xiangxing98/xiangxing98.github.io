# Concepts in Computing with Data--正则表达式（Regular Expression、regexp）

假设我们有一个字符向量，包括了三个字符串。我们的目标是从中抽取电邮地址。

R语言中很多字符函数都能识别正则表达式，而最重要的函数就是gregexpr()。
```
gregexpr
function (pattern, text, ignore.case = FALSE, perl = FALSE, fixed = FALSE, 
    useBytes = FALSE) 
{
    if (!is.character(text)) 
        text <- as.character(text)
    .Internal(gregexpr(as.character(pattern), text, ignore.case, 
        perl, fixed, useBytes))
}
<bytecode: 0x09331de4>
<environment: namespace:base>

```
该函数的第一个参数是正则表达式，前后需要用引号，对元字符进行转义时要用\\。
第二个参数是等待处理的文本。
那么用如下三行代码，我们从word字符向量中得到一个列表，
其中第一项元素中的5表示电邮地址从第5个字符位置开始，24表示电邮地址长度为24。

```
word <- c('abc noboby@stat.berkeley.edu','text with no email','first me@mything.com also you@yourspace.com')
pattern <- '[-A-Za-z0-9_.%]+@[-A-Za-z0-9_.%]+\\.[A-Za-z]+'
(gregout <- gregexpr(pattern,word))
# output
[[1]]
[1] 5
attr(,"match.length")
[1] 24
attr(,"useBytes")
[1] TRUE

[[2]]
[1] -1
attr(,"match.length")
[1] -1
attr(,"useBytes")
[1] TRUE

[[3]]
[1]  7 27
attr(,"match.length")
[1] 14 17
attr(,"useBytes")
[1] TRUE
```

下一步我们需要将电邮地址抽取出来，此时配合substr函数，即可根据需要字符串的位置来提取子集。
```
substr(word[1],gregout[[1]],gregout[[1]]+attr(gregout[[1]],'match.length')-1)

# 函数getcontent，参数s表示待处理的文本，参数g表示的是通过gregexpr函数处理后的结果。
# 这个函数我们在后面还会用到。
getcontent <- function(s,g) {
    substring(s,g,g+attr(g,'match.length')-1)
}

getcontent(word[1],gregout[[1]])
```

实际的数据抓取工作中，如何使用正则表达式。
任务目标是要抓取豆瓣电影中250部最佳电影的资料。
R代码如下：
```
url <-'http://movie.douban.com/top250?format=text'

# 获取网页原代码，以行的形式存放在web变量中
web <- readLines(url,encoding="UTF-8")
# 找到包含电影名称的行编号
name <- web[grep('<td headers="m_name">',web)+1]
# 用正则表达式来提取电影名
gregout <- gregexpr('>\\w+',name)
movie.names = 0
for (i in 1:250) {
    movie.names[i] <-getcontent(name[i],gregout[[i]])
}
movie.names <- sub('>','',movie.names)
# 找到包含电影发行年份的行编号并进行提取
year <- web[grep('<span class="year">',web)] 
movie.year <- substr(year,36,39)
# 找到包含电影评分的行编号并进行提取
score <- web[grep('<td headers="m_rating_score">',web)+1]
movie.score <- substr(score,21,23)
# 找到包含电影评价数量的行编号并进行提取
rating <- web[grep('<td headers="m_rating_num">',web)+1]
movie.rating <- sub(' *','',rating)
# 合成为数据框
movie <- data.frame(names=movie.names,year=as.numeric(movie.year),
                    score=as.numeric(movie.score),rate=as.numeric(movie.rating))
# 绘散点图
library(ggplot2)
p <- ggplot(data=movie,aes(x=year,y=score))
p+geom_point(aes(size=rate),colour='lightskyblue4',
             position="jitter",alpha=0.8)+
  geom_point(aes(x=1997,y=8.9),colour='red',size=4)


```

用散点图来观察数据，可以看到前250名电影中大部分是1980年之后发行的。

1997年和2010年发行的电影有不少精品。

而其中红色点所代表的是哪部电影你知道吗？那就是Titanic。