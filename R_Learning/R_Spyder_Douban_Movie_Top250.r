library(RSQLite)
library(RCurl)
library(XML)
library(stringr)


setwd('D:\\Rscript\\sqlite')
sqlite<-dbDriver('SQLite')
con<-dbConnect(sqlite,'douban.db3')
create_sql<-"create table if not exists 'test' (title varchar(250),content varchar(250))"
res<-dbGetQuery(con,create_sql)

header<-str_c(
  "Accept"="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Host"="movie.douban.com",
  "User-Agent"= "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
  "Accept-Encoding"="gzip,deflate,br",
  "Connection"="keep-alive",
  "Cache-Control"="max-age=0"
)
handle<-getCurlHandle(httpheader=header,followlocation=TRUE)
urls<-str_c("https://movie.douban.com/top250?start=",seq(0,225,25),"&filter=")

yichang<-function(x){
  content<-xmlValue(x)
  content<-ifelse(is.null(content),'not',content)
  return(content)
}


gethtml<-function(x){
  page<-getURL(x,curl=handle)
  html_page<-htmlParse(page)
  #获取title
  
  for(i in 1:25){
    #title
    title_xpath<-str_c("//ol[@class='grid_view']/li[",i,"]/div/div[2]/div[1]/a")
    title<-str_replace_all(str_trim(xpathSApply(html_page,title_xpath,xmlValue)),' ','')
    #content
    content_xpath<-str_c("//ol[@class='grid_view']/li[",i,"]/div/div[2]/div[2]/p[@class='quote']/span/text()")
    content<-xpathSApply(html_page,content_xpath,fun = yichang)
    #insert database
    insert_sql<-str_c('insert into test values','("',title,'","',content,'")')
    dbGetQuery(con,insert_sql)
    
  }
}

lapply(urls, gethtml)
dbDisconnect(con)
