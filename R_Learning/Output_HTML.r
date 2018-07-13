rm(list = ls(all = TRUE))

## load package in a safe way

# ```{r load package in a safe way}
# # Load data.table package
# if(!suppressWarnings(require(c('data.table','rvest', 'dplyr'))))
# {
#   install.packages(c('data.table','rvest', 'dplyr'))
#   require(c('data.table','rvest', 'dplyr'))
# }
# 
# ```

library(rvest)
library(data.table)
library(dplyr)

#这里是导入网址。研究一下amazon的顺序，直接导入就好
id <- 1:5

# 销售爬升最快榜： http://www.amazon.cn/gp/movers-and-shakers/digital-text/
# https://www.amazon.cn/gp/movers-and-shakers/digital-text/ref=zg_bsms_pg_2?ie=UTF8&pg=2
url_increase_fast<-paste0(
  "http://www.amazon.cn/gp/movers-and-shakers/digital-text/ref=zg_bsms_pg_",
  id,
  "?ie=UTF8&pg=",
  id)
# url_increase_fast


# 新品榜： http://www.amazon.cn/gp/new-releases/digital-text/
# https://www.amazon.cn/gp/new-releases/digital-text/ref=zg_bsnr_pg_2?ie=UTF8&pg=2

url_newest<-paste0(
  "http://www.amazon.cn/gp/new-releases/digital-text/ref=zg_bsnr_pg_",
  id,
  "?ie=UTF8&pg=",
  id)
# url_newest

url<-c(url_increase_fast,url_newest)
#这里编写readdata函数，读取网页内容。里面有些不常用的字段，为了最后导出效果好看，我没全部都导。
#有额外需要的可以自己改编，譬如分类啊，好评率啊等等。对我来说，知道价格、书名就够了

readdata<-function(i){
  web<-read_html(url[i],encoding="UTF-8")
  
  # url[1]
  # title<-web %>% html_nodes("a.div.p13n-sc-truncated") %>% html_text()
  # web %>% html_nodes("a") %>% html_nodes("div")  %>% html_nodes(".p13n-sc-truncated")%>% html_text()
  # web %>% html_nodes("div") %>% html_nodes("ol") %>% html_nodes("li") %>% html_text()
  # web %>% html_nodes("a>div") %>% html_text()
  # web %>% html_nodes("a>div") %>% html_text()
  # web %>% html_nodes("div") %>% html_nodes("img") %>% html_attr("alt")
  # web %>% html_nodes("div.p13n-sc-truncate") %>% html_attr("class")
  # web %>% html_nodes("div.p13n-sc-line-clamp-1") %>% html_text()
  # web %>% html_nodes("div.p13n-sc-line-clamp-2") %>% html_text()  
  
  title <- web %>% html_nodes("div.p13n-sc-truncate") %>% html_text()
  # head(title)
  # [1] "\n            福利国家之后\n        "                                                                                                        
  # [2] "\n            基因：不平等的遗传\n        "                                                                                                  
  # [3] "\n            无人驾驶，十万亿美元的大饼怎么分？ (《经济学人·商论》选辑)\n        "                                                          
  # [4] "\n            侠隐（姜文电影《邪不压正》原著小说）\n        "                                                                                
  # [5] "\n            死灵之书（不只是克苏鲁神话！洛夫克拉夫特小说全集！《冰与火之歌》《普罗米修斯》《水形物语》《魔兽世界》的灵感来源！）\n        "
  # [6] "\n            科学学习：斯坦福黄金学习法则\n   
  
  # 移除 '\n'
  title <- gsub("\n", "", title)
  # 移除 ' '
  title <- gsub(" ", "", title)
  # head(title)
  # [1] "福利国家之后"                                                                                                        
  # [2] "基因：不平等的遗传"                                                                                                  
  # [3] "无人驾驶，十万亿美元的大饼怎么分？(《经济学人·商论》选辑)"                                                           
  # [4] "侠隐（姜文电影《邪不压正》原著小说）"                                                                                
  # [5] "死灵之书（不只是克苏鲁神话！洛夫克拉夫特小说全集！《冰与火之歌》《普罗米修斯》《水形物语》《魔兽世界》的灵感来源！）"
  # [6] "科学学习：斯坦福黄金学习法则"  
  
  title_short<-substr(title,1,20)
  
  # web %>% html_nodes("span.p13n-sc-price") %>% html_text()
  
  price <-
    as.numeric(gsub(
      "￥",
      "",
      web %>% html_nodes("span.p13n-sc-price") %>% html_text()
    ))
  price
  
  
  ranking_movement <-
    # web %>% html_nodes("span .zg-sales-movement") %>% html_text()
    web %>% html_nodes("span>span.zg_salesMovement") %>% html_text()
  ranking_movement
  
  # zg-badge-text
  
  rank_number <- web %>% html_nodes("div>span") %>% html_text()
  rank_number  
  # as.numeric(gsub("\\.","",web %>% html_nodes("span.zg_rankNumber") %>% html_text()))
  
  
  
  #新书榜里没有销售变动记录，所以记为NA
  if (length(ranking_movement)==0) {
    ranking_movement=rep(NA,20)
    rank_number=rep(NA,20)}
  
  link<-gsub("\\\n","",web %>% html_nodes("div.zg_title a") %>% html_attr("href"))
  ASIN<-sapply(strsplit(link,split = "/dp/"),function(e)e[2])
  img<-web %>% html_nodes("div.zg_itemImage_normal img")  %>% html_attr("src")
  
  #这里加上html代码
  img_link<-paste0("<img src='",img,"'>")
  title_link<-paste0("<a href='",link,"'>",title_short,"</a>")
  
  #合并数据
  combine<-data.table(img_link,title_link,price,ranking_movement)
  setnames(combine,c("图像","书名","价格","销售变动"))
  
  #以防被封IP，设为5秒跑一次数据。
  Sys.sleep(5)
  combine
}

#做一个循坏开始跑数
final <- data.table()
for (i in 1:10) {
  final <- rbind(final, readdata(i))
  print(i)
}

#这里编写一个函数，把data.table转化为html_table
#要点请查看w3school，table页，以<table>开始，表头是<th>，行与行之间是<tr>
#主要就是sapply, apply，paste的应用啦……就是把数据框先加<td>，再加<tr>，最后外面套一层<table>
transfer_html_table<-function(rawdata){
  title<-paste0("<th>",names(rawdata),"</th>")
  content<-sapply(rawdata,function(e)paste0("<td>",e,"</td>"))
  content<-apply(content,1,function(e) paste0(e,collapse = ""))
  content<-paste0("<tr>",content,"</tr>")
  bbb<-c("<table border=1><tr>",title,"</tr>",content,"</table>")
  bbb
}

#这里应用transfer_html_table函数，把榜单输出为html表格
final_less1<-transfer_html_table(rawdata=final %>% filter(价格<=1))
write(final_less1,"~//Kindle-低于1元特价书.html")


final_1_2<-transfer_html_table(rawdata=final %>% filter(价格>1 & 价格<=2))
write(final_1_2,"~//Kindle_1-2元特价书.html")

final_2_5<-transfer_html_table(rawdata=final %>% filter(价格>2 & 价格<=5))
write(final_2_5,"~//Kindle_2-5元特价书.html")




library(ggplot2)
library(plotly)
p <- ggplot(data = diamonds, aes(x = cut, fill = clarity)) +
  geom_bar(position = "dodge")
ggplotly(p)


d <- diamonds[sample(nrow(diamonds), 500), ]
plot_ly(d, x = d$carat, y = d$price, 
        text = paste("Clarity: ", d$clarity),
        mode = "markers", color = d$carat, size = d$carat)




# <a target="_blank" href="//www.123.com/hospital/3300/">123</a>
# 我写的html_attrs(“href”)  提出不出来， 提示参数错误;
# 应该怎样 提取 “www.123.com/hospital/3300/” 这个链接？？？

# install.packages(\"rvest\")
library(rvest) # 第一步
# 这里先自定义两个函数
# 第1个：自定义读取单个商品url地址函数 
read.url<-function(category){ 
# 解析网页 
webs<-read_html(category,encoding ="gbk")

urls<-webs %>%
html_nodes("div.con.shoplist") %>% 
html_nodes("ul") %>%
html_nodes("li") %>%
html_nodes("a.pic") %>%
html_attr("href")

return(urls)
}

# ------

MyData <- function(address){
web <- read_html(address)

#Name
name <- web %>%
  html_nodes("#aiv-contend-title") %>%
  html_text()
name <- trimws(strsplit(name, "\n")[[1]][2])

#year
year <- web %>%
  html_nodes("#aiv-contend-title span") %>%
  html_text()
year <- as.numeric(year[1])

#stars
stars <- web %>%
  html_nodes("#avgRating span") %>%
  html_text()
stars <- as.numeric(strsplit(strsplit(stars, "\n")[[1]][2],"")[[1]][1])

#director
director <- web %>%
  html_nodes("#avgRating tr:nth-child(2) a") %>%
  html_text()

MOVIE <- list(name, year, stars, director)
                    
MOVIE                 
}





