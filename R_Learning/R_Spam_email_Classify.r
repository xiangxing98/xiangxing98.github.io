rm(list = ls())  
if(require(tm) == FALSE) {  
  install.packages("tm")  
  library(tm)  
}  
if(require(ggplot2) == FALSE) {  
  install.packages("ggplot2")  
  library(ggplot2)  
}  


spam.path <- "email_classification/data/spam/"             #垃圾邮件1  
spam2_path <- "email_classification/data/spam_2/"          #垃圾邮件2  
easyham.path <- "email_classification/data/easy_ham/"      #容易与垃圾邮件区分的非垃圾邮件1  
easyham2.path <- "email_classification/data/easy_ham_2/"   #容易与垃圾邮件区分的非垃圾邮件2  
hardham.path <- "email_classification/data/hard_ham/"      #很难与垃圾邮件区分的非垃圾邮件1  
hardham2.path <- "email_classification/data/hard_ham_2/"   #很难与垃圾邮件区分的非垃圾邮件2  


###### function:get.msg ###########################  
# target:邮件中抽取正文  
# method:每个邮件正文和头部信息是通过一个空白行分割  
# arguments:character 邮件文件路径  
# return:character 邮件正文内容  
get.msg <- function(path) {  
  con <- file(path, open = "rt", encoding = "latin1")  
  texts <- readLines(con)  
  breakLineNum <- which(texts == "")[1]  
  
  if( is.na(breakLineNum) || is.nan(breakLineNum) || is.infinite(breakLineNum)) {  
    cat(paste(path, breakLineNum,  "", sep=" "))  
    breakLineNum <- 0  
  }    
  msg <- texts[seq(breakLineNum, length(texts), 1)]  
  close(con)  
  return(paste(msg, collapse = "\n"))  
}  
###################################################  
spam.docs <- dir(spam.path) #获取所有的垃圾邮件  
spam.docs <- spam.docs[which(spam.docs != "cmds")] #排除一部分不想要的邮件  
all.spam <- sapply(spam.docs, function(p) get.msg(paste(spam.path, p, sep=""))) #处理所有的邮件，提取正文部分的内容  


ham.docs <- dir(easyham.path)  
ham.docs <- ham.docs[which(ham.docs != "cmds")]  
ham.docs <- ham.docs[1:500]  
all.ham <- sapply(ham.docs, function(p) get.msg(paste(easyham.path, p, sep="")))  


############# funciont get.tdm  ###################  
# target: 获取词频矩阵  
# method: 通过tm包中携带的函数获取一系列文本的词频矩阵  
# arguments: vector 文本数组  
# return: matrix 词频数组  
get.tdm <- function(doc.vec) {  
  doc.corpus <- Corpus(VectorSource(doc.vec))  
  control <- list(stopwords = TRUE, removePunctuation = TRUE, removeNumbers = TRUE, minDocFreq = 2)  
  doc.tdm <- TermDocumentMatrix(doc.corpus, control)  
  return(doc.tdm)  
}  


###################################################  
tdm <- get.tdm(all.spam)  
spam.matrix <- as.matrix(tdm)       #词文本矩阵，即这个词在某个文本中出现的次数 稀疏矩阵  
spam.counts <- rowSums(spam.matrix) #每一行和，即单词在所有文本中出现的总次数  
spam.df <- data.frame(cbind(names(spam.counts), as.numeric(spam.counts)), stringsAsFactors = FALSE)  
names(spam.df) <- c('term','frequency')  
spam.df$frequency <- as.numeric(spam.df$frequency)  
spam.occurrence <- sapply(1:nrow(spam.matrix),  
                          function(i) {length(which(spam.matrix[i,] > 0)) / ncol(spam.matrix)})  
spam.density <- spam.df$frequency/sum(spam.df$frequency)  
spam.df <- transform(spam.df, density=spam.density,   
                     occurrence=spam.occurrence)  




tdm <- get.tdm(all.ham)  
ham.matrix <- as.matrix(tdm)  
ham.counts <- rowSums(ham.matrix)  
ham.df <- data.frame(cbind(names(ham.counts), as.numeric(ham.counts)), stringsAsFactors = FALSE)  
names(ham.df) <- c('term','frequency')  
ham.df$frequency <- as.numeric(ham.df$frequency)  
ham.df$density <- ham.df$frequency/sum(ham.df$frequency)  
ham.occurrence <- sapply(1:nrow(ham.matrix), function(i) {length(which(spam.matrix[i,] > 0)) / ncol(spam.matrix)})  


ham.df$occurrence <- ham.occurrence  


head(spam.df[with(spam.df, order(-occurrence)), ])  




head(ham.df[with(ham.df, order(-occurrence)), ])  


###分类函数###  
classify.email <- function(path, traning.df, prior=0.5, c=1e-6) {  
  msg <- get.msg(path)  
  msg.tdm <- get.tdm(msg)  
  msg.freq <- rowSums(as.matrix(msg.tdm))  
  msg.match <- intersect(names(msg.freq), traning.df$terms)  
  
  if (length(msg.match) < 1) {  
    #如果一个相同的单词都没有出现，那么每个单词的概率就以默认概率的乘积  
    return(prior*c^(length(msg.freq)))  
  } else {  
    #否则出现的以出现的概率计算，没有出现的以默认概率计算，最后求乘积  
    match.probs <- traning.df$occurrence[match(msg.match, training.df$term)]  
    return(prior * prod(match.probs) * c^(length(msg.freq) - length(msg.match)))  
  }  
  
}  


hardham.docs <- dir(hardham.path)  


hardham.docs <- hardham.docs[which(hardham.docs != "cmds")]  
hardham.spamprob <- sapply(hardham.docs, function(p) {classify.email(paste(hardham.path, p, sep=""), spam.df)})  
hardham.hamprob <- sapply(hardham.docs, function(p) {classify.email(paste(hardham.path, p, sep=""), ham.df)})  


hardham.class <- ifelse(hardham.spamprob > hardham.hamprob, 'spam', 'ham')  




spam2.docs <- dir(spam2_path)  


spam2.docs <- spam2.docs[which(spam2.docs != "cmds")]  
spam2.spamprob <- sapply(spam2.docs, function(p) {classify.email(paste(spam2_path, p, sep=""), spam.df)})  
spam2.hamprob <- sapply(spam2.docs, function(p) {classify.email(paste(spam2_path, p, sep=""), ham.df)})  


spam2.class <- ifelse(spam2.spamprob > spam2.hamprob, 1, 0)  
length(spam2.class)  
length(spam2.class[which(spam2.class==0)])  