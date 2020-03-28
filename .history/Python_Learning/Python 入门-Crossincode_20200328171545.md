# Python 入门

https://res.crossincode.com/wechat/python.html

## 【Python 第0课】Why Python？

> https://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5MDEyMDk4Mw==&appmsgid=10000003&itemidx=1&sign=7ba917f45dedbe2d35b78ec31440fb94

![img](http://mmbiz.qpic.cn/mmbiz/icic13vic5h8JHIPIKFibAQRpyhQdGa3RYrAsLMKuIp3fTUmzRCWhBvdhiayicNiabibNvQ0oOJESt1FDkG2wMvBiaemGWA/640?wx_fmt=png&tp=webp&wxfrom=5)

为什么用Python作为编程入门语言？


原因很简单。



嗯。。。原因就是，很**简单**。。。



每种语言都会有它的支持者和反对者。去Google一下“why python”（程序员准则：要Google不要百度。虽然我平时也都用百度来搜八卦新闻，但有关编程的东西真的搜出来结果差很多），你会得到很多结果，诸如应用范围广泛、开源、社区活跃、丰富的库、跨平台等等等等，也可能找到不少对它的批评，格式死板、效率低、国内用的人很少之类。不过这些优缺点的权衡都是程序员们的烦恼。作为一个想要学点编程入门的初学者来说，简单才是最重要的。当学C++的同学还在写链表，学Java的同学还在折腾运行环境的时候，学Python的你已经像上图一样飞上天了。



当然，除了简单，还有一个重要的原因：因为我现在每天都在写Python。虽然以后可能会讲些手机编程之类（如果真的有那么一天π_π），但目前这时候，各位也就看菜吃饭，有啥吃啥了。每天5分钟，先别计较太多。况且Python还是挺有利于形成良好编程思维的一门语言。



推荐两本我个人比较喜欢的Python入门书籍，一本是《**简明Python教程**》，在网上可以搜到它的在线中文版本。我自己最开始就是看着它学的，接下来也会大体参考里面的内容讲。另一本是《**Head First Python**》，Head First系列都是非常浅显易懂的入门类书籍，虽然我只瞄过几眼，但感觉还是不错的。





\# -------- 程序员的分割线 -------- #



Why这个公众账号？



事情的直接起因是Sunny同学昨天跟我说，她最近在学Python，如果碰到不懂的地方希望能问问我。我又联想到前阵子Jing同学说想学一门编程语言，于是就有了这么个号。（这中间还有个小插曲：我之前申请过两个公众号，结果再次申请的才被系统告知不能再申了，之前的号也不能改名字、不能删除。后来多亏Jing同学帮忙申请才得以把这个账号开起来。在此谢过！）



回想起来，我可能从很早的时候就有一种好为人师的心理。当别人听了半天课又琢磨了很久也没搞懂某个问题，被自己讲解了一番就恍然大悟的时候，总会有一种成就感。



其实就算没这个号，我现在也经常辅导某人学习编程，去年是Python，今年是C++。既然都是教，干脆开个号，给大家一起听听。如果这个号能满足我小小的成就感，又能帮到一点点想学编程的朋友，何乐而不为？只不过最近的确很忙，每天5分钟，先试试看吧。



我觉得，如果真能坚持说下去，又有人能坚持听下去（当然，有人听是前提），那至少听完的人可以对编程有个大概的了解，写点小程序自娱自乐不在话下。至多的话，那就不好说了，编个游戏、弄个网站、甚至以此为业，Impossible is Nothing。真能那样的话，我也算功德一件了。



如果你有任何疑问，没听懂的，觉得我讲得不好的，寂寞了想找人聊天的，都可以直接发消息。反正现在关注的人少，才两位数，收到必回。



好了，就这么多。不出意外的话，明天大家就能看到第一个Python程序了。还是那句话，希望我坚持下去的话，请推荐更多的人来关注，虽然只要还有一个人在听，我就尽力坚持，但更多的人听，我就更能坚持啦！

## 【Python 第1课】安装

> https://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5MDEyMDk4Mw==&appmsgid=10000006&itemidx=1&sign=871cc744bc9d9e660d63f76df4f7e43d

![img](http://mmbiz.qpic.cn/mmbiz/icic13vic5h8JHIPIKFibAQRpyhQdGa3RYrA17lYw1iaib7sH7fGhY1lGic11jLKlGl2icuT3ghjrV2ia8Ez7F2GepfP1IQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5)

在Windows系统上安装Python的方法还算简单，比平常装个软件稍稍麻烦一点。进入Python的官方下载页面**Python.org/download**，你会看到一堆下载链接。我们就选“**Python 2.7.13 Windows Installer**”（选最新的即可），如果是64位系统的同学选下面那个“Python 2.7.13 Windows X86-64 Installer”。如果你不是百分百确定自己是64位系统，请装非64位版本。想用最新 py3 版本也可以，请在公众号回复 **2v3**，查看一篇关于2和3之间的一些变化注意事项。



下载之后，就和装其他软件一样，双击，一路Next，想换安装路径的同学可以换个位置。但不管换不换，请把这个路径复制下来，比如我的是“C：\python27\”，后面要用到它。另外有个要注意的是，如果有“**add python.exe to path**”这个选项，请选中它，会让你省不少事。（不同版本这里有差异）

![img](https://mmbiz.qpic.cn/mmbiz_png/icic13vic5h8JGcuP959wQ278yf72yia6JU488FDHUS5iaGoEGWauY6yhPtzZicZpm33WbVoc0pGB8kzL137KjxOcneQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://mmbiz.qpic.cn/mmbiz_png/icic13vic5h8JGcuP959wQ278yf72yia6JU4U7pZ3ZmBgYzQ82KFpYZkzgSu8u4aZFAD0meuhh3uWQKYUHKIxXKicmg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



安装结束还没完，我们还差最后一步：设置**环境变量**。如果你上一步按照我说的，选上了“**add python.exe to path**”，则可略过此步骤。这是什么东西我暂时先不解释，大家照着做就好。右键单击**我的电脑**，依次点击"**属性**"->"**高级**"->"**环境变量**"，在“**系统变量**”表单中点击叫做**Path**的变量，然后编辑这个变量，把“**;C:\Python27\**”，也就是你刚才复制的安装路径，加到它的结尾。注意！要用英文分号和前面已有的内容隔开。然后点确定，点确定，再点确定。完成。

- 注意1：**win7系统**是右键单击“计算机”，点击“属性”->“高级系统设置”->“环境变量”
- 注意2：**win10系统**需要在Path里新建一条记录，把路径加进去，无需分号
- 注意3：环境变量里会有**用户变量**和**系统变量**两类，如果添加后无效，建议在两类的Path里都加上路径，或者尝试**重启**下系统
- 注意4：设置完要重新打开命令行

![img](https://mmbiz.qpic.cn/mmbiz_png/icic13vic5h8JGcuP959wQ278yf72yia6JU4sKnTl8kpm5XkWwqz9qHl8fUJFJXiakFiaibfS2qJCFQY2LibLrWPqXHs6g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



怎么知道你已经成功安装了Python呢？这时候你需要打开**命令行**，或者叫命令提示符、控制台。方法是：点击**开始菜单**->**程序**->**附件**->命令提示符；或者直接在桌面按快捷键“**Win+r**”，Win键就是Ctrl和Alt旁边那个有windows图标的键，输入**cmd**，回车。这时候你就看到可爱的黑底白字了。



在命令行里输入**python**，回车。如果看到诸如：

Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32

的提示文字，恭喜你！否则，请重新检查你哪里的打开方式不对，或者直接给我留言。

![img](https://mmbiz.qpic.cn/mmbiz_png/icic13vic5h8JGcuP959wQ278yf72yia6JU4OiaXvYiaJmQ22Y3ficEM5PXVcrtYCB6VwS1ibfBib5WSzUCj6g5znlJ5hlw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



接下来，你就可以输入那句程序员最爱的

**print("Hello World")**

向Python的世界里发出第一声啼哭。注意：一定要用英文引号！py3一定要加上括号()！



![img](https://mmbiz.qpic.cn/mmbiz_png/icic13vic5h8JGcuP959wQ278yf72yia6JU4P9aKjSZ2eniaibnhnoPAicc1sJiag7qIgyBjkzBBHL43lnRn4P3kAbpAicw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



嗯。。。如果这么几步你还是被绕晕了，没关系，我还留了一手：从公众号右边菜单里的“在线编程”或回复**code**，可进入我为你开发的一个在线写python的网页工具，练习一下python语言。不过在线工具毕竟功能有限，仅可作为体验，真正要学习还得在电脑上。



那Mac的同学怎么办？Mac上叫“终端”，英文版叫**Terminal**，可以在“应用程序”里找到，也可以直接在你的Mac上搜索“终端”或者“Terminal”找到。打开之后输入“python”，回车，就可以进入python了。



好了，今天就这么多，快去试试你的python，输出一行“Hello World”吧。完成的同学可以截个屏发给我。欢迎各种建议、讨论和闲聊，当然更欢迎你把这里分享给更多的朋友。



## 【Python 第2课】print

> https://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5MDEyMDk4Mw==&appmsgid=10000010&itemidx=1&sign=4c738a1328804a48250739974443de3b


![img](http://mmbiz.qpic.cn/mmbiz/icic13vic5h8JHIPIKFibAQRpyhQdGa3RYrA0EC8e9uyoyvIoot3R5adHosnjgl5pQicOnTjhejg7hOh7egk2Gk1E6Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5)

今天早上醒来，发现咱们的同学人数一夜之间多了50，后来又陆陆续续来了很多，于是我坚持下去的信心又增加了不少。在这里感谢连客官微的宣传，表示今晚将用加班写代码来表达谢意！



昨天大家是不是都在自己的电脑上搞定了python环境？或是试用过了在线环境？对了，这里补充两点：我今天发现昨天提供的compileonline.com网站有时候会很慢，甚至无法正常运行，于是我又找了一个：**pythonfiddle.com**，似乎要快一点，不过好像只能在电脑上的浏览器打开。另外就是，昨天忘了给Mac的同学们说一下怎么打开命令行。Mac上叫做“**终端**”或者“**Terminal**”，可以在“应用程序”里找到，也可以直接在“**spotlight**”里直接输入“**Terminal**”打开。打开后就可以通过“python”命令进入开发环境了。



今天新来的同学，可以回复“**python**”查看已有的课程目录，也可以直接发送“**0**”和“**1**”查看前两课的内容。



\#======== 进入今天的正题 ========#



今天要讲的东西，昨天课上大家已经见过，就是：**print**（注意：全是小写字母）。



print，中文意思是打印，在python里它不是往纸上打印，而是打印在命令行，或者叫终端、控制台里面。print是python里很基本很常见的一个操作，它的操作对象是一个字符串（什么是字符串，此处按住不表，且待日后慢慢道来）。基本格式是：

  **print 你要打印的东西**

或者

  **print(你要打印的东西)**

这里一定要英文字符的括号，所有程序中出现的符号都必须是英文字符，注意别被你的输入法坑了。



注意：如果你是python3及以后的版本，一定得用print()，不然会出错。



各位同学可以在自己的python环境中试着输出以下内容：



\>>> print "hello"

hello

\>>> print('world')

world

\>>> print 1

1

\>>> print(3.14)

3.14

\>>> print 3e30

3e+30

\>>> print 1 + 2 * 3

7

\>>> print(2 > 5)

False



python3记得在后面必须加上()



直接在print后面加一段文字来输出的话，需要给文字加上双引号或者单引号。大家发现，print除了打印文字之外，还能输出各种数字、运算结果、比较结果等。你们试着自己print一些别的东西，看看哪些能成功，哪些会失败，有兴趣的话再猜一猜失败的原因。



其实在python命令行下，print是可以省略的，默认就会输出每一次命令的结果。就像这样：



\>>> 'Your YiDa!'

'Your YiDa!'

\>>> 2+13+250

265

\>>> 5<50

True



今天内容就这么多。没听出个所以然？没关系，只要成功print出来结果就可以，我们以后还有很多时间来讨论其中的细节。



\#======== 课程预告 ========#



昨晚我想了下，如果只是单纯一个个语法、命令讲过去，实在太枯燥了。所以我决定设定一个短期目标，吊一下大家的胃口。



这个短期目标就是一个很简单很弱智的小游戏：



COM: Guess what I think?

5

COM: Your answer is too small.

12

COM: Your answer is too large.

9

COM: Your answer is too small.

10

COM: BINGO!!!



解释一下：首先电脑会在心中掐指一算，默念一个数字，然后叫你猜。你猜了个答案，电脑会厚道地告诉你大了还是小了，直到最终被你果断猜中。



这是我十几年前刚接触编程时候写的第一个程序，当时家里没有电脑，在纸上琢磨了很久之后，熬到第二个星期的电脑课才在学校的486上run起来。后来我还写过一个windows下的窗口版本。现在就让它也成为你们第一个完整的程序吧。照我们每天5分钟的进度，初步估计半个月后大约能完成了。

明天我打算再回到开发环境上，介绍一下编写python的开发工具。工欲善其事，必先利其器嘛。



## 【Python 第3课】IDE

![img](http://mmbiz.qpic.cn/mmbiz/icic13vic5h8JHZUcBAuzLUYMxKs4Qk0ibmDBst7m5warIe8CAheLcckskCshWhhFzhEBW6NbBictKgV4jv8b5fJaVQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5)

昨天的课发出去之后，有不少同学发来了反馈，有完成截屏的，也有遇到问题的。一些问题突然让我意识到，很多地方自己描述得不是很到位，会产生歧义，或者干脆就很难听懂。比如：



我自己不是Mac党，手边也没有Mac，所以不知道Mac上还有控制台（console）和终端（Terminal）之分。我想说的其实是终端。Mac的同学们可能要多自己摸索一下了。



另外我之前说了命令行下和在线编辑器两种输代码的方式，但其实这两种是不太一样的。（今天接下来会提到）我在文章里面的例子是在命令行里一行一行的输入得到的效果，有同学误以为全都是输入，贴到在线编辑器里，然后，就没有然后了。



因此在这里，我特别要申明一下：如果你发现照我说的去做，没有得到预期的结果，那多半是我没说清。千万不要觉得为什么编程这么难，搞了半天也不对。导致错误的原因，往往只是一点点小偏差，稍微改一下就好了。（顺便提一句，今天下午我工作的时候就因为一个单词拼错了，折腾了半天代码）



所以嘛，有问题不要一直自己闷着头纠结，多沟通一下就好了。人生中的事情，大抵如此，做人嘛，最重要的是要开心啦……咳咳。



另外，为了让大家更好地回顾讲过的内容，以及有问题时候方便讨论交流，我昨晚在百度贴吧上申请了一个版面--“Crossin的编程教室”吧，今天下午刚刚通过审核了。新建的吧好像不能模糊搜索，所以别漏打字了哦。点击本文最下方的“阅读原文”也可以直接进入这篇教程。



\#======== 进入今天的正题 ========#



什么是IDE？英文叫做Integrated Development Environment，中文就是集成开发环境。嗯，等于没说。



打个不恰当的比方，如果说写代码是制作一件工艺品，那IDE就是机床。再打个不恰当的比方，PS就是图片的IDE，Word就是doc文档的IDE，PowerPoint就是ppt文件的IDE。python也有自己的IDE，而且还有很多。



python自带了一款IDE，叫做IDLE。先说Windows，Windows上安装了之后，可以在“开始菜单”->“程序”->“Python 2.7”里找到它。打开后之后很像我们之前用过的命令行。没错，它就是的，在里面print一下试试。不知之前用命令行的同学有没有注意到，命令行输一行命令就会返回结果，而且之前print了那么多，关掉之后也不知道到哪里去了。所以它没法满足我们编写弱智小游戏的大计划。我们需要用新的方法！



**如何新建一个文件**



点击窗口上方菜单栏的“File”->“New Window”（有些版本是“New File”），会打一个长得很像的新窗口，但里面什么也没有。这是一个文本编辑器，在这里面就可以写我们的python程序了。继续print几行，这次可以多print一点：



print('Hello')

print('IDE')

print('Here I am.')



注意1：①用英文符号②py3要加上括号



现在是，见证奇迹的时刻！点击“Run”->“Run Module”，或者直接按快捷键F5。会提示你保存刚才文件，随便取个名字，比如“lesson3.py”。（.py是python代码文件的类型，虽然不指定.py也是可以的，但建议还按规范来）保存完毕后，之前那个控制台窗口里就会一次性输出你要的结果。



以后想再次编辑或运行刚才的代码，只要在IDLE里选择“File”->“Open...”，打开刚才保存的.py文件就可以了。



注意2：之后我们写多行代码时，一定要通过新建的代码文件，写好后保存运行。否则直接打开IDLE的环境是无法写多行代码的。



Mac上的IDLE是预装好了，在“终端”里输入“IDLE”就可以启动，使用方法同Windows。也可以在文件夹/usr/bin里可以找到IDLE。如果是重新下载安装了python，似乎是可以在“应用程序”里找到IDLE的，Mac的同学可以验证下。（有同学反馈说 Mac 上默认的 Python 里是不带 IDLE 的，需要自行下载安装 Python 后里面才有）



除了官配的 IDLE，还有一些很好用的第三方 IDE，把文件目录、文本编辑器、命令行都整合到了一起，还增加了很多辅助功能，配置好之后用起来应该比 IDLE 方便。这其中首推 PyCharm，它之前是收费软件，现在已经推出了免费版本，足够一般的学习和开发使用。有兴趣的同学也可以去找来试试看。



另外，Windows下还有一个第三方的免费IDE，叫PyScripter，地址：http://sourceforge.net/projects/pyscripter/。但 PyScripter 的编码设置有时会导致奇怪的问题，还有要注意它的安装位置和.py文件的保存位置都不能有中文，另外其官方的维护也不给力，所以现在不是十分推荐。



今天的内容有点长。配置开发环境这种事最麻烦了，大家耐心一点，毕竟一次投入，长期受益。以后我们的课程都会在IDE中进行，基本不再往命令行里直接敲代码了。



最后说下，有很多python程序员都不使用任何IDE。至于原因嘛，可能就像优秀的手工艺人是不会用机床来加工艺术品的吧。

## 【Python 第63课】python 2 到 3 的新手坑

> https://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5MDEyMDk4Mw==&appmsgid=10021103&itemidx=1&sign=398f5144682fb764b887679757a51245

![img](http://mmbiz.qpic.cn/mmbiz/icic13vic5h8JFsyh7TlAvKR09KqSoBjpDD53eqFSPIhmwrkZ0374IHOG5icyJosXzujEIGUcgfJ5GT1e3O5zqtNKw/640?tp=webp&wxfrom=5)

昨天挖了个坑，论坛上已经有不少解答了，还有c语言的版本。今天先不填坑，让题目再飞一会儿，没做的同学可以周末试着写写玩儿。



周三的时候去参加“编程一小时”活动，过程中发现，python版本2和版本3之间一些小改动把很多人都给坑了，花了大量的时间在这件事情上。所以今天来讲一下最大的两个坑：print 和 input。



**print**



我们在课程最开始的时候就讲过 print，在版本2的使用方法是：

print 'this is version 2'



也可以是

print('this is version 2')



但到了3，就只能加上括号，像一个函数一样来使用 print：



print('this is version 3')



假如你看了基于2的教程（比如我写的），然后又装了python 3，可能就会奇怪为什么完全照着写，结果却不一样。



另外2里不换行输出是加上逗号：



print '*',



到了3里就要改成：



print('*', end=' ')



**input**



而 input 就更绕一点。2里面有两个用来从命令行接受输入的函数：input 和 raw_input。



value = input()



input 接收的是一个值或变量，也就是说，你如果输 123，程序接收到的就是整数 123，你输 True，就是 bool 值 True。如果你输了 abc，程序会认为这是一个叫做 abc 的变量，而假如你没有定义过这个变量，就会报错。



所以，当你想用 input 得到一段文字的话，必须把文字写在引号 "" 或 '' 中。



text = raw_input()



raw_input 接收的则是你输入的字符串，而不管你输的是什么内容。如果你直接拿 raw_input 得到的“数字”去比较大小，则会得到奇怪的结果。



在版本3里，为了减少混乱，这两种输入方式被合并了。只是合并的方式又坑了新手：它保留了 input 这个名字和 raw_input 的效果。3里只有input函数，它接收你输入的字符串，不管你输的是什么。



text = input()



这种情况下，不管你是看着3的教材用2，还是看着2的教材用3，都会踩到这个坑。3里直接拿 input 得到的“数字”比较大小，会报错类型不同无法比较。



那么在3里，如何像2一样得到用户输入的一个值呢？方法是 eval()：



value = eval(input())



或者，如果你只是需要一个整数值，也可以：



value = int(input())





除了一开始越到的这两个坑外，还有其他一些可能遇到的变动，这里以3与2相比的差异来说：



- 打开文件不再支持 file 方法，只能用 open
- range不再返回列表，而是一个可迭代的range对象
- 除法 / 不再是整除，而是得到浮点数，整除需要用双斜杠 //
- urllib和urllib2合并成了urllib，常用的urllib2.urlopen()变成了urllib.request.urlopen()
- 字符串及编码相关有大变动，简单来说就是原来的str变成了新的bytes，原来的unicode变成了新的str。具体内容比较多，可以公众号回复 **编码**，有一篇专门讲3的字符编码问题



变动不止这些，这里仅列出初学者比较常见的几个。更多问题可以给我们留言，或者在 bbs.crossincode.com 上发帖提问，看到后会回复。