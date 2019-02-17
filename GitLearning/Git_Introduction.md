# Git的使用简介

Git是一个版本控制系统，用来追踪计算机文件的变化的工具，也是一个供多人使用的协同工具。它是一个分布式的版本控制系统，本文将简单介绍如何使用。简单来说，就是你要和你的伙伴一起完成一项任务，但是你们要互相交换修改，查看自己的历史版本等。版本控制系统就是帮助我们做这个的。

Git的使用简介（简单明了不废话）

网上一堆教程，难得讲得清楚的。这里也不废话介绍原理之类的，直接说明如何使用。由于Git是一个分布式文件控制系统，所以一般采用一个服务器方便大家交换修改用的。每个人本地都有一个版本库，保存自己的历史版本，然后每个人可以把自己的修改提交到服务器上，被人就可以获取你的修改了。因此，Git的版本库（Repository）对于每个人来说有两个，一个是远程的，一个是本地的。这篇博客就是描述怎么从远程服务器克隆版本到本地，以及如何分享本地修改到远程的。

## 一、从远程仓库中下载到本地

这个就是说我在远程服务器（或者是GitHub上公开的项目）的有一个项目，并且该项目是放在了类似GitHub的版本控制系统上，例如我们自己在一个远程的Linux上搭建了GitLab服务然后供大家使用（GitHub是免费的公开的项目分享，可以搭建私有的库，但是私有库是收费的，所以一般大家自己有服务器就在自己服务器上安装一个GitLab服务就好了）。现在GitHub或者是我们自己的GitLab上有个项目，并且我们也是有权限访问的，那么这小节介绍的就是如何把远程项目导入到本地。

1.1、首先打开git的界面（一般git都是用命令操作比较多，安装好git之后，打开git.bash就可以了）之后设置一下全局变量（也就是你访问git时候的用户名和邮箱了），如果是公开的项目可以省略这一步。

```bash
git config --global user.name "dufei"
git config --global user.email "dufeizj@163.com"
git config --list
```

1.2、进入你想把项目存到本地的位置，比如我想存到本地D盘的GitTest文件夹中，那就使用Git.bash进入到这个文件夹（没有就创建一个），然后执行"git init"初始化这个文件夹（也就是在这个文件夹下创建一个.git文件夹，将一些配置信息放进来）

```bash
cd d:/gittest
git init
mkdir testgit
cd testgit
pwd

git add .
git add readme.txt
git commit -m "add readme.txt"
git status
git diff readme.txt

git add .
git commit -m "modify readme.txt"
git log
git log –pretty=oneline
```

那如果要回退到前100个版本的话，使用上面的方法肯定不方便，我们可以使用下面的简便命令操作：

```bash
git reset --hard HEAD~100
```

如果想回退到上一个版本的命令如下操作：

```bash
git reset --hard HEAD^
cat readme.txt
```

git reset --hard 版本号 ，但是现在的问题假如我已经关掉过一次命令行或者333内容的版本号我并不知道呢？要如何知道增加3333内容的版本号呢？可以通过如下命令即可获取到版本号：git reflog 演示如下

git reset --hard 6fcfc89来恢复了。演示如下：

如下图所示

Git的使用简介（简单明了不废话）

1.3、找到你想克隆到本地项目的远程仓库地址，例如我想从GitHub上拷贝我的WebTemplate项目到本地，那么就执行git clone命令：git clone 如下图所示

Git的使用简介（简单明了不废话）


接下来等一会这个项目就会克隆到本地了。查看一下本地就能看到这个项目了。接下来就可以基于这个项目进行开发了。

## 二、将本地已有项目分享到远程仓库中

这小节就是说你远程已经建立了一个空的仓库，现在需要把本地的某个项目分享到远程的仓库中。

2.1、打开终端，然后进入你项目所在的目录，执行如下命令，对目录初始化，这样就会在这个项目的文件夹下多了.git文件夹了，和上面类似。

```bash
cd d:/gittest/WebTemplate
git init
```

2.2、将当前项目下所有的文件添加到本地的git仓库的暂存区（如果只想共享一部分，那就不用.，就把对应的文件或者文件夹列出来就行，这里用add表示将当前文件放到暂存区，其实并没有提交）

```bash
git add .
```

2.3、接下来提交暂存区文件到本地仓库，使用git commit命令，后面-m表示message，意思是提交本次修改的信息。

```bash
git commit -m "inital commit"
```

2.4、将本地库与远程库进行关联，这时候假设你在远程库上已经有了一个仓库，比如我的WebTemplate项目的远程地址就是： ，那么关联操作命令如下：

git remote add origin https://github.com/df19900725/WebTemplate.git

这里git remote表示对远程仓库的操作，origin是远程仓库本体（默认分支名称），add表示将远程的库加入，也就是关联的操作，接下来我们使用git remote -v命令查看关联结果发现已经关联上了：

```bash
git remote -v
```

如下图所示

Git的使用简介（简单明了不废话）

2.5、最后把本地文件进行提交即可

```bash
git push origin master
```

git push表示提交代码的意思，origin表示远程的分支名称，master表示本地分支名称，上面代码就是说把本地的master分支推送到远程端，操作之后可以在远程看到了。

## 三、从远程仓库更新本地文件

多人协作开发的时候，每次开发前第一步是从远程将别人提交的修改更新到本地，因为如果你不更新直接编程会导致自己的版本号比远程新，特别容易造成冲突。所以一般先更新再提交修改。从远程更新时候第一步先查看一下远程的分支情况，然后将指定的分支更新到本地。

3.1、查看远程分支

```bash
git remote -v
```

如下图所示

Git的使用简介（简单明了不废话）

我们看到远程只有一个origin分支，那么我们直接根据这个更新就可以了。

3.2、将远程修改更新到本地

```bash
git fetch origin master
```


Git的使用简介（简单明了不废话）

前面说过origin是远程仓库分支，master是本地分支，所以这个命令就是将远程分支更新到本地。

3.3、合并远程与本地

```bash
git merge origin/master
```

远程修改更新到本地之后要做merge操作才能看到最终修改。

Git的使用简介（简单明了不废话）

当然git fetch -> git merge 操作可以使用git pull代替。这样只要执行一步就好了。

```bash
git pull
```


Git的使用简介（简单明了不废话）

## 四、将本地修改提交到远程

提交本地修改到远程三步，第一步是add文件，表示要提交修改的文件，第二步commit代码到暂存区，第三步push代码到远程仓库，其实在第一小节我们已经说过了。

```bash
git add README.md
git commit README.md 'test'
git push origin master
```

如果是提交GitHub之类的可能还要用户名密码登录：



## 五、删除将本地修改提交到远程

### 删除单个文件

如果只是删除本地的一个文件，通常是物理删除，然后git删除，再提交即可。

```bash
 rm test.txt
 git status
 git rm test.txt
 git commit -m "remove test.txt"
 git push 
```

### 还原那些误删的文件

另一种情况是删错了，因为版本库里还有呢，所以可以很轻松地把误删的文件恢复到最新版本：

```bash
$ git checkout -- test.txt
```

`git checkout`其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。

### 批量删除多个文件

在项目根目录使用命令`git add -A`然后使用命令`git commit -m "del"` 再然后要使用 `git push`推送到远程服务器

建议每一次add之后再次使用`git status`命令来查看是否已经stage了

如果你要上传删除（全部上传）
`git add --all`



# Git 日常发布流程

```{sh}
# 本地如果无远程代码，先做这步，不然就忽略 
git clone git@github.com:heiniuhaha/heiniuhaha.github.com.git

# 定位到你blog的目录下 
cd .ssh/heiniuhaha.github.com

# 配置用户名
git config --global user.name "xiangxing98"

# 配置邮箱
git config --global user.email "xiangxing985529@163.com"

# 配置项的列表
git config --list

# 创建SSH Key(添加Github远程库时需要)
# 在用户主目录下(我的win7，在C:\Users\**\下)，看看有没有.ssh目录.
# 如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，
# 如果已经有了，可直接跳到下一步。
# 如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：
ssh-keygen -t rsa -C "xiangxing985529@163.com"

# Generating public/private rsa key pair.
# Enter file in which to save the key (/c/Users/xiang/.ssh/id_rsa):
# Created directory '/c/Users/xiang/.ssh'.
# Enter passphrase (empty for no passphrase):
# Enter same passphrase again:
# Your identification has been saved in /c/Users/xiang/.ssh/id_rsa.
# Your public key has been saved in /c/Users/xiang/.ssh/id_rsa.pub.
# The key fingerprint is:
# SHA256:3rno58FajjxAb39mP9WXNfmo3S0ca3zzxZuhqMUFA+4 xiangxing985529@163.com
# The key's randomart image is:
# +---[RSA 2048]----+
# |         .       |
# |        . .      |
# |         . o    .|
# |      . .   o  o.|
# |     . .SE   . .*|
# |      ..oo... oo=|
# |       o..*o = *=|
# |       ..*+o* X.O|
# |       .*=== +.*+|
# +----[SHA256]-----+

 cat /c/Users/xiang/.ssh/id_rsa.pub

# 如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件.
# 这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，
# 可以放心地告诉任何人。
# 登陆GitHub，打开“Account settings”，“SSH Keys”页面,点“Add SSH Key”，填上任意Title，在Key文本框里粘贴公钥id_rsa.pub文件的内容.

#测试SSH 执行
ssh -T git@github.com
# 对于 oschina 的 “码云” ，执行 ssh -T git@git.oschina.net
# 对于 coding 的 “码市” ，执行 ssh -T git@git.coding.net
# The authenticity of host 'github.com (13.250.177.223)' can't be established.
# RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
# Are you sure you want to continue connecting (yes/no)? yes
# Warning: Permanently added 'github.com,13.250.177.223' (RSA) to the list of known hosts.

# Hi xiangxing98! You've successfully authenticated, but GitHub does not provide shell access.


# 显示当前的Git配置
git config --list

# 编辑Git配置文件，# .config文件在C:\Users\你的用户名\.gitconfig
git config -e --global
git config --global --edit

# 设置提交代码时的用户信息
git config [--global] user.name "[name]"
git config [--global] user.email "[email address]"


# 先同步远程文件，后面的参数会自动连接你远程的文件
git pull origin master

# 查看本地自己修改了多少文件
git status 

# 添加远程不存在的git文件
git add . 

# 提交到本地版本库
git commit * -m "what I want told to someone" 

# 更新到远程服务器上
git push origin master
```