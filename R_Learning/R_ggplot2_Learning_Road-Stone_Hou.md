# 201706 ggplot2 Learning Road-Stone_Hou.md

- Grammar of Graphics

卤戮脰脺碌脛脛脷脠脻露脭脫娄ggplot2脛脟卤戮脢茅碌脛碌脷3脮脗 录貌脪陋陆茅脡脺脕脣grammar of graphics碌脛脌铆脗脹禄霉麓隆 禄霉卤戮脡脧脛驴碌脛脢脟陆篓脕垄脪禄脤脳脫茂路篓 脢鹿碌脙脠脦潞脦脪禄赂枚脥录露录驴脡脪脭脦篓脪禄碌脴脫脙脮芒脤脳脫茂路篓脙猫脢枚鲁枚脌麓

脮芒脮脗禄霉卤戮脙禄露脕露庐 潞贸脨酶脮脗陆脷禄谩路脰卤冒脧锚脧赂陆茅脡脺脙驴脪禄虏驴路脰 驴脡脪脭碌陆脢卤脭脵露脭卤戮脮脗脛脷脠脻陆酶脨脨虏鹿鲁盲

aesthetic:
掳眉脌篓潞谩脰谩脳脻脰谩脳酶卤锚 卤锚脰戮麓贸脨隆隆垄脩脮脡芦潞脥脨脦脳麓

geom:
掳眉脌篓脪脭脧脗录赂脰脰
point, bar, boxplot, line

scaling:
禄霉卤戮脡脧脢脟掳脩脦脪脙脟碌脛脢媒戮脻脳陋禄炉脦陋碌莽脛脭驴脡脢露卤冒碌脛脢媒戮脻
卤脠脠莽陆芦脳酶卤锚脫鲁脡盲碌陆[0, 1]碌脛脪禄赂枚脢媒 陆芦脩脮脡芦脫鲁脡盲碌陆脠媒脦卢脩脮脡芦驴脮录盲脰脨碌脛脪禄赂枚碌茫 陆芦脨脦脳麓脫鲁脡盲脦陋脪禄赂枚脮没脢媒

脪禄赂枚脥录掳眉脌篓脠媒赂枚虏驴路脰:
1) data: 脪虏戮脥脢脟geom
2) scales and coordinate system: 掳眉脌篓脳酶卤锚脰谩潞脥脥录脌媒
3) plot annotations: 卤鲁戮掳潞脥卤锚脤芒

Scaling路脰脦陋脠媒赂枚虏驴路脰: transforming, training, mapping

Layers:
Scales:
Coordinate system:
Faceting:

脢媒戮脻陆谩鹿鹿:
脙驴赂枚脥录掳眉脌篓脪脭脧脗录赂赂枚虏驴路脰
data, mapping, layers, scales, coordinates, facet, options.

脦脪麓脫脮芒脰脺驴陋脢录虏脦录脫脧碌脌茂碌脛脪禄赂枚鹿脴脫脷ggplot2碌脛study group
脣霉脪脭脦脪脧拢脥没脛脺掳脩脙驴麓脦碌脛脰梅脪陋脛脷脠脻脪脭卤脢录脟碌脛脨脦脢陆脮没脌铆脧脗脌麓
脛脷脠脻脢脟禄霉脫脷脮芒卤戮脢茅[ggplot2: Elegant Graphics for Data Analysis](http://www.amazon.com/dp/0387981403)
脕铆脥芒戮脻脣碌脮芒卤戮脪虏脢脟赂枚虏禄麓铆碌脛虏脦驴录R Graphics Cookbook(http://www.amazon.com/dp/1449316956)

脧脗脙忙脢脟ggplot2碌脛脪禄脨漏脦脛碌碌潞脥github脡脧碌脛脭麓麓煤脗毛
http://docs.ggplot2.org/current/
https://github.com/hadley/ggplot2

卤戮脝陋脦脛脮脗脡忙录掳ggplot2: Elegant Graphics for Data Analysis 脰脨碌脛碌脷露镁脮脗
脭脷脮媒脢陆驴陋脢录脩搂脧掳ggplot2脙眉脕卯脰庐脟掳 脦脪脙脟脢脳脧脠脤脰脗脹qplot
qplot脢脟quick plot碌脛脣玫脨麓 脰录脭脷脫脙脳卯录貌露脤碌脛脙眉脕卯禄颅鲁枚脦脪脙脟脣霉脨猫碌脛脥录

==========

1. 脢媒戮脻

脢脳脧脠脭脷R脰脨掳虏脳掳ggplot2
install.packages("ggplot2")
library(ggplot2)

脦脪脙脟脢鹿脫脙碌脛脢媒戮脻
X <- read.delim("http://www.stat.ubc.ca/~rickw/gapminderDataFiveYear.txt")
str(X)

'data.frame':	1704 obs. of  7 variables:
 $ country  : Factor w/ 142 levels "Afghanistan",..: 1 1 1 1 1 1 1 1 1 1 ...
 $ year     : int  1952 1957 1962 1967 1972 1977 1982 1987 1992 1997 ...
 $ pop      : num  8425333 9240934 10267083 11537966 13079460 ...
 $ continent: Factor w/ 5 levels "Africa","Americas",..: 3 3 3 3 3 3 3 3 3 3 ...
 $ lifeExp  : num  28.8 30.3 32 34 36.1 ...
 $ gdpPercap: num  779 821 853 836 740 ...
 $ year.fac : Factor w/ 12 levels "1952","1957",..: 1 2 3 4 5 6 7 8 9 10 ...

==========

2. qplot禄霉卤戮脫脙路篓

qplot脳卯录貌碌楼碌脛脢鹿脫脙路陆路篓潞脥R base脰脨碌脛plot禄霉卤戮脪禄脩霉 驴脡脪脭脫脙脌麓禄颅脡垄碌茫脥录
qplot(gdpPercap, lifeExp, data=X)


脢鹿脫脙 color = year 驴脡脪脭陆芦赂脙卤盲脕驴脫脙虏禄脥卢脩脮脡芦卤锚脢戮鲁枚脌麓
脮芒脌茂year脢脟赂枚脕卢脨酶碌脛卤盲脕驴 脣霉脪脭脩脮脡芦脪脭脝脳碌脛脨脦脢陆卤锚脢戮
脫脙 log = "x" 卤铆脢戮露脭潞谩脰谩碌脛卤盲脕驴陆酶脨脨log卤盲禄禄
qplot(gdpPercap, lifeExp, data=X, log = "x", color = year)


脪虏驴脡脪脭陆芦year卤盲鲁脡factor 麓脣脢卤禄谩脫脙脌毛脡垄碌脛脩脮脡芦卤锚脢戮
qplot(gdpPercap, lifeExp, data=X, log = "x", color = factor(year))


脢鹿脫脙 size = pop 脫脙卤锚脰戮碌脛麓贸脨隆脧脭脢戮赂脙卤盲脕驴碌脛麓贸脨隆
qplot(gdpPercap, lifeExp, data=X, log = "x", color = year, size = pop)


禄鹿驴脡脪脭脢鹿脫脙 shape = continent 脫脙虏禄脥卢碌脛卤锚脰戮脌麓脧脭脢戮赂脙卤盲脕驴
qplot(gdpPercap, lifeExp, data=X, log = "x", color = year, shape = continent)


脳卯潞贸 alpha=I(0.25) 脰赂露篓脥赂脙梅露脠 0脦陋脠芦脥赂脙梅 1脦陋虏禄脥赂脙梅
碌卤脢媒戮脻脰脴碌镁脩脧脰脴脢卤卤脠陆脧脫脨脫脙
qplot(gdpPercap, lifeExp, data=X, log = "x", alpha=I(0.25))


==========

3. geom

geom脢脟geometric object碌脛录貌鲁脝 脫脙脌麓脡煤鲁脡虏禄脥卢脰脰脌脿碌脛脥录

=====

3.1 smooth

脢脳脧脠脢脟smooth 脫脙脌麓脙猫脢枚脢媒戮脻碌脛脝陆禄卢脟梅脢脝
脳垄脪芒麓脣麓娄 c("point", "smooth") 卤铆脢戮脧脠禄颅point 脭脵禄颅smooth
qplot(gdpPercap, lifeExp, data=X, log = "x", alpha=I(0.5), geom=c("point", "smooth"))


脧脿路麓碌脛 c("smooth", "point") 戮脥脢脟脧脠禄颅smooth 脭脵禄颅point
qplot(gdpPercap, lifeExp, data=X, log = "x", alpha=I(0.5), geom=c("smooth", "point"))


鲁媒脕脣脛卢脠脧碌脛脝陆禄卢路陆路篓脰庐脥芒 禄鹿驴脡脪脭脳脭脨脨脰赂露篓 卤脠脠莽脧脽脨脭脛拢脨脥
qplot(gdpPercap, lifeExp, data=X, log = "x", alpha=I(0.5), geom=c("point", "smooth"), method=lm)


脕铆脥芒禄鹿驴脡脪脭脳脭脨脨脰赂露篓鹿芦脢陆 脌媒脠莽露脿脧卯脢陆禄脴鹿茅
qplot(gdpPercap, lifeExp, data=X, log = "x", alpha=I(0.5), geom=c("point", "smooth"), method=lm, formula = y ~ poly(x, 3))


=====

3.2 line潞脥path

line禄谩陆芦脢媒戮脻脩脴潞谩脰谩路陆脧貌掳麓脣鲁脨貌脕卢陆脫脝冒脌麓 脪禄掳茫脫脙脌麓卤铆脢戮脢卤录盲脨貌脕脨脢媒戮脻
qplot(pop, lifeExp, data=X, log = "x", alpha=I(0.5), color=year, geom="line")


path禄谩陆芦脭颅脢录脢媒戮脻脰脨脧脿脕脷碌脛脕陆赂枚碌茫脕卢陆脫脝冒脌麓 脪禄掳茫脫脙脌麓卤铆脢戮露镁脦卢脢媒戮脻脣忙脢卤录盲碌脛卤盲禄炉
qplot(gdpPercap, lifeExp, data=X, log = "x", alpha=I(0.5), color=year, geom=c("point", "path"))


=====

3.3 boxplot潞脥jitter

潞脥R base脰脨碌脛boxplot脪禄脩霉 潞谩脰谩碌脛脢媒戮脻脨猫脪陋脢脟factor
X$year.fac <- factor(X$year)
脳垄脪芒 color=I("red") 脰脨碌脛I()脢脟卤脴脨毛碌脛 路帽脭貌"red"禄谩卤禄碌卤脳枚脪禄赂枚脨脗碌脛factor
qplot(year.fac, lifeExp, data=X, color=I("red"), geom="boxplot")


jitter潞脥boxplot脌脿脣脝
qplot(year.fac, lifeExp, data=X, color=I("red"), geom="jitter")


=====

3.4 histogram潞脥density

脮芒脌茂脢鹿脫脙 fill=continent 陆芦脰卤路陆脥录掳麓虏禄脥卢碌脛continent路脰赂卯驴陋
qplot(lifeExp,data=X, geom="histogram", fill=continent)


density脫毛histogram脌脿脣脝
qplot(lifeExp,data=X, alpha=I(0.5), geom="density", color=continent)


==========

4. facets

脢鹿脫脙facets驴脡脪脭陆芦脪禄赂枚脥录赂霉戮脻脪禄赂枚禄貌脕陆赂枚卤盲脕驴碌脛脰碌路脰卤冒脧脭脢戮鲁枚脌麓 脫脨脌没脫脷赂眉脰卤鹿脹碌脴陆酶脨脨卤脠陆脧
~脳贸卤脽卤铆脢戮脙驴脪禄脨脨碌脛卤盲脕驴 脫脪卤脽卤铆脢戮脙驴脪禄脕脨碌脛卤盲脕驴
卤脠脠莽 continent~. 赂霉戮脻continent脰碌碌脛虏禄脥卢 陆芦density碌脛脥录脭脷脙驴脪禄脨脨脌茂脧脭脢戮鲁枚脌麓
qplot(lifeExp,data=X, geom="density", facets=continent~.)


脌脿脣脝碌脛 facets=year~continent 赂霉戮脻脙驴脪禄脨脨year潞脥脙驴脪禄脕脨continent脰碌碌脛虏禄脥卢 陆芦histogram碌脛脥录脧脭脢戮鲁枚脌麓
qplot(lifeExp,data=X, geom="histogram", facets=year~continent)








```r

library(gcookbook)
simpledat
```