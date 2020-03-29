# Get Started with Python-Python入门

> [crossincode Python入门](https://res.crossincode.com/wechat/python.html), [Python 入门](https://python666.cn/cls/lesson/1/)

[TOC]

## 【Python 第0课】为什么选择 Python 入门？

> https://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5MDEyMDk4Mw==&appmsgid=10000003&itemidx=1&sign=7ba917f45dedbe2d35b78ec31440fb94
>
> [Python入门  第0课](https://python666.cn/cls/lesson/1/)



![img](https://cdn.py2china.cn/wechat/pystart/0-1.png)

### **Why Python？**

为什么用Python作为编程入门语言？

原因，很简单。

嗯。。。原因就是，很**简单**。。。

每种语言都会有它的支持者和反对者。去网上搜索一下“**python的好处**”，你会得到很多结果，诸如应用范围广泛、开源、社区活跃、丰富的库、跨平台等等等等，也可能找到不少对它的批评，格式死板、效率低、版本不兼容之类。不过这些优缺点的权衡都是程序员们的烦恼。作为一个想要学点编程入门的初学者来说，简单才是最重要的。如果对你来说不能上手，后面其他的是空谈。当学C++的同学还在写链表，学Java的同学还在折腾运行环境的时候，学Python的你已经像上图一样飞上天了。

当然，除了简单，我做Python教程还有一个重要的原因：我每天都在写Python代码。我可以更细致地为你讲解其中容易被忽略的细节。Python是很有利于形成良好编程思维的一门语言。每天5分钟，先动起手来再说。

推荐一本我比较喜欢的入门书籍《**父与子的编程之旅**》（又译作《**与孩子一起学编程**》） ，这本书特别适合完全没有接触过编程的人入门（唯一缺点是版本有一点老）。如果你曾接触过其他编程语言，可以考虑另外两本：《**简明Python教程**》和《**Head First Python**》。

###\#======== 课外的话 ========#

Why这个公众账号？

事情的直接起因是Sunny同学昨天跟我说，她最近在学Python，如果碰到不懂的地方希望能问问我。我又联想到前阵子Jing同学说想学一门编程语言，于是就有了这么个号。（这中间还有个小插曲：我之前申请过两个公众号，结果再次申请的才被系统告知不能再申了，之前的号也不能改名字、不能删除。后来多亏Jing同学帮忙申请才得以把这个账号开起来。在此谢过！）

回想起来，我可能从很早的时候就有一种好为人师的心理。当别人听了半天课又琢磨了很久也没搞懂某个问题，被自己讲解了一番就恍然大悟的时候，总会有一种成就感。

其实就算没这个号，我现在也经常辅导别人学习编程。既然都是教，干脆开个号，给大家一起听听。如果这个号能满足我小小的成就感，又能帮到一点点想学编程的朋友，何乐而不为？只不过最近的确很忙，每天5分钟，先试试看吧。

我觉得，如果真能坚持说下去，又有人能坚持听下去（当然，有人听是前提），那至少听完的人可以对编程有个大概的了解，写点小程序自娱自乐不在话下。至多的话，那就不好说了，编个游戏、弄个网站、甚至以此为业，Impossible is Nothing。真能那样的话，我也算功德一件了。

如果你有任何疑问，没听懂的，觉得我讲得不好的，寂寞了想找人聊天的，都可以来公众号 **Crossin的编程教室** 里直接发消息。反正现在关注的人少，才两位数，收到必回。（更新：现在六位数了）公众号二维码：

![二维码](https://python666.cn/static/minaclass/img/wxqr.jpg)

好了，就这么多。不出意外的话，明天大家就能看到第一个Python程序了。还是那句话，希望我坚持下去的话，请推荐更多的人来关注，虽然只要还有一个人在听，我就尽力坚持，但更多的人听，我就更能坚持啦！

 <div STYLE="page-break-after: always;"></div>

## 【Python 第1课】安装

> https://python666.cn/cls/lesson/2/
>
> https://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5MDEyMDk4Mw==&appmsgid=10000006&itemidx=1&sign=871cc744bc9d9e660d63f76df4f7e43d

### 0. Python 2

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

** print("Hello World") **

向Python的世界里发出第一声啼哭。注意：一定要用英文引号！py3一定要加上括号()！

![img](https://mmbiz.qpic.cn/mmbiz_png/icic13vic5h8JGcuP959wQ278yf72yia6JU4P9aKjSZ2eniaibnhnoPAicc1sJiag7qIgyBjkzBBHL43lnRn4P3kAbpAicw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

嗯。。。如果这么几步你还是被绕晕了，没关系，我还留了一手：从公众号右边菜单里的“在线编程”或回复**code**，可进入我为你开发的一个在线写python的网页工具，练习一下python语言。不过在线工具毕竟功能有限，仅可作为体验，真正要学习还得在电脑上。

那Mac的同学怎么办？Mac上叫“终端”，英文版叫**Terminal**，可以在“应用程序”里找到，也可以直接在你的Mac上搜索“终端”或者“Terminal”找到。打开之后输入“python”，回车，就可以进入python了。

好了，今天就这么多，快去试试你的python，输出一行“Hello World”吧。完成的同学可以截个屏发给我。欢迎各种建议、讨论和闲聊，当然更欢迎你把这里分享给更多的朋友。

在Windows系统上安装Python的方法还算简单，就比平常装个软件稍稍麻烦一点点。（Mac 也差不多）

 

### 1. Python 3 下载

进入Python的官方下载页面 https://www.python.org/downloads/，你会看到下载按钮和一堆下载链接。我们就直接选“**Download Python 3.7.3**”（选最新的即可），如果没有自动下载，64位系统的同学可以选下面那个“Windows x86-64 executable installer”。如果你不是百分百确定自己是64位系统，请装非64位版本“Windows x86 executable installer”。

由于Python 3是今后的主流，不建议安装Python 2。不过想用 py2 版本也可以，请在公众号回复关键字 **2v3**，查看一篇关于2和3之间的一些变化注意事项。

### 2. Python 3 安装

下载之后，就和装其他软件一样，双击，一路Next，想换安装路径的同学可以换个位置。但不管换不换**，请把这个路径复制下来**，比如我的是“**C:\python37\**”，后面要用到它。另外有个要注意的是，如果有“**add python.exe to path**”这个选项，请选中它，会让你省不少事。（不同版本这里略有差异）

![img](https://cdn.py2china.cn/wechat/pystart/1-0.png)

 

### 3. Python 3 运行

安装完之后，你应该可以在开始菜单的程序里找到 Python 的文件夹了。里面有一个叫做 **IDLE** 的程序，点击它，就进入了 Python 的开发工具。

![img](https://cdn.py2china.cn/wechat/pystart/1-4.png)

能打开 IDLE，看到里面输出的版本提示信息，就完成 Python 的安装了。

接下来，你就可以写下那句程序员最爱的

```python
print('Hello World')
```

向Python的世界里发出第一声啼哭。注意：单引号、双引号都可以，但引号和括号都一定要用英文的标点！

![img](https://cdn.py2china.cn/wechat/pystart/1-5.png)

 

特别说明：有时候，虽然 python 正常安装完毕，但是打开 IDLE 的时候会报错，或者无法正常使用。这时候，首先把报错信息在网上搜索一下，通常都会找到解决方案。如果不行，可以考虑换个早一点的python版本，比如 3.5、3.4 之类的重新安装下（不影响学习）。仍然不行的话，可以考虑再多安装一个 pycharm 软件来写代码（详细说明可在公众号回复关键字 **pycharm**）。你也可以去我们的[论坛](http://bbs.crossincode.com/)上寻求帮助。

### 4. Python 3 配置命令行（可选）

说明：完成前3步，你就已经可以开始写 Python 了，所以如果接下来的这一步让你感到头大，可以暂时忽略，基本不影响初期的学习。而且如果你上一步按照我说的，选上了“**add python.exe to path**”，此步骤就已自动完成。这一步的目的是设置**环境变量**，它的目的是让你能够在系统的命令行里运行 Python，具体是什么意思我暂时先不说得太复杂，大家照着做就好。

右键单击**我的电脑**，依次点击"**属性**"->"**高级**"->"**环境变量**"（或者直接通过开始菜单的搜索栏搜索“**环境变量**”进入），在“**系统变量**”表单中点击叫做 **Path** 的变量，然后编辑这个变量，把“**;C:\Python37\**”，也就是你刚才复制的安装路径，用**英文分号**和前面已有的内容隔开，加到它的结尾。然后点确定，点确定，再点确定。完成。

![img](https://cdn.py2china.cn/wechat/pystart/1-1.png)

 

怎么知道你已经配置成功安装了呢？这时候你需要打开**命令行**，或者叫命令提示符、控制台。方法是：点击**开始菜单**->**程序**->**附件**->**命令提示符**；或者直接在桌面按快捷键“**Win+r**”，Win键就是Ctrl和Alt旁边那个有windows图标的键，输入**cmd**，回车。这时候你就看到可爱的黑底白字了。

在命令行里输入**python**，回车。如果看到诸如：

Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32

的提示文字，恭喜你！

![img](https://cdn.py2china.cn/wechat/pystart/1-2.png)

否则，请重新检查你哪里的打开方式不对，或者直接给我留言。

**没出现上图效果请务必检查这几项注意：**

- 注意1：一定是要用**英文分号**和前面已有的内容隔开，记得关闭你的中文输入法
- 注意2：**win7系统**是右键单击“计算机”，点击“属性”->“高级系统设置”->“环境变量”
- 注意3：如果不存在Path记录，就创建一条新的
- 注意4：**win10系统**的Path不是用分号分隔，而是需要点击Path后再点击**新建**一条记录，把路径加进去，**无需分号**
- 注意5：环境变量里会有**用户变量**和**系统变量**两类，如果添加后无效，建议在两类的Path里都加上路径，并尝试**重启**下系统
- 注意6：设置完要**重新打开命令行**

命令行里的Python环境一样可以运行代码：

![img](https://cdn.py2china.cn/wechat/pystart/1-3.png)

 

嗯。。。如果这么几步你还是被绕晕了，没关系，我还留了一手：从公众号右边菜单里的“**在线编程**”或回复关键字**code**，可进入我为你开发的一个在线写python的网页工具，练习一下python语言。不过在线工具毕竟功能有限，仅可作为体验，真正要学习还得在电脑上。

那Mac的同学怎么办？Mac上叫“**终端**”，英文版叫**Terminal**，可以在“应用程序”里找到，也可以直接在你的Mac上搜索“终端”或者“Terminal”找到。打开之后输入 **idle** ，敲下回车，就可以进入开发工具；如果输入 **python** ，就可以打开如上的 python 命令行，你可以自己亲手试一试。

好了，今天就这么多，快去试试你的python，输出一行“Hello World”吧。完成的同学可以截个屏发给我。欢迎各种建议、讨论和闲聊，当然更欢迎你把这里分享给更多的朋友。

<div STYLE="page-break-after: always;"></div>

## 【Python 第2课】print

> https://python666.cn/cls/lesson/3/
>
> https://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5MDEyMDk4Mw==&appmsgid=10000010&itemidx=1&sign=4c738a1328804a48250739974443de3b

![img](http://mmbiz.qpic.cn/mmbiz/icic13vic5h8JHIPIKFibAQRpyhQdGa3RYrA0EC8e9uyoyvIoot3R5adHosnjgl5pQicOnTjhejg7hOh7egk2Gk1E6Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5)

昨天大家是不是都在自己的电脑上搞定了python环境？或是试用过了在线环境？

今天要讲的东西，昨天课上大家已经见过，就是：**print**（注意：全是小写字母）。

print，中文意思是打印，在 python 里它不是往纸上打印，而是打印在命令行，或者叫终端、控制台里面。print 是 python 里很基本很常见的一个操作，它的操作对象是一个字符串（什么是字符串，此处按住不表，且待日后慢慢道来）。基本格式是：

```python
print(你要打印的东西)
print('hello world')
```

这里一定要英文字符的括号，所有程序中出现的符号都必须是英文字符，注意别被你的输入法坑了。

各位同学可以在自己的python环境中试着输出以下内容：

```python
>>> print('world')
world
>>> print(1)
1
>>> print(3.14)
3.14
>>> print(3e30)
3e+30
>>> print(1 + 2 * 3)
7
>>> print(2 > 5)
False
```

直接在print后面加一段文字来输出的话，**需要给文字加上双引号或者单引号，除此之外的数字、计算式，还有我们以后会提到的变量，都不要加引号**。

大家发现，print除了打印文字之外，还能输出各种数字、运算结果、比较结果等。你们试着自己print一些别的东西，看看哪些能成功，哪些会失败，有兴趣的话再猜一猜失败的原因。

其实在python命令行下（每行前面有 **>>>** 的地方），print是可以省略的，默认就会输出每一次命令的结果。就像这样：

```python
>>> 'Your YiDa!'
'Your YiDa!'
>>> 2+13+250
265
>>> 5<50
True
```

今天内容就这么多。没听出个所以然？没关系，只要成功 print 出来结果就可以，我们以后还有很多时间来讨论其中的细节。

### \#======== 课程预告 ========#

昨晚我想了下，如果只是单纯一个个语法、命令讲过去，实在太枯燥了。所以我决定设定一个短期目标，吊一下大家的胃口。

这个短期目标就是一个很简单很弱智的小游戏：

```markup
COM: Guess what I think?
5
COM: Your answer is too small.
12
COM: Your answer is too large.
9
COM: Your answer is too small.
10
COM: BINGO!!!
```

解释一下：首先电脑会在心中掐指一算，默念一个数字，然后叫你猜。你猜了个答案，电脑会厚道地告诉你大了还是小了，直到最终被你果断猜中。

这是我十几年前刚接触编程时候写的第一个程序，当时家里没有电脑，在纸上琢磨了很久之后，熬到第二个星期的电脑课才在学校的486上运行起来。后来我还写过一个windows下的窗口程序版本。现在就让它也成为你们第一个完整的程序吧。照我们每天5分钟的进度，初步估计半个月后大约能完成了。

明天我打算再回到开发环境上，介绍一下编写python的开发工具。工欲善其事，必先利其器嘛。

### \#======== 课外的话 ========#

今天早上醒来，发现咱们的同学人数一夜之间多了50，后来又陆陆续续来了很多，于是我坚持下去的信心又增加了不少。在这里感谢连客官微的宣传，表示今晚将用加班写代码来表达谢意！

今天新来的同学，可以公众号内回复关键字 **python** 查看已有的课程目录，也可以直接发送数字 **0** 和 **1** 查看前两课的内容。

<div STYLE="page-break-after: always;"></div>

## 【Python 第3课】IDE

> https://python666.cn/cls/lesson/4/

![img](http://mmbiz.qpic.cn/mmbiz/icic13vic5h8JHZUcBAuzLUYMxKs4Qk0ibmDBst7m5warIe8CAheLcckskCshWhhFzhEBW6NbBictKgV4jv8b5fJaVQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5)

昨天的课发出去之后，有不少同学发来了反馈，有完成截屏的，也有遇到问题的。一些问题突然让我意识到，很多地方自己描述得不是很到位，会产生歧义，或者干脆就很难听懂。比如：

我自己不是Mac党，手边也没有Mac，所以不知道Mac上还有控制台（console）和终端（Terminal）之分。我想说的其实是终端。Mac的同学们可能要多自己摸索一下了。

另外我之前说了命令行下和在线编辑器两种输代码的方式，但其实这两种是不太一样的。（今天接下来会提到）我在文章里面的例子是在命令行里一行一行的输入得到的效果，有同学误以为全都是输入，贴到在线编辑器里，然后，就没有然后了。

因此在这里，我特别要申明一下：如果你发现照我说的去做，没有得到预期的结果，那多半是我没说清。千万不要觉得为什么编程这么难，搞了半天也不对。导致错误的原因，往往只是一点点小偏差，稍微改一下就好了。（顺便提一句，今天下午我工作的时候就因为一个单词拼错了，折腾了半天代码）

所以嘛，有问题不要一直自己闷着头纠结，多沟通一下就好了。人生中的事情，大抵如此，做人嘛，最重要的是要开心啦……咳咳。

另外，为了让大家更好地回顾讲过的内容，以及有问题时候方便讨论交流，我昨晚在百度贴吧上申请了一个版面--“Crossin的编程教室”吧，今天下午刚刚通过审核了。新建的吧好像不能模糊搜索，所以别漏打字了哦。点击本文最下方的“阅读原文”也可以直接进入这篇教程。

\#======== 进入今天的正题 ========#

什么是 **IDE**？英文叫做 **Integrated Development Environment**，中文就是**集成开发环境**。嗯，等于没说。

说人话：打个不恰当的比方，如果说写代码是制作一件工艺品，那IDE就是机床。再打个不恰当的比方，PS就是图片的IDE，Word就是doc文档的IDE，PowerPoint就是ppt文件的IDE。python也有自己的IDE，而且还有很多。

python自带了一款IDE，就是我们一开始介绍过的 **IDLE**。Windows上安装 python 了之后，可以在“开始菜单”->“程序”->“Python 3.7”里找到它（或者直接搜索 idle）。

不知道各位同学注意到没有，在这个默认的窗口里，三个箭头 >>> 后面写代码，输一行代码敲回车就会返回结果，没法换行；而且之前 print 了那么多，关掉之后也不知道到哪里去了，重新打开就都没有了。

所以它没法满足我们编写弱智小游戏的大计划。我们需要用新的方法！

### **如何新建一个文件**

点击窗口上方菜单栏的“**File**”->“**New File**”（有些版本是“New Window”），会打一个长得很像的新窗口，但里面什么也没有。这是一个文本编辑器，在这里面就可以写我们的python程序了。在里面写上几行 print 代码，这次可以多 print 一点：

```python
print('Hello')
print('IDE')
print('Here I am.')
```

**注意1：**①用英文符号②别忘了括号

现在是，见证奇迹的时刻！点击菜单栏de“**Run**”->“**Run Module**”，或者直接按快捷键F5。会提示你保存刚才文件，随便取个名字，比如“lesson3.py”。（.py是python代码文件的类型，虽然不指定.py也是可以的，但建议还按规范来）保存完毕后，之前那个控制台窗口里就会一次性输出你要的结果。

![img](https://cdn.py2china.cn/wechat/pystart/3-0.png)

以后想再次编辑或运行刚才的代码，只要在IDLE里选择“**File**”->“**Open...**”，打开刚才保存的.py文件就可以了。

**注意2**：之后我们写多行代码时，一定要通过新建的代码文件，写好后保存运行。否则直接打开IDLE的环境是无法写多行代码的。

**注意3**：一开始请不要在代码里写中文，可能会导致无法保存。如果一定要写的话，需要在文件一开始加上一行内容：

```python
# coding: gbk
```

Mac上的IDLE是预装好的，在“**终端**”里输入“**IDLE**”就可以启动，使用方法同Windows。也可以在文件夹 **/usr/bin** 里可以找到IDLE。如果是重新下载安装了python，有些版本是可以在“应用程序”里找到IDLE的（一个小火箭图标）。（有同学反馈说他用的 Mac 上默认的 Python 版本里是不带 IDLE 的，需要自行下载安装 Python 后里面才有，那请参考 [安装](https://python666.cn/cls/lesson/2/) 课程里的方法下载安装。）

除了官配的 IDLE，还有一些很好用的第三方 IDE，把文件管理、文本编辑器、命令行都整合到了一起，还增加了很多辅助功能比如代码提示、自动补全和跳转等，配置好之后用起来比 IDLE 更爽。这其中首推 **PyCharm**，它之前是收费软件，现在已经推出了免费版本，足够一般的学习和开发使用。有兴趣的同学也可以去找来试试看。在公众号里回复关键字 **pycharm**，可以看到之前写过的相关介绍文章。

今天的内容有点长。配置开发环境这种事最麻烦了，也是自学时候劝退率最高的环节，大家耐心一点，毕竟一次投入，长期受益。以后我们的课程都会在IDE中进行。

最后说下，有一些python程序员不使用任何IDE。至于原因嘛，可能就像优秀的手工艺人是不会用机床来加工艺术品的吧。

### \#======== 课外的话 ========#

昨天的课发出去之后，有不少同学发来了反馈，有完成截屏的，也有遇到问题的。一些问题突然让我意识到，很多地方自己描述得不是很到位，会产生歧义，或者干脆就很难听懂。比如：Mac上有控制台（console）和终端（Terminal）之分。我想说的其实是终端。Mac的同学们请注意。

另外，前面的课程我们是在Python命令行（有>>>的环境下）运行，我在文章里面的例子是在命令行里一行一行的输入得到的效果，有同学误以为全都是输入，一起贴到在线编辑器里，结果就报错得不到结果。

因此在这里，我特别要申明一下：如果你发现照我说的去做，没有得到预期的结果，那多半是我没说清。千万不要觉得为什么编程这么难，搞了半天也不对。导致错误的原因，往往只是一点点小偏差，稍微改一下就好了。（顺便提一句，今天下午我工作的时候就因为一个单词拼错了，折腾了半天代码）

所以嘛，有问题不要一直自己闷着头纠结，多沟通一下就好了。人生中的事情，大抵如此，做人嘛，最重要的是要开心啦……咳咳。

### 交流论坛

另外，为了让大家更好地回顾讲过的内容，以及有问题时候方便讨论交流，我建了一个论坛：[bbs.crossincode.com](https://python666.cn/cls/lesson/4/bbs.crossincode.com) ，你们可以在论坛相关的帖子下讨论课程内容，或者单独发帖提问。

<div STYLE="page-break-after: always;"></div>

## 【Python 第4课】输入

> https://python666.cn/cls/lesson/5/

Hi~我Crossin又来了。

可以用编程语言让计算机按你说的指令做事情之后，大家是不是有些跃跃欲试呢？别着急，先回顾一下我们之前几节课。我们到现在一共提到了三种可以运行print的方式：

1. 打开 IDLE，直接在 >>> 后面输入 print 语句并回车执行。但是这种方法很难帮我们实现写一个完整小程序的目标。

2. 在 IDLE 里新建一个代码文件，写好 print 语句后，保存并运行。以后我们课程里的内容，你都可以用此方法进行。不知道大家是不是都顺利搞定，并且能顺利保存并打开py文件了呢？

3. 也可以直接在命令行里运行 python 命令，进入 python 命令行的交互环境。命令行，包括Win下的控制台（CMD）和Mac下的终端（Terminal）。

大家是不是都准备好自己的武器了呢？那我们接下来就要正式开战啦！

\#======== 进入今天的正题 ========#

之前print了那么多，都是程序在向屏幕“输出”。那有来得有往，有借得有还，有吃。。。咳咳！那啥，我们得有向程序“输入”信息的办法，才能和程序对话，进行所谓的“人机交互”。

python有一个接收命令行下输入的方法：

```python
input()
```

注意，和 print 一样，我们必须得加上()，而且得是英文字符的括号。

好了，终于可以搬出那个弱智小游戏了，耶！

游戏里我们需要跟程序一问一答，所以我们先把话给说上。

打开我们的python编辑器，不管是IDLE，还是其他的IDE。新建一个代码文件，在其中输入下面几句代码：

```python
print("Who do you think I am?")
input()
print("Oh, yes!")
```

然后，点击 Run -> Run module。你会在命令行中看到，程序输出了第一句之后就停住了，这是 input 在等待你的输入。

**注意1**：这里的代码请新建一个代码文件后，在其中编写并运行，否则无法换行并获取输入（参见之前 [IDE](https://python666.cn/cls/lesson/4/) 那课中的说明）

**注意2**：这里是在控制台里输入内容后回车，而不是把你要输的东西提前写在括号里！切记！括号里可以加文字，但那只是用来作为输入的提示语。input 不是提前代码里写死输入内容，而是在程序运行时动态获取用户的输入。

输入你的回答，敲回车。你会看到程序的回答。

![img](https://cdn.py2china.cn/wechat/pystart/4-0.png)

图中的代码额外有增加了一问一答，蓝色字是程序输出，黑色字是我们运行时的输入。

**注意3：py3里的input()得到的都是字符串**。如果输入了数字，得到的也是含有这个数字的字符串，而非数值。

看上去不错哦，似乎就这么对上话了。是不是觉得离小游戏的完成迈进了一大步？可是大家发现没有，即使你说"Idiot！"，程序仍然会淡定地回答"Oh, yes!"因为它左耳进右耳出，根本就没听进去我们到底说了啥。那怎么才能让它认真听话呢？

啪！且听下回分解。

### \#======== 课外的话 ========#

PS：今天心情不错，给大家讲个很冷的程序员笑话。

> *一位程序员对书法十分感兴趣，退休后决定在这方面有所建树。于是花重金购买了上等的文房四宝。一日，饭后突生雅兴，一番磨墨拟纸，并点上了上好的檀香，颇有王羲之风范，又具颜真卿气势，定神片刻，泼墨挥毫郑重地写下一行字：*
>
> hello world

<div STYLE="page-break-after: always;"></div>

## 【Python 第5课】变量

> https://python666.cn/cls/lesson/6/

昨天说到，需要让程序理解我们输入的东西。那首先，就需要有东西把我们输入的内容记录下来，好为接下来的操作做准备。

> Python之神说，要有变量！于是就有了变量。

**变量**，望文生义，**就是可变化的量**。python里创建一个变量的方法很简单，给它起个名字，然后给它一个值。举起几个栗子:

```python
name = 'Crossin'
myVar = 123
price = 5.99
visible = True
```

“**=**”的作用是把右边的值赋予给左边的变量。

这里说一下另外一个概念，叫做“数据类型”，上面4颗栗子分别代表了python中较常见的四种基本类型：

- 字符串 ： 表示一串字符，需要用''单引号或""双引号包围起来
- 整数
- 浮点数 ： 就是小数
- bool（布尔）： 这个比较特殊，是用来表示逻辑上的“真”和“假”（或者说“**是**”和“**非**”）的一种类型，它只有两个值，**True** 和 **False**。（注意：这里没有引号，有了引号就变成字符串了）

再次用到我们熟悉的 print。这次，我们升级了，要用print输出一个“变量”：

```python
name = 'Crossin'
print(name)
```

看到结果了吗？没有输出“**name**”，也没有报错，而是输出了“**Crossin**”。

**注意：**name不需要加引号，不然它也就成了一个字符串，而不是变量

现在想一想：为什么之前 print 一段文字，如果没加引号就会报错，而 print 一个数字就没有问题呢？

它叫变量，那就是能变的。所以在一次“赋值”操作之后，还可以继续给它赋予新的值，而且可以是不同类型的值。

```python
a = 123
print(a)
a = 'hi'
print(a)
```

“=”的右边还可以更复杂一点，比如是一个计算出的值:

```python
value = 3 * 4
print(value)
value = 2 < 5
print(value)
```

甚至，也可以是input():

```python
name = input()
print(name)
```

于是，我们又可以进化一下我们的小游戏了。把上次写的内容稍微改一下，加上变量：

```python
print("Who do you think I am?")
you = input()
print("Oh, yes! I am a")
print(you)
```

![img](https://cdn.py2china.cn/wechat/pystart/5-0.png)

看来程序已经知道我们的输入了。接下来，就要让它学会对不同的答案做出判断。这个我们留到下次再说。

### \#======== 课外的话 ========#

有些同学在用我们的**在线编辑器**或者其他类似的网页工具在写代码。但有个不幸的消息是：绝大多数在线编辑器没办法完全模拟控制台下输入输出的操作（不支持 input）。所以，你可以通过它来简单的体验和学习，但是想跟着我一起完成那个弱智小游戏，还是必须给你的电脑装上python。

今天是周五。我觉得吧，到周末了，大家应该远离一下电脑，多陪陪家人朋友，吃吃饭，出去走走。祝大家周末愉快！

### 两数相加

```python
# 依次输入两个值，输出这两个值的和
# 例：
# 输入
# 3
# 4
# 输出
# 7

a = int(input())
b = int(input())
print(a + b)
```

<div STYLE="page-break-after: always;"></div>

## 【Python 第6课】bool

> https://python666.cn/cls/lesson/7/

昨天说到了python中的几个基本类型，字符串、整数、浮点数都还算好理解，关于剩下的那个 **bool（布尔值）**我要稍微多说几句。

**逻辑判断**在编程中是非常重要的。大量的复杂程序在根本上都是建立在“**真**”与“**假**”的基本逻辑之上。而 bool 所表示的就是这种最单纯最本质的 **True/False**，真与假，是与非。

来看下面的例子：

```python
a = 1 < 3
print(a)
b = 1
c = 3
print(b > c)
```

通过用“**>**”“**<**”来比较两个数值，我们就得到了一个bool值。这个bool值的真假取决于比较的结果。

“>”“<”在编程语言中被称为**比较运算符**（或叫 关系运算符），常用的比较运算符包括：

| >    | 大于                                                         |
| ---- | ------------------------------------------------------------ |
| <    | 小于                                                         |
| >=   | 大于等于                                                     |
| <=   | 小于等于                                                     |
| ==   | 等于（比较两个值是否相等。之所以用两个等号，是为了和变量赋值区分开来） |
| !=   | 不等于                                                       |

还有一种**逻辑运算符**：

| not  | 逻辑“**非**” | 如果 x 为 True，则 not x 为 False                |
| ---- | ------------ | ------------------------------------------------ |
| and  | 逻辑“**与**” | 如果 x 为 True，且 y 为 True，则 x and y 为 True |
| or   | 逻辑“**或**” | 如果 x、y 中至少有一个为 True，则 x or y 为 True |

比较运算符和逻辑运算符的结果都是 bool 类型的值。

关于bool值和逻辑运算其实远不止这些，但现在我们暂时不去考虑那么多，以免被绕得找不到北。最基本的**大于、小于、等于**已经够我们先用一用的了。

试试把bool加到我们的小游戏里：

```python
num = 10
print('Guess what I think?')
answer = int(input())

result = answer<num
print('too small?')
print(result)

result = answer>num
print('too big?')
print(result)

result = answer==num
print('equal?')
print(result)
```

代码比之前稍微多了一点，解释一下。

第一段代码：先创建一个值为10的变量 num，输出一句提示，然后再输入一个值给变量 answer。（因为input拿到的值是字符串而不是数字，这里我们需要将input的结果强行转成整数类型int）

第二段代码：计算 answer<num 的结果，记录在 result 里，输出提示，再输出结果。

第三段、第四段都与第二段类似，只是比较的内容不一样。

注意：当你自己写这段代码的时候，要确保不要有笔误，比如拼错单词，漏掉等号、引号、括号……。（这种情况在新手身上屡有发生）

![img](https://cdn.py2china.cn/wechat/pystart/6-0.png)

看看结果是不是跟你预期的一致？虽然看上去还是有点傻，但是离目标又进了一步。（这里不管正确与否，三个答案都会被输出。如果你只要它输出正确的那一个结果，学到后面课程就知道了）

现在数数你手上的工具：**输入**、**输出**，用来记录数值的**变量**，还有可以比较数值大小的**逻辑运算**。用它们在你的python里折腾一番吧。

### \#======== 课外的话 ========#

闲扯还是要的。有同学问，为什么这个语言要叫python。这个嘛，它肯定不是我起的。python，读作“派森”（差不多啦），中文意思“巨蟒”。其实是一个喜剧团体用了“Monty Python”这个名字，而python的创造者（Guido van Rossum 老爷子）又是他们的电视节目《Monty Python and the Flying Circus》（巨蟒飞行马戏团）的粉丝。当他还在自娱自乐地折腾python的雏形时，就拿来命了名。所以，你要是发明了一种语言，也可以命名个 GoT、TBBT、zhenhuan 之类的。

<div STYLE="page-break-after: always;"></div>

## 【Python 第7课】if

> https://python666.cn/cls/lesson/8/

继续上次的程序。我们已经能让程序程序判断我们输入的值了，但这程序还是有点呆，不管怎样都要把话说三遍。因为到目前为止，我们的程序都是按照顺序从上到下一行接一行地执行。

有同学发来问题了：怎么能让它根据我们输入的结果来选择执行呢？ 答案就是： **if**

if，英文翻译过来就是 **如果**。 来看一张图（纯手绘，渣画质）

![img](https://cdn.py2china.cn/wechat/pystart/7-0.png)

解释一下：程序顺序往下执行遇到 **if 语句**的时候，会去判断它所带**条件的真假**。

“如果”条件为True，就会去执行接下来的内容。“如果”条件为False，就跳过。

语法为：

```python
if 条件:
    选择执行的语句
```

特别说明：条件后面的**冒号不能少**，同样必须是**英文标点**。

特别特别说明：if 内部的语句需要有一个统一的**缩进**（就是指每一行开头的空格），一般用4个空格。缩进表示这些代码属于这个 if 条件内部，是一个“代码块”。python用这种方法替代了其他很多编程语言中的大括号{}。

你也可以选择1/2/3...个空格或者按一下tab键，但必须整个文件中都统一起来。**千万不可以tab和空格混用**，不然就会出现各种莫名其妙的错误。所以建议都直接用4个空格。

如果 if 中的代码块又再包含一个 if，那就需要再进一步缩进一次。一个代码中的缩进需要统一，比如每次都是增加4个空格。上栗子：

```python
# coding: gbk
age = int(input())
if age >= 18:
    print("你是个成年人了！")
```

**注意1**：这里的代码请新建一个代码文件后，在其中编写并运行，否则无法换行及缩进（参见之前 [IDE](https://python666.cn/cls/lesson/4/) 课中的说明）

**注意2**：由于代码中有中文，所以我们在开头加上了一行编码申明（同样参见之前 [IDE](https://python666.cn/cls/lesson/4/) 课中的说明）

试试看：当你输入一个大于等于18的数字时就会有输出，否则什么也没有。想想是为什么？

所以现在，我们的游戏可以这样改写：

```python
num = 10
print ('Guess what I think?')
answer = int(input())
if answer<num:
    print ('too small!')
if answer>num:
    print ('too big!')
if answer==num:
    print ('BINGO!')
```

![img](https://cdn.py2china.cn/wechat/pystart/7-1.png)

if 在编程语言中被称为“**控制流语句**”，用来控制程序的执行顺序。还有其他的控制流语句，后面的课程中我们会陆续介绍。

### \#======== 课后作业 ========#

有不少同学强烈要求布置作业。好吧，满足你们。还记得之前那个“*你觉得我是什么人？(Who do you think I am)*”的程序吧？（不记得的请戳 [4. 输入](https://python666.cn/cls/lesson/5/)）

改写一下，只有你回答某些好话的时候，程序才会回复 “**Oh yes”**，其他都不理你。甚至说某些词的时候，它还要反驳你。至于用哪些词哪些条件，你们自己设定吧。

### \#======== 课外的话 ========#

学会了if，有一个好处，就是你能听懂下面这个笑话了：

*老婆给当程序员的老公打电话：“下班顺路买一斤包子带回来，如果看到卖西瓜的，就买一个。”*

*当晚，程序员老公手捧一个包子进了家门……*

*老婆怒道：“你怎么就买了一个包子？！”*

*老公答曰：“因为看到了卖西瓜的。”*

<div STYLE="page-break-after: always;"></div>

## 【Python 第8课】while

> https://python666.cn/cls/lesson/9/

先介绍一个新东西：**注释**

python里，以“#”开头的文字会被忽略，不会被认为是可执行的代码。

```python
print ("hello world")
```

和

```python
print ("hello world")    #输出一行字
```

是同样的效果。但后者可以帮助开发者更好地理解代码。

在接下来的课程中，我会经常用注释来解释代码。

\#======== 进入今天的正题 ========#

用if改进完我们的小游戏后，功能已经基本实现了。很多同学做完后纷纷表示，每次只能猜一次，完了之后又得重新run，感觉好麻烦。能不能有办法让玩家一直猜，直到猜中为止？答案很显然：如果这种小问题都解决不了，那 python 可就弱爆了。

最简单的解决方法就是：**while**

同 if 一样，while 也是一种控制流语句，另外它也被称作循环语句。继续来看渣画质手绘流程图：

![img](https://cdn.py2china.cn/wechat/pystart/8-0.png)

while，英文翻译过来就是“当...的时候”。

程序执行到 **while** 处，“当”条件为 True 时，就去执行 while 内部的代码；“当”条件为 False 时，就跳过。

语法为：

```python
while 条件:
    循环执行的语句
```

同 if 一样，注意冒号，注意缩进。

今天的栗子：

```python
# coding: gbk
a = 1             # 为了后面的条件能满足，先把a设为1
while a != 0:     # 如果a不等于0就循环（1不等于0）
    print("please input")
    a = int(input())     # 在循环内部获取输入，改变a的值（想想看不改会怎样？）
print("over")
```

程序执行后，会不断向你询问输入，直到你输入0，条件 **a!=0** 不满足，循环结束。

现在，想想怎么用while改进小游戏？有多种写法，大家自己思考下，我不多做说明了。

下图给出一种方法。

![img](https://cdn.py2china.cn/wechat/pystart/8-1.png)

解释下：

1. 代码中，我们用了一个叫做 bingo 的变量，来记录是否猜中了结果，猜中了就是 True，没猜中就是 False（bingo本身就是有“赢了”的意思，你也可以命名为 caizhong，这个随意）。
2. 一开始，我们给 bingo 赋值为 False，使程序可以进入循环。
3. 每次循环中，我们都会输入一遍 answer，然后判断是大是小还是相等。如果相等了，再此条件的代码块里面增加一句 bingo = True，修改 bingo 的值，使得程序在下一次循环判断的时候，发现 bingo == False 这个循环条件不再满足，于是程序结束。

注意：这里出现了两层缩进，要保持每层缩进的空格数相同。

到此为止，小游戏已经基本成型了。不过好像还差一点：每次自己都知道答案，这玩起来有神马意思。

明天来讲，怎么让你不知道电脑的答案。

PS：如果你对本课中的 bingo = False、bingo == False 和 bingo = True 感到困惑，先别着急挠头，我们会在后面 [11.逻辑判断](https://python666.cn/cls/lesson/12/) 课程中进一步详细解释。

### \#======== 作业练习 ========#

你可以在公众号**Crossin的编程教室**中的**课外辅导**栏目里找到一些 [练习题](http://mp.weixin.qq.com/mp/homepage?__biz=MjM5MDEyMDk4Mw==&hid=3&sn=08af41239ec5d518ac25edb0f9167cc0&scene=18#wechat_redirect)，学了 while 之后，你可以试一试完成 3~6 题。

```python
# 输出1到100

# 例：
# 1
# 2
# 3
# ...
# 100

start_num = 1
end_num = 100

while start_num <= end_num:
    print(start_num)
    start_num = start_num + 1
```

#### 输出累计求和

于是，利用变量、循环、累加，可以写一个程序，来完成传说中高斯大牛在小时候做过的题：

1+2+3+...+100=?

从1加到100等于多少？

```python
# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Test_Sum100.py
@Time    :   2020/03/28 23:56:07
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# 输出1+2+3+...+100的和
# 例：
# 5050

x = 1
sum = 0

while x <= 100:
    sum += x
    x += 1
    print("1 to ", x ", the sum is: ", sum)

print("Final Sum of 1 to 100 is: ", sum)

```

提示：你可以用一个变量a记录现在加到几了，再用一个变量b记录加出来的结果，通过while来判断是不是加到100了。

####  输出等比数列前10项

```python
# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Test_Output_Proportional_Sequence.py
@Time    :   2020/03/29 09:05:39
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# Proportional sequence output
# 输入一个值，输出以这个值为公比，1为首项的等比数列前10项
# 例：
# 输入
# 2
# 输出
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# 256
# 512

print("Pls input Proportional number")

q = int(input())
n = 1
an = 1

while n <= 10:
    print(an)
    an *= q
    n += 1

```

> **有时治愈，常常帮助，总是安慰**。--特鲁多

#### 输出斐波纳契数列的前n项

```python
# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Test_Output_Fibonacci_Series.py
@Time    :   2020/03/29 09:26:04
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib


# Test_Output_Fibonacci_Series
# 输入一个大于等于3的值n，输出斐波纳契数列的前n项。
# 注：斐波纳契数列：1,1,2,3,5,8,13,21...前两项为1，从第3项起，每一项是前两项的和

# 例：
# 输入
# 7
# 输出
# 1
# 1
# 2
# 3
# 5
# 8
# 13

print("Pls input Fibonacci Series number")

n = int(input())
x = 3
a1 = 1
a2 = 1
print(a1)
print(a2)

while x <= n:
    a3 = a1 + a2
    print(a3)
    a1 = a2
    a2 = a3
    x += 1

```



<div STYLE="page-break-after: always;"></div>

## 【Python 第9课】random

> https://python666.cn/cls/lesson/10/

之前我们用了很多次的 print 和 input 方法，它们的作用是实现控制台的**输入**和**输出**。除此之外，python还提供了很多**模块**，用来实现各种常见的功能，比如时间处理、科学计算、网络请求、随机数等等等等。

今天我就来说说，如何用python自带的**随机数模块**，给我们的小游戏增加不确定性。

引入模块的方法：

```python
from 模块名 import 方法名
```

看不懂没关系，这东西以后我们会反复用到。今天你只要记住，你想要产生一个随机的整数，就在程序的最开头写上：

```python
from random import randint
```

之后你就可以用 **randint** 来产生随机数了。

还记得input后面的()吗，我们使用randint的时候后面也要有()。而且，还要在括号中提供两个数字，先后分别是产生**随机整数范围的下限和上限**。例如：

```python
randint(5, 10)
```

这样将会产生一个5到10之间（包括5和10）的随机整数。

放到我们的小游戏里，用

```python
num = randint(1, 100)
```

替代

```python
num = 10
```

程序在运行时候，会产生一个1到100的随机整数，存在num里，每次运行都不一样，我们也不知道是多少，真的全靠猜了。

![img](https://cdn.py2china.cn/wechat/pystart/9-0.png)

好了，觉得还有点意思么？

我们终于一步步把这个弱智小游戏给做出来了，有没有一丁点的成就感呢？

如果你对其中的某些细节还不是很理解，恭喜你，你已经开始入门了。相信你会带着一颗追求真相的心，在编程这条路上不断走下去。

我们的课程，也才刚刚开始。

### \#======== 作业练习 ========#

今天来挖第一坑。题目很简单： 

从1~n中，随机取m个数。1<=m<=n 

```python
# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson9.py
@Time    :   2020/03/28 20:50:56
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

import random
total_count = 100
sample_count = 10
i = 1

while i <= 10:
    rs1 = random.sample(range(1, total_count), sample_count)
    print("Loop count: ", i,  ". Ramdom Sample: ", rs1)
    i = i  + 1

# python——random.sample()的用法
# 写脚本过程中用到了需要随机一段字符串的操作，查了一下资料，
# 对于random.sample的用法，多用于截取列表的指定长度的随机数，但是不会改变列表本身的排序
list = [0,1,2,3,4]
rs = random.sample(list, 2)

print(rs)
# [2, 4]    #此数组随着不同的执行，里面的元素随机，但都是两个
print(list)
# [0, 1, 2, 3, 4]

# 上面这种方法要求知道已知的数列，但是不能满足我在一定范围内，随机出一定长度数据的要求。
# 下面这种方法，跟range相结合，在指定范围内获取一定长度的数据，这个用起来就比较灵活，代码如下：
rs = random.sample(range(0, 9), 4)
print(rs)
```

### [Python random模块sample、randint、shuffle、choice随机函数概念和应用](https://www.cnblogs.com/dylancao/p/8202888.html)

Python标准库中的random函数，可以生成随机浮点数、整数、字符串，甚至帮助你随机选择列表序列中的一个元素，打乱一组数据等。

random中的一些重要函数的用法：

1 )、random() 返回0<=n<1之间的随机实数n；
2 )、choice(seq) 从序列seq中返回随机的元素；
3 )、getrandbits(n) 以长整型形式返回n个随机位；
4 )、shuffle(seq[, random]) 原地指定seq序列；
5 )、sample(seq, n) 从序列seq中选择n个随机且独立的元素；

#### 详细介绍：

random.random() 函数是这个模块中最常用的方法了，它会生成一个随机的浮点数，范围是在0.0~1.0之间。

random.uniform() 正好弥补了上面函数的不足，它可以设定浮点数的范围，一个是上限，一个是下限。

random.randint() 随机生一个整数int类型，可以指定这个整数的范围，同样有上限和下限值，python random.randint。

random.choice() 可以从任何序列，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等。

random.shuffle() 如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法。

random.sample() 可以从指定的序列中，随机的截取指定长度的片断，不作原地修改。

#### 使用例子：

```python
# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   random.py
@Time    :   2020/03/28 20:50:56
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

import random

print("\n\t")
print("start test choice:")
foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))

print("\n\t")
print("start test slice:")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回  
print(slice) 
print(list) #原有序列并没有改变
             
print("\n\t")
print("start test uniform:")
print(random.uniform(10, 20))  
print(random.uniform(20, 10)) 
    
print("\n\t")
print("start test randint:")
print(random.randint(10, 20))  
print(random.randint(0, 1))

print("\n\t")
print("start test random:")
print(random.random()*1000)
print(random.random())

print("\n\t")
print("start test shuffle:")
li = range(20)
print(li)
print(random.shuffle(li))
print(li)

# Traceback (most recent call last):
#  File "F:/Github/xiangxing98.github.io/Python_Learning/random_test.py", line 45, in #<module>
#    print(random.shuffle(li))
#  File "C:\Program Files\Python37\lib\random.py", line 278, in shuffle
#    x[i], x[j] = x[j], x[i]
#TypeError: 'range' object does not support item assignment
```

<div STYLE="page-break-after: always;"></div>

## 【Python 第10课】变量2

> https://python666.cn/cls/lesson/11/

变量这东西，我们已经用过。有了变量，就可以存储和计算数据。今天来讲点变量的细节。

### \#==== 变量命名规则 ====#

变量名不是你想起就能起的：

1. 第一个字符必须是字母或者下划线_
2. 剩下的部分可以是字母、下划线_或数字0~9
3. 变量名称是对大小写敏感的，myname 和 myName 不是同一个变量。

几个有效的栗子：

```python
i
__my_name
name_23
a1b2_c3
```

几个坏掉的栗子（想一下为什么不对）：

```python
2things
this is spaced out
my-name
```

### \#==== 变量的运算 ====#

我们前面有用到变量来存储数据：

```python
num = 10
answer = input()
```

也有用到变量来比较大小：

```python
answer < num
```

除此之外，变量还可以进行数学运算：

```python
a = 5
b = a + 3
c = a + b
```

python中运算的顺序是，先把“=”右边的结果算出了，再赋值给左边的变量，相当于是两个步骤。

计算规则本身的顺序和数学中一样，先乘除后加减，有括号先算括号里。（对于拿不准顺序的计算，尽量加上括号）

下面这个例子：

```python
a = 5
a = a + 3
print(a)
```

你会看到，输出了8，因为先计算出了右边的值为8，再把8赋给左边的a。通过这种方法，可以实现**累加求和**的效果。

它还有个简化的写法：

```python
a += 3
```

这个和

```python
a = a + 3
```

是一样的。

我们之前的猜数字游戏，就可以用此方法加上一个记录猜了多少次的功能：

```python
from random import randint
num = randint(1, 100)

print('Guess what I think?')
bingo = False
count = 0

while bingo == False:
    count += 1
    answer = int(input())
    if answer<num:
        print('too small! Guess Again.')
    if answer>num:
        print('too big! Guess Again.')
    if answer==num:
        print('BINGO!Stop')
        bingo = True

print(count)
```

### \#======== 作业练习 ========#



<div STYLE="page-break-after: always;"></div>

## 【Python 第11课】逻辑判断

> https://python666.cn/cls/lesson/12/

之前粗略地提到 **bool 类型**的变量，又说到 if 和 while 的判断条件。有些同学反馈说没怎么理解，为什么一会儿是 bingo=False，一会又是 bingo==False，一会儿是 while 在条件为 True 的时候执行，一会儿又是 while 在 bingo==False 的时候执行。别急，你听我说。

首先，要理解，一个逻辑表达式，其实最终是代表了一个bool类型的结果，比如：

```python
1 < 3
# 这个就像当于是一个True的值

2 == 3
# 这个就是False
```

把它们作为判断条件放到 if 或者 while 的后面，就是根据他们的值来决定要不要执行。

同样的栗再来几颗：

```python
a = 1
print(a > 3)  # False
print(a == 2-1)  # True

b = 3
print(a+b == 2+2)  # True
```

比较容易搞混的，是bool变量的值和一个逻辑表达式的值，比如：

```python
a = False
print(a)  #False
print(a == False)  #True
```

虽然 a 本身的值是 False，但是 a==False 这个表达式的值是True。（说人话！）“a”是错的，但“a是错的”这句话是对的。

回到上面那几个概念：

```python
bingo = False
```

把bingo设为一个值为False的变量

```python
bingo == False
```

判断bingo的值是不是False，如果是，那么这句话就是True

while 在判断条件条件为 True 时执行循环，所以当 bingo==False 时，条件为 True，循环是要执行的。

晕了没？谁刚学谁都晕。不晕的属于骨骼惊奇百年一遇的编程奇才，还不赶紧转行做程序员！

逻辑这东西是初学编程的一大坑，我们后面还要在这个坑里挣扎很久。

留个习题：

```python
a = True
b = not a  # 不记得not请回顾 6.bool
```

想想下面这些逻辑运算的结果，然后用 print 输出看看你想的对不对：

```python
a = True
b = not a  # 不记得not请回顾 6.bool

b
print(b)
# False

print(not b)
# True

print(a == b)
# False

print(a != b)
# True

print(a and b)
# False

print(a or b)
# True

print(1 < 2 and b == True)
# False

```


<div STYLE="page-break-after: always;"></div>

## 【Python 第12课】for循环

> https://python666.cn/cls/lesson/13/

大家对 while 循环已经有点熟悉了吧？今天我们来讲另一种循环语句：

**for ... in ...**

同 while 一样，for 循环可以用来重复做一件事情。在某些场景下，它比 while 更好用。

比如之前的一道习题：**输出1到100**（公众号中的练习题3）。

我们用while来做，需要有一个值来记录已经做了多少次，还需要在 while 后面判断是不是到了100。

如果用for循环，则可以这么写：

```python
for i in range(1, 101):
    print(i)

```

解释一下，**range(1, 101)** 表示从1开始，到101为止（不包括101，注意这里和 randint 不一样），取其中所有的整数。

**for i in range(1, 101)** 就是说，把这些数，依次赋值给变量i。

相当于一个一个循环过去，第一次 i = 1，第二次 i = 2，……，直到 i = 100。当 i = 101 时跳出循环。

所以，当你需要一个循环10次的循环，你就只需要写：

```python
for i in range(1, 11)
```

或者

```python
for i in range(0, 10)
```

区别在于前者i是从1到10，后者 i 是从0到9。当然，你也可以不用 i 这个变量名，换成其他合法的变量名也可以。

比如一个循环n次的循环：

```python
for count in range(0, n)
```

for 循环的本质是对一个序列中的元素进行遍历。什么是序列，以后再说。先记住这个最简单的形式：

```python
for i in range(a, b)
```

就是从 a 循环至 b-1

现在，你可以用 for 循环来改写 [习题3~习题6](http://mp.weixin.qq.com/mp/homepage?__biz=MjM5MDEyMDk4Mw==&hid=3&sn=08af41239ec5d518ac25edb0f9167cc0&scene=18#wechat_redirect) 了。（小程序无法跳转的话可从公众号内菜单进入习题）

### \#======== 作业练习 ========#

#### 输出累计求和

于是，利用变量、循环、累加，可以写一个程序，来完成传说中高斯大牛在小时候做过的题：

1+2+3+...+100=?

从1加到100等于多少？

```python
# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Test_Sum100_for.py
@Time    :   2020/03/29 10:25:34
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# 输出1+2+3+...+100的和
# 例：
# 5050

x = 1
sum = 0

for x in range(1, 101):
    sum += x
    x += 1
    print("1 to ", x-1, ", the sum is: ", sum)

print("Final Sum of 1 to 100 is: ", sum)

```

提示：你可以用一个变量a记录现在加到几了，再用一个变量b记录加出来的结果，通过while来判断是不是加到100了。

####  输出等比数列前10项

```python
# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Test_Output_Proportional_Sequence_for.py
@Time    :   2020/03/29 10:28:38
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# Proportional sequence output
# 输入一个大于等于3的值n，输出斐波纳契数列的前n项。
# # 注：斐波纳契数列：1,1,2,3,5,8,13,21...前两项为1，从第3项起，每一项是前两项的和

# 例：
# 输入
# 7
# 输出
# 1
# 1
# 2
# 3
# 5
# 8
# 13

print("Pls input Proportional number")

q = int(input())
n = 1
an = 1

for n in range(1, q):
    print(an)
    an *= q
    n += 1

```

> **有时治愈，常常帮助，总是安慰**。--特鲁多

#### 输出斐波纳契数列的前n项

```python
# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Test_Output_Fibonacci_Series_for.py
@Time    :   2020/03/29 10:31:04
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# Test_Output_Fibonacci_Series
# 输入一个大于等于3的值n，输出斐波纳契数列的前n项。
# 注：斐波纳契数列：1,1,2,3,5,8,13,21...前两项为1，从第3项起，每一项是前两项的和

# 例：
# 输入
# 7
# 输出
# 1
# 1
# 2
# 3
# 5
# 8
# 13

print("Pls input Fibonacci Series number")

n = int(float(input()))
x = 3
a1 = 1
a2 = 1
print(a1)
print(a2)

for x in range(1, n):
    a3 = a1 + a2
    print(a3)
    a1 = a2
    a2 = a3
    x += 1

```


<div STYLE="page-break-after: always;"></div>

## 【Python 第13课】字符串

> https://python666.cn/cls/lesson/14/

字符串就是一组字符的序列（序列！又见序列！还记得我在说 for 循环的时候就提到过的序列吗？今天仍然不去细说它。），它一向是编程中的常见问题。之前我们用过它，以后我们还要不停地用它。

python中最常用的字符串表示方式是单引号（''）和双引号（""）。我还是要再说：一定得是英文标点！

**'string'** 和 **"string"** 对于 Python 来说效果是一样的。

可以直接输出一个字符串

```python
print('good')
```

也可以用一个变量来保存字符串，然后输出

```python
str = "bad"
print(str)
```

如果你想表示一段带有英文单引号或者双引号的文字，那么表示这个字符串的引号就要与内容区别开。

内容带有单引号，就用双引号表示

```python
"It's good"
```

反之亦然

```python
'You are a "BAD" man'
```

还有一种在字符串中表示引号的方法，就是用 **\**，可以不受引号的限制

**\'** 表示单引号，**\"** 表示双引号

```python
'I\'m a \"good\" teacher'
```

**\** 被称作**转义字符**，除了用来表示引号，还有比如用

- ***\*\n\** 表示字符串中的换行（相当于按一下回车键的效果）**
- ***\*\t\** 表示字符串中的制表符（相当于按一下tab键的效果）**
- ***\*\\*\* 表示字符串中的 \**\*\*** （因为单个斜杠被用来做转义了，所以真的要表示 \ 字符，就要两个斜杠）

**\\** 还有个用处，就是用来在代码中换行，而不影响输出的结果：

```python
"this is the \
same line"
```

这个字符串仍然只有一行，和

```python
"this is the same line"
```

是一样的，只是在代码中换了行。当你要写一行很长的代码时，这个会派上用场。

python中还有一种表示字符串的方法：

三个引号（'''）或者（"""）

在三个引号中，你可以方便地使用单引号和双引号，并且可以直接换行

```python
'''
"What's your name?" I asked.
"I'm Han Meimei."
'''
```

### \#======== 课后作业 =========#

用print输出以下文字：

```markup
#1
He said, "I'm yours!"

#2
\\_v_//

#3
Stay hungry,
stay foolish.
             -- Steve Jobs

#4
*
***
*****
***
*

#5 
输入一个大于等于1的值n，输出星号（*）组成的等腰三角形，底边长为n

例：
输入
3
输出
  *
 * *
* * *


n = input()
for i in range(1, n+1): # n row
   for j in range(0, n-i): # i row, need n-1 blank
      print(' ',end='')
   for j in range(0, i): # i row, need i *
      print('*',end='')
   print() # blank row
```

 


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>


<div STYLE="page-break-after: always;"></div>



## 每日一题

> https://res.crossincode.com/wechat/exercise.html

### 找数字

```python
# 今天的坑： 
# 有一个字符串 
# text = "aAsmr3idd4bgs7Dlsf9eAF" 
# 请将text字符串中的数字取出，并输出成一个新的字符串。 

上一个坑，取出字符串中的数字，在论坛上出现了好几种方法。除了基本的遍历判断来做外，还有一些简便的python解法：

1.正则
''.join(re.findall(r'\d+',text))

2.isdigit
''.join([i for i in text if i.isdigit()])
[i for i in test]这是一种生成list的方法，通过后面的if可以增加生成时的过滤条件。这种写法在python中很常用。

3.filter
filter(lambda x: x.isdigit(), text)
filter是一个过滤器，其中的lambda表达式是过滤的条件。这个稍微高深了一点，有兴趣的同学可以去搜索一下“lambda表达式”。
```

### 查找文件

```python
# 找出指定文件夹中的所有以txt结尾的文件，包括所有嵌套的子文件夹。
# 解决这个问题的好方法就是用os模块的walk方法，它可以遍历一个文件夹下的所有文件，包括嵌套的子文件夹。
# 这里给一个示例代码：
import os
import fnmatch

def findfile(inputdir):
    txtlist = []
    for parent, dirnames, filename in os.walk(inputdir):
        print filename
        for filenames in filename:
            txtlist.append(filenames)
    return fnmatch.filter(txtlist, '*.txt')

# 这里还用到了fnmatch模块的filter方法，用了匹配符合规定的文件名。
# 当然你也可以用字符串的endswith来做。
```

### 文字竖排

```python
# 把一段字符串用“右起竖排”的古文格式输出，并且拿竖线符号作为每一列的分割符。
# 比如这段文字：
"静夜思 李白床前明月光，疑似地上霜。举头望明月，低头思故乡。"

输出结果：

低┊举┊疑┊床┊静
头┊头┊似┊前┊夜
思┊望┊地┊明┊思
故┊明┊上┊月┊ 
乡┊月┊霜┊光┊李
。┊，┊。┊，┊白

# 你可以选择按标点划分成新队列，或者按照固定长度划分新队列，
# 然后再按照元素在队列中的位置，重新整合成新队列输出。
# 具体实现就不在微信里发了。
```

### 查找文件内容

```python
# 今天就是在之前“查找文件”的基础上，增加对文件内容的检索。

# 仍然是设定某个文件夹，不同的是要再增加一个文本参数，然后列出这个文件夹（含所有子文件夹）里，
# 所有文件内容包括这个搜索文本的文件。
```







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