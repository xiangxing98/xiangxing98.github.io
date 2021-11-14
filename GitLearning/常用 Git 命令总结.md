# 常用 Git 命令总结.md

> Stone Hou 2015-12-24 15:46:13 collect from <http://www.pythontab.com/html/2015/linuxkaiyuan_1224/999.html> & <https://www.jianshu.com/p/75b9a88bd4f9>

下面是常用 Git 命令清单。几个专用名词的译名如下。

Workspace：工作区

Index / Stage：暂存区

Repository：仓库区（或本地仓库）

Remote：远程仓库

## git原理

究竟git是如何工作的？打开.git目录便可一目了然。

- HEAD 指向当前分支

- config 项目配置文件

- description 供GitWeb程序使用

- hooks/ 客户端与服务端钩子脚本

- info/ 忽略模式

- index 暂存区域信息

- objects/ 所有数据内容

- refs/ 指向所有commit的指针

HEAD文件中是形如以下代码的内容：ref: refs/heads/dev，它指向refs/heads/dev，而dev文件中代码指向当前分支最近的commit对象

objects目录中保存有所有git对象，这些对象取sha-1值的前两个字母为一个目录，剩下的38个字符作为文件名保存，在上一节“git中对象”中能查看到的所有git对象都保存在这个目录中，可以使用`git cat-file <sha-1>`来获取对象内容。

```bash
git cat-file -p 63a46849
```

不妨多使用cat-file命名多看看各种对象的内容，有助于理解git对象的结构。

refs目录中保存了git中使用的所有引用或指针，因为不可能任何时候都是用sha-1值来指代对象， git对象也可以有“缩略名”。通常refs目录会包含以下目录：

- heads 保存所有分支的HEAD指针

- remotes 保存远程仓库信息

- tags 保存所有tag指针

逐一地查看这些文件内容，你就什么都明白了。使用 git update-ref 命令可以直接新建一个引用。

```bash
git update-ref refs/heads/test-branch c56dce
git update-ref refs/tags/test-tag c56dce
```

执行上述命令，这样你的git版本库中就多了一个test-branch分支和一个名为test-tag的tag。

其他的比如git还有些底层的命令，我在文中所列举的，包括之前基础篇的都是一些高级命令。

可以使用这些底层命名直接对git库进行一些操作，有关git底层命名的详细内容，可以到网上去找找。

## git中的对象

git中包含4类对象：

- commit 提交对象
- tree 目录
- blob 文件
- tag 标记

git提交便产生一个commit对象，commit对象中包含一个tree对象，tree对象中又会包含其他的tree对象或是blob对象，blob对象是最小的组成单元，即独立的文件。每个对象都对应一个唯一的SHA-1值，只有当文件或目录有修改时这个值才会重新计算发生改变。

```bash
# 可以查看所有commit对象
git log

# 查看commit对象中的tree对象
git ls-tree <commit>

# 查看blob的具体内容
git show <blob>
```

## 一、新建本地代码库-本地代码库初始化

```bash
# 查看环境变量内是否有git
git
git --version

# ubuntu下安装git
sudo apt-get install git  
```



### 1.1 通过 git clone 实现-初始化本地仓库

```bash
# 先在桌面创建一个文件夹，在这里我创建的文件夹名称是 MAD_Repo
cd Desktop/MAD_Repo 

# 下载一个项目和它的整个代码历史
git clone [project-path]

#Gitee
$ git clone https://gitee.com/yourname/repository
$ git clone https://gitee.com/Cait7/learngit

#Github
$ git clone https://github.com/yourname/repository.git

#yourname  您在码云或github注册的用户名
#repository  您创建的远程仓库名称
```



### 1.2 通过init初始化本地项目

```bash
# 先在桌面创建一个文件夹，在这里我创建的文件夹名称是 MAD_Repo
cd Desktop/MAD_Repo 
# 在当前目录新建一个Git代码库目录，将其初始化为Git代码库
git init [project-name]

#Gitee
$ cd d:/test //首先在文件系统中创建一个项目文件夹，然后在Git中 cd 到这个工程目录
$ git init //初始化本地项目
$ git remote add origin <远程仓库地址> //绑定远程仓库
#注:地址形式为 https://gitee.com/yourname/test.git 或 git@gitee.com:yourname/test.git

#Github
$ cd d:/test
$ git init
$ git remote add origin <远程仓库地址>
#注：地址形式为 https://github.com/yourname/test.git

```

## 二、本地git配置

### 配置用户名与登陆邮件

git配置文件根据作用域的不同分为三种：

- 系统配置文件（git安装目录/gitconfig）

- 用户配置文件（用户主目录/.gitconfig）

- 项目配置文件（.git/config）

git配置项都通过git config命令写入，传入不同参数写入不同的配置文件, 具体的配置项设置参考帮助文档，`$ git config –help`

```bash
# 具体的配置项设置参考帮助文档
config –help
# git config --system/--global/

# 写入系统配置
git config –-system

# 写入用户配置
git config –-global

# 写入项目配置
git config
```

Git的设置文件为.gitconfig，它可以在用户主目录下（全局配置），也可以在项目目录下（项目配置）。

name尽量和码云或GitHub保持一致，但email必须是码云或GitHub注册时使用的邮箱。命令不分前后，没有顺序。

```{bash}
# 显示当前的Git配置
git config --list

# 编辑Git配置文件
git config -e [--global]

# 设置提交代码时的用户信息
git config [--global] user.name "[name]"
git config [--global] user.email "[email address]"

# 设置用户邮箱
git config --global user.email "XXXXX@qq.com"
# 设置用户名
git config --global user.name "GavinSimons"  

# 修改配置参数
git config --global --edit
```

### 排除忽略文件、目录规则的维护ignore

在一个git版本仓库中，有时候很多文件/目录并不需要使用git进行版本维护，那么就可以将这些文件/目录加入.gitignore文件中，在.gitignore文件中可定义要排除在git版本管理之外的文件/目录，git默认会读取项目目录下的.gitignore文件。

.gitignore使用标准的shell glob模式匹配，shell glob你可以简单地理解为一种特特殊化的正则表达式，其实要比正则表达式简单许多，语法如下：

- 允许使用空行，没有实际语法作用

- \# 开头的行视作注释

- ! 开头的模式会覆盖之前的定义，将匹配的对象重新加入跟踪列表

- 以/结尾的模式，git会屏蔽掉该目录及其所有子目录及文件（只屏蔽目录）

- 不以/结尾的模式，git屏蔽同名的文件名及目录（屏蔽目录和同名文件）

- 以/开头的模式，git只会屏蔽项目根目录下的匹配对象

示例：**.gitignore example**

```gitignore
.txt
.gitignore
!readme.txt
exclude/*.txt
```

该.gitignore中定义的屏蔽规则为：

屏蔽所有的txt文件，但是readme.txt例外；

屏蔽所有的.gitignore文件；

屏蔽exclude目录下的所有txt文件（包括readme.txt）。

另外，还可以在配置项中通过core.excludesfile来指定ignore文件。

```bash
git config core.excludesfile '_myignore'
```

关于**忽略特殊文件.gitignore**

```bash
# 被.gitignore屏蔽的文件，采用这种方式，强制加入stage
git add -f file

# 查看哪个规则屏蔽了file文件
git check-ignore -v file  
```

### 获取SSHKey

首先要在本地创建一个ssh key 这个的目的就是你现在需要在你电脑上获得一个密匙。

按如下命令来生成sshkey:

```python
$ ssh-keygen -t rsa -C "youremail@youremail.com"  

# Generating public/private rsa key pair...
# 三次回车即可生成 ssh key
```

查看你的 public key

```python
$ cat ~/.ssh/id_rsa.pub
# ssh-rsa AAAAB3NzaC1yc2E... youremail@youremail.com

```

并把他添加到Gitee（gitee.com [SSHKey添加地址](http://git.oschina.net/profile/sshkeys)）或者github

添加后，在终端中输入

```PYTHON
#Gitee
$ ssh -T git@gitee.com

#GitHub
$ ssh -T git@github.com
```

第一次绑定的时候输入上边的代码之后会提示是否continue,输入yes后程序会自动连接，如果要求登录，直接输入登录信息即可。

再次执行上面的命令，检查是否成功连接，如果返回一下信息，则表示添加成功

```python
#Gitee
Welcome to Gitee.com, YourName!
 
#GitHub
You've successfully authenticated, but GitHub does not provide shell access.
```





## 三、增加/删除文件

```{bash}
# 添加指定文件到暂存区
git add [file1] [file2] ...

# 添加指定目录到暂存区，包括子目录
git add [dir]

# 添加当前目录的所有文件到暂存区
git add .

# 删除工作区文件，并且将这次删除放入暂存区
git rm [file1] [file2] ...
git rm file  # 从版本库中删除file文件
# git checkout其实是用版本库里的版本替换工作区的版本，无论工作区修改还是删除，都可"一键还原"

#  -f to force removal
git rm -f .\GitLearning\001-Git_Note_Advanced.md

# 停止追踪指定文件，但该文件会保留在工作区
git rm --cached [file]

# 改名文件，并且将这个改名放入暂存区
git mv [file-original] [file-renamed]
```

## 四、代码提交

```{bash}
# 提交暂存区到仓库区
git commit -m [message]

# 提交暂存区的指定文件到仓库区
git commit [file1] [file2] ... -m [message]

# 提交工作区自上次commit之后的变化，直接到仓库区
git commit -a

# 提交时显示所有diff信息
git commit -v

# 使用一次新的commit，替代上一次提交
# 如果代码没有任何新变化，则用来改写上一次commit的提交信息
git commit --amend -m [message]

# 重做上一次commit，并包括指定文件的新变化
git commit --amend   ...
```

## 五、分支管理

建议多使用分支来维护项目，便于保证主干的稳定性。

```{bash}
# 列出所有本地分支，查看当前分支,当前分支会在分支前加以星号（*）标注。
git branch

# 查看已合并的分支
git branch --merge

# 查看未合并的分支
git branch --no-merged

# git branch -v命令将附加显示最后一次提交相关信息的分支信息
git branch -v

# 列出所有远程分支
git branch -r

# 列出所有本地分支和远程分支
git branch -a

# 新建一个分支，但依然停留在当前分支
git branch [branch-name]
# 创建分支, git中创建分支的方法非常简单,git branch <branch-name>
git branch dev

# 新建一个分支，并切换到该分支，使用checkout -b命令来创建分支后并切换到新的分支
git checkout -b [branch]
# 创建dev分支， 并切换到dev分支（相当于以下两条命令）
git checkout -b dev  
git branch dev  # 创建dev分支
git checkout dev  # 切换到dev分支

# 新建一个分支，指向指定commit
git branch [branch] [commit]

# 新建一个分支，与指定的远程分支建立追踪关系
git branch --track [branch] [remote-branch]

# 切换到指定分支，并更新工作区
git checkout [branch-name]
# 假设从当前分支创建了一个名为dev的分支，可以让此分支作为开发分支。
# 使用checkout <branch-name>可以很方便地在分支间进行切换：
git checkout master
git checkout dev

# 建立追踪关系，在现有分支与指定的远程分支之间
git branch --set-upstream [branch] [remote-branch]


# 分支合并
# 当一个分支完成预期的工作，通过测试后，便可合并到主干，作为稳定版本进行后续开发，
# 合并分支的命令非常简单：git merge branch-name, 合并指定分支到当前分支
git merge [branch]
# 把dev分支合并到当前分支
git merge dev
# 如果顺利，dev分支将自动地合并到当前分支。
# 当然很多时候会产生冲突，这个时候就需要手动坚决冲突后再进行合并。

# 把issue-101分支合并到当前分支，并提交说明
git merge --no-ff -m "message" issue-101  

# 选择一个commit，合并进当前分支
git cherry-pick [commit]

# 删除分支
git branch -d [branch-name]
# 删除dev分支
git branch -d dev

# 强制删除分支
git branch -D <branch-name>

# 重命名分支
git branch -rm <old-branch> <new-branch>

# 远程分支
# 删除远程分支
git push origin --delete $ git branch -dr

# 删除远程分支
$ git push <remote> :<remote-branch-name>
# 这个命令是不是可以从推送本地分支到远程分支的命令中得到一点灵感？
# 是的，省略本地分支名后，远程分支即被删除！

#推送本地分支到远程服务器
git push <remote> <branch-name>[:<remote-branch-name>]

# 远程分支名如果省略，则使用本地分支名作为远程分支名
git push <remote> <branch-name>
```

### conflict冲突

conflict在git中如遇冲突，会显示冲突提示，合并会中断conflict, 此时你可以使用git mergetool命令调用merge工具进行手动合并.

```bash
git mergetool
# mergetool在配置项进行配置，以下是使用vimdiff的merge操作界面
mergetool vimdiff
```

手动解决完冲突后，还需要进行一次提交，便完成了整个手动合并过程。

### 解决merge时出现的冲突

当你和其他团队成员对同一个文件进行修改后，merge的时候有可能会出现冲突。你可以打开每个冲突的文件，手工解决冲突；也可以借助冲突处理工具来解决冲突。

这里分别介绍这两种方式：

#### 1. 手工解决冲突

冲突提示如下图所示：

CONFLICT表示有冲突，在这一行的末尾，显示冲突文件。这里有两个文件冲突，分别是README.md和app.iml

这里以README.md为例，解决冲突：

被红框框住的符号 ======= 是冲突的分割线。

<<<<<<< HEAD 和分割线之间的是本地的文本，

分割线和 >>>>>>> upstream/dev 之间的是远程分支的文本

你可以选择保留其中一个版本的文本，然后将三个冲突符号都删除。这样表示已解决冲突。

如果你想同时保留两个版本，那么只需将冲突符号删除。

解决冲突后如下图所示：

#### 2. 借助冲突处理工具

个人认为Meld这个工具比较好用，Android Studio自带的冲突处理工具和它很相似。

我用过tortoisegit的工具，感觉没有Meld好用，这里就不介绍了。

（1） 首先去Meld的官网下载安装文件并安装。->点此进入Meld官网

（2） 安装完后，打开你的git工具，比如msysgit。
执行 `git config --edit --global` ，此时会打开一个配置文件。在文件最后添加以下四行：

```bash
    [merge]  
             tool = meld  
    [mergetool "meld"]
             path = e:/software/MeldMergeTool/Meld.exe  
```

提示：path是根据你安装Meld的路径来决定的，同时要把路径中的 \ 改成 / 。
从上面可以看出我的安装路径为 e:\software\MeldMergeTool\ 。

（3） 在merge的时候，如果出现冲突，运行命令 git mergetool 这时就会打开Meld。

（4） Meld的界面如下：

冲突的地方会显示红色，如果你想保留本地的代码，则点击左边的 → 箭头。
把所有红色（冲突）区域解决后，可以根据实际情况去解决绿色（添加）和灰色（更改）。
一般保存中间的修改就行。如上图红框处。

## 六、标签tag

在git中可以为任意其他对象添加tag，包括commit，tree，blob，甚至包括tag自身。git中都是用sha-1标识git对象，这是一个40个字符长度的字符串，不方便记忆，那么可为git对象添加一个tag便于标识不同对象。

```{bash}
# 列出所有tag
git tag

# 当然可以筛选
git tag -l 'v1.*'

# 新建一个tag在当前commit
git tag [tag]

# 新建一个tag在指定commit
git tag [tag] [commit]
# 添加tag
# git tag tag-name sha-1
git tag v1.0 bdc390c2
# 这样便为bdc390c2的对象添加了一个tag，如果不指定sha-1，会为最近的一个commit对象添加tag

# 查看tag信息
git show [tag]

# 提交指定tag
git push [remote] [tag]

# 提交所有tag
git push [remote] --tags

# 新建一个分支，指向某个tag
git checkout -b [branch] [tag]

# 删除tag
git tag -d <tag-name>

# 重命名tag,重命名tag有两种方式：
# 1. 删除原tag，重新添加
# 2. git tag -f 强制替换已存在的tag后，再删除原tag
git tag -f <new-tag> <old-tag>
git tag -d <old-tag>
```

### tag的分类

- 轻量型标签

轻量型标签直接使用 `$ git tag <tag-name> <git-object>` 即可创建

- 标注型(annotated)标签

标注型标签可记录更多的信息，使用 `$ git tag -a <tag-name> <git-object> -m ‘tag message’`即可创建一个标注性标签

## 七、查看信息

```{bash}
# 显示有变更的文件
git status

# 显示当前分支的版本历史，版本迭代历史记录
git log

# 显示commit历史，以及每次commit发生变更的文件
git log --stat

# 显示某个文件的版本历史，包括文件改名
git log --follow [file]$ git whatchanged [file]

# 一行展示一条版本迭代历史记录
git log --pretty=oneline  

# 显示指定文件相关的每一次diff
git log -p [file]

# 显示指定文件是什么人在什么时间修改过
git blame [file]

# 显示暂存区和工作区的差异
git diff

# 显示暂存区和上一个commit的差异
git diff --cached []

# 显示工作区与当前分支最新commit之间的差异
git diff HEAD

# 显示两次提交之间的差异
git diff [first-branch]...[second-branch]

# 查看file文件差异
git diff file  

# 显示某次提交的元数据和内容变化
git show [commit]

# 显示某次提交发生变化的文件
git show --name-only [commit]

# 显示某次提交时，某个文件的内容
git show [commit]:[filename]

# 显示当前分支的最近几次提交
git reflog
```

## 八、远程同步

```{bash}
# 创建SSH Key
ssh-keygen -t rsa -C "youremail@example.com"

# 测试SSH连接
ssh -T git@github.com

# 下载远程仓库的所有变动
git fetch [remote]

# 显示所有远程仓库
git remote -v

# 显示某个远程仓库的信息
git remote show [remote]

# 增加一个新的远程仓库，并命名
git remote add [shortname] [url]
git remote add origin git@github.com:GavinSimons/XXXXX.git  # 添加远程仓库

# 取回远程仓库的变化，并与本地分支合并
git pull [remote] [branch]

# 上传本地指定分支到远程仓库
git push [remote] [branch]
git push -u origin master  # 推到远程
git push  # 把当前分支master推送到远程
git push origin master  # 推送到远程

# 强行推送当前分支到远程仓库，即使有冲突
git push [remote] --force

# 推送所有分支到远程仓库
git push [remote] --all

# 从远程克隆仓库
git clone git@github.com:GavinSimons/xxxxx.git
```

### 把本地最新的代码更新到远程仓库

```bash
git add .    //指定更新内容    . 表示全部更新，test.txt 表示更新指定文件
git commit -m "一些注释说明"     //添加更新说明
git push origin master            //执行更新操作
```

### 从远程仓库同步最新版本到本地

```bash
$ cd d:/test
$ git pull origin master
```



## 九、代码回滚、撤销

```{bash}
# 恢复暂存区的指定文件到工作区，放弃工作区file文件的修改
git checkout [file]
git checkout -- file

# 恢复某个commit的指定文件到工作区
git checkout [commit] [file]

# 恢复上一个commit的所有文件到工作区
git checkout .

# 把暂存区的修改撤销掉(unstage), 重新放回工作区
# git reset 命令既可以回退版本，也可以把暂存区的修改回退到工作区，我们用HEAD时，表示最新的版本。
git reset HEAD file  

# 重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
git reset [file]

# 重置暂存区与工作区，与上一次commit保持一致
git reset --hard

# 重置当前分支的指针为指定commit，同时重置暂存区，但工作区不变
git reset [commit]

# 重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致
git reset --hard [commit]

# 重置当前HEAD为指定commit，但保持暂存区和工作区不变
git reset --keep [commit]

# 回滚到上一版本
git reset --hard HEAD^

# 回滚到上上版本
git reset --hard HEAD^^

# 回滚到上100个版本
git reset --hard HEAD~100

# 回滚到commit id(md5) 为 4459657的版本
git reset --hard 4459657

# 查看每次命令历史记录
git reflog  

# 新建一个commit，用来撤销指定commit
# 后者的所有变化都将被前者抵消，并且应用到当前分支
git revert [commit]
```

## 十、多人协作

```{bash}
# 查看远程库信息
git remote

# 查看远程库详细信息
git remote -v

# 将该分支推送到远程库对应的远程分支上
git push origin master

# 将该分支推送到远程库dev的分支上
git push origin dev

# 将远程origin的dev分支复制到本地
git checkout -b dev origin/dev

# 将当前分支推送到远程的dev分支
git push origin dev

# 把最新提交从origin/dev抓下来
git pull  

# 设置dev和origin/dev的链接
git branch --set-upstream-to=origin/dev dev

# 创建本地分支和远程分支的链接关系
git branch --set-upstream branch-name origin/branch-name  
```

## 十一、其他

```bash
# 生成一个可供发布的压缩包
git archive

# 把当前工作现场“储藏”起来
git stash

# stash 列表
git stash list

# 恢复stash0，但stash0内容并不删除
git stash apply stash@{0}

# 删除stash0
git stash drop stash@{0}

# 恢复stash0，并自动删除
git stash pop stash@{0}

# 清屏
$ clear
```

## 相关Git报错问题

fatal: unable to access ‘’: OpenSSL SSL

Git报错：fatal: unable to access ‘’：OpenSSL SSL_connect was reset in connection to gitee.com:443

解决方法：

```
git config --global http.sslVerify ``false
```

 2：push不上去可以先pull下来试试

```
git pull origin master
```

 3:强制推送，注意会强制删除原有仓库中的某些代码

```
git push -u origin master -f
```

## rebase

rebase亦是将分支的修改进行“合并”。

但在具体行为上略有不同，使用merge进行合并，更新部分依然会视作是从分支而来；而rebase则是直接将更新合并到新分支，相当于是在合并分支的直接修改。

如果我们的更新是非常小，不足以作为一个分支进行合并，并且不想污染版本日志，那么便可以使用rebase来合并更新。

### git rebase修改已经提交的commit说明

```bash
# 01. 先用git log查看commit信息：
git log

# 02. 我打算更改下面那个commit，使用git rebase -i 版本号^

# 03. 执行命令后，会进入pick这样的界面,
# 它把我们传入的版本号之上的commit条目都显示出来了，
# 这里只关注我们要改的那一条。将第一个`pick`修改为`reword`，保存并退出。

# 04. 过一会儿，它会再进入这样的界面：
# 将第一行的Android的ListView改为这个更改后的message，保存并退出。

# 05. 再用`git log`查看
# 不仅commit message被更改了，从被更改的commit开始，commit id都会重新生成。
```

### git rebase合并commit

```bash
# 01. 先用git log查看commit信息：

# 02. 如果你想把最近的四个commit合并成一个commit，有两种方法。
# 一种是用git reset --soft d7ac，在git commit -m "新的commit message"，
# 另一种是用git rebase。接下来讲第二种。
# 首先根据上图的commit id，我想把afe14f之后的commit合并到afe14f里面，
# 执行 git rebase -i afe14f^。进入编辑界面：

# 03. 看图文界面
# 根据提示，squash会把所在的commit合并到前一个commit上面。
# 我们要合并到afe14f，所以修改后三个。
# 而在合并之后，我们需要修改afe14f的commit message，所以使用reword。
# 你也可以用缩写，比如squash的缩写是s。而reword的缩写是s

# 04. 保存并退出，会进入下一个界面。
# 修改第一行的commit message，即reword的那个message，为添加Android学习笔记，
# 特别是ListView的介绍；添加对git commit的修改教程。如下图：

# 05. 保存并退出。自动进入下一个界面：
# This is a combination of n commit
# 此时要将其他三个message去掉，只要在那三行前面加#注释掉就行了。如下图：

# 06. 保存并退出，等待git处理完成。

# 07. 再次使用git log查看commit信息,完成！

```

## Commit message写法规范

```bash
git log <last tag> HEAD --pretty=format:%s
```

每次提交，Commit message 都包括三个部分：Header，Body 和 Footer。

```bash
<type>(<scope>): <subject>
// 空一行
<body>
// 空一行
<footer>
```

其中，Header 是必需的，Body 和 Footer 可以省略。不管是哪一个部分，任何一行都不得超过72个字符（或100个字符）。这是为了避免自动换行影响美观。

### 1. Header部分

只有一行，包括三个字段：type（必需）、scope（可选）和subject（必需）

（1）type

type用于说明 commit 的类别，只允许使用下面7个标识。

- feat：新功能（feature）

- fix：修补bug

- docs：文档（documentation）

- style： 格式（不影响代码运行的变动）

- refactor：重构（即不是新增功能，也不是修改bug的代码变动）

- test：增加测试

- chore：构建过程或辅助工具的变动

如果type为feat和fix，则该 commit 将肯定出现在 Change log 之中。其他情况（docs、chore、style、refactor、test）由你决定，要不要放入 Change log，建议是不要。

（2）scope

scope用于说明 commit 影响的范围，比如数据层、控制层、视图层等等，视项目不同而不同。

（3）subject

subject是 commit 目的的简短描述，不超过50个字符。

- 以动词开头，使用第一人称现在时，比如change，而不是changed或changes

- 第一个字母小写

- 结尾不加句号（.）

### 2. Body

Body 部分是对本次 commit 的详细描述，可以分成多行。下面是一个范例。

```bash
More detailed explanatory text, if necessary.  Wrap it to
about 72 characters or so.
Further paragraphs come after blank lines.
- Bullet points are okay, too
- Use a hanging indent
```

有两个注意点。

（1）使用第一人称现在时，比如使用change而不是changed或changes。

（2）应该说明代码变动的动机，以及与以前行为的对比。

### 3. Footer

Footer 部分只用于两种情况。

（1）不兼容变动

如果当前代码与上一个版本不兼容，则 Footer 部分以BREAKING CHANGE开头，后面是对变动的描述、以及变动理由和迁移方法。

```bash
BREAKING CHANGE: isolate scope bindings definition has changed.
    To migrate the code follow the example below:
    Before:
    scope: {
      myAttr: 'attribute',
    }

    After:
    scope: {
      myAttr: '@',
    }

    The removed `inject` wasn't generaly useful for directives so there should be no code using it.
```

（2）关闭 Issue

如果当前 commit 针对某个issue，那么可以在 Footer 部分关闭这个 issue 。

```bash
Closes #234
```

也可以一次关闭多个 issue 。

```bash
Closes #123, #245, #992
```

## Git 日常发布流程

```bash
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

## 常用的git命令

```bash
git init                        #把当前目录变成git可以管理的仓库
git add readme.txt              #添加一个文件，也可以添加文件夹
git add -A                      #添加全部文件
git rm test.txt                 #删除一个文件，也可以删除文件夹
git commit -a -m "some commit"  #提交修改
git status                      #查看是否还有未提交
git log                         #查看最近日志
git reset --hard HEAD^          #版本回退一个版本
git reset --hard HEAD^^         #版本回退两个版本
git reset --hard HEAD~100       #版本回退多个版本
git remote add origin +地址     #远程仓库的提交（第一次链接）
# git remote add origin git@gitee.com:liaoxuefeng/learngit.git
# git remote -v
# git remote rm origin
git push -u origin master       #仓库关联
git push                        #远程仓库的提交（第二次及之后）

# 先关联GitHub的远程库：注意，远程库的名称叫github，不叫origin了。
# git remote add github git@github.com:michaelliao/learngit.git

# 再关联Gitee的远程库：同样注意，远程库的名称叫gitee，不叫origin。
# git remote add gitee git@gitee.com:liaoxuefeng/learngit.git

# 现在，我们用git remote -v查看远程库信息，可以看到两个远程库：
git remote -v
gitee	git@gitee.com:liaoxuefeng/learngit.git (fetch)
gitee	git@gitee.com:liaoxuefeng/learngit.git (push)
github	git@github.com:michaelliao/learngit.git (fetch)
github	git@github.com:michaelliao/learngit.git (push)

# 如果要推送到GitHub，使用命令：
# git push github master

# 如果要推送到Gitee，使用命令：
# git push gitee master

# 这样一来，我们的本地库就可以同时与多个远程库互相同步：
```

更多的`git`命令，可以输入`git --help`查看

或者访问`git`命令手册：https://git-scm.com/docs

```bash
git --help
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone             Clone a repository into a new directory
   init              Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add               Add file contents to the index
   mv                Move or rename a file, a directory, or a symlink
   restore           Restore working tree files
   rm                Remove files from the working tree and from the index
   sparse-checkout   Initialize and modify the sparse-checkout

examine the history and state (see also: git help revisions)
   bisect            Use binary search to find the commit that introduced a bug
   diff              Show changes between commits, commit and working tree, etc
   grep              Print lines matching a pattern
   log               Show commit logs
   show              Show various types of objects
   status            Show the working tree status

grow, mark and tweak your common history
   branch            List, create, or delete branches
   commit            Record changes to the repository
   merge             Join two or more development histories together
   rebase            Reapply commits on top of another base tip
   reset             Reset current HEAD to the specified state
   switch            Switch branches
   tag               Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch             Download objects and refs from another repository
   pull              Fetch from and integrate with another repository or a local branch
   push              Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.


```

